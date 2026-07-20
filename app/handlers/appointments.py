import re

from bale import Message
from app.bot import bot
from app.api.services import get_services
from app.api.client import get_or_create_user, update_user_contact
from app.keyboards.appointments import services_keyboard
from app.states.appointment import (
    set_state,
    get_state,
    clear_state,
    is_in_appointment_flow
)


PHONE_PATTERN = re.compile(r"^09\d{9}$")


async def show_services_step(message: Message):

    services = await get_services()

    if not services:
        await message.reply("متاسفانه در حال حاضر خدماتی برای ثبت نوبت وجود ندارد")
        return

    await message.reply(
        "لطفاً نوع خدمات مورد نظر خود را انتخاب کنید:",
        components=services_keyboard(services)
    )


@bot.event
async def handle_appointment_entry(message: Message):

    if message.text != "📅 ثبت نوبت":
        return False

    user = await get_or_create_user(
        message.chat.id,
        message.chat.first_name,
        message.chat.last_name or ""
    )

    if not user or not user.get("phone"):

        set_state(message.chat.id, step="phone")

        await message.reply(
            "برای ثبت نوبت لازمه ابتدا شماره تلفن خود را وارد کنید "
            "(مثال: 09123456789):"
        )

        return True

    await show_services_step(message)

    return True


async def handle_appointment_text(message: Message):

    if not message.text:
        return False

    if not is_in_appointment_flow(message.chat.id):
        return False

    state = get_state(message.chat.id)

    if state.get("step") != "phone":
        return False

    phone = message.text.strip()

    if not PHONE_PATTERN.match(phone):

        await message.reply(
            "شماره تلفن نامعتبر است. لطفاً یک شماره صحیح مثل 09123456789 وارد کنید:"
        )

        return True

    user = await update_user_contact(
        chat_id=message.chat.id,
        first_name=message.chat.first_name,
        last_name=message.chat.last_name or "",
        phone=phone
    )

    clear_state(message.chat.id)

    if not user:

        await message.reply(
            "خطا در ثبت شماره تلفن. لطفاً دوباره تلاش کنید."
        )

        return True

    await show_services_step(message)

    return True