import re

from bale import Message

from app.api.client import get_or_create_user, update_user_contact
from app.api.consultations import create_consultation_api
from app.states.consultation import (
    set_state,
    get_state,
    clear_state,
    is_in_consultation_flow
)


PHONE_PATTERN = re.compile(r"^09\d{9}$")


async def start_consultation_flow(message: Message):

    await get_or_create_user(
        message.chat.id,
        message.chat.first_name,
        message.chat.last_name or ""
    )

    set_state(message.chat.id, step="name")

    await message.reply(
        "لطفاً نام و نام خانوادگی خود را وارد کنید:"
    )


async def handle_consultations(message: Message):

    if message.text != "📞 درخواست مشاوره":
        return False

    await start_consultation_flow(message)

    return True


async def handle_consultation_text(message: Message):

    if not message.text:
        return False

    if not is_in_consultation_flow(message.chat.id):
        return False

    state = get_state(message.chat.id)
    step = state.get("step")

    if step == "name":

        full_name = message.text.strip()
        parts = full_name.split(" ", 1)

        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""

        set_state(
            message.chat.id,
            step="phone",
            data={
                "first_name": first_name,
                "last_name": last_name
            }
        )

        await message.reply(
            "لطفاً شماره تلفن خود را وارد کنید (مثال: 09123456789):"
        )

        return True

    if step == "phone":

        phone = message.text.strip()

        if not PHONE_PATTERN.match(phone):

            await message.reply(
                "شماره تلفن نامعتبر است. لطفاً یک شماره صحیح مثل 09123456789 وارد کنید:"
            )

            return True

        user = await update_user_contact(
            chat_id=message.chat.id,
            first_name=state.get("first_name"),
            last_name=state.get("last_name"),
            phone=phone
        )

        if not user:

            await message.reply(
                "خطا در ثبت اطلاعات. لطفاً دوباره تلاش کنید."
            )

            clear_state(message.chat.id)

            return True

        await create_consultation_api(
            user_id=user["id"],
            note=f"نام: {state.get('first_name')} {state.get('last_name')}\nتلفن: {phone}"
        )

        clear_state(message.chat.id)

        await message.reply(
            "✅ درخواست مشاوره شما ثبت شد. کارشناسان ما در اسرع وقت با شما تماس خواهند گرفت."
        )

        return True

    return False