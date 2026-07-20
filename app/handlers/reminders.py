import jdatetime

from bale import Message

from app.api.services import get_services
from app.api.client import get_or_create_user
from app.api.reminders import create_reminder_api
from app.keyboards.reminders import reminder_services_keyboard
from app.states.reminder import (
    set_state,
    get_state,
    clear_state,
    is_in_reminder_flow
)


async def handle_reminders(message: Message):

    if message.text != "⏰ ثبت یادآوری زمان ترمیم":
        return False

    services = await get_services()

    if not services:
        await message.reply(
            "در حال حاضر خدماتی برای ثبت یادآوری وجود ندارد"
        )
        return True

    await message.reply(
        "لطفاً نوع خدمتی که انجام داده‌اید را انتخاب کنید:",
        components=reminder_services_keyboard(services)
    )

    return True


async def start_reminder_date_step(callback_message, service_id: int, service_name: str):

    set_state(
        callback_message.chat.id,
        step="day",
        data={
            "service_id": service_id,
            "service_name": service_name
        }
    )

    await callback_message.reply(
        "لطفاً روز انجام خدمت را به تاریخ شمسی وارد کنید (مثلاً 12):"
    )


def to_english_digits(text):

    return text.strip().translate(
        str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    )


async def handle_reminder_text(message: Message):

    if not message.text:
        return False

    if not is_in_reminder_flow(message.chat.id):
        return False

    state = get_state(message.chat.id)
    step = state.get("step")

    if step not in ("day", "month", "year"):
        return False

    raw_value = to_english_digits(message.text)

    try:
        value = int(raw_value)
    except ValueError:
        await message.reply("مقدار وارد شده معتبر نیست. لطفاً فقط عدد وارد کنید:")
        return True

    if step == "day":

        set_state(message.chat.id, step="month", data={"day": value})

        await message.reply("لطفاً ماه انجام خدمت را وارد کنید (مثلاً 05):")

        return True

    if step == "month":

        set_state(message.chat.id, step="year", data={"month": value})

        await message.reply("لطفاً سال انجام خدمت را وارد کنید (مثلاً 1403):")

        return True

    # step == "year"

    day = state.get("day")
    month = state.get("month")
    year = value

    try:

        gregorian_date = jdatetime.date(
            year,
            month,
            day
        ).togregorian()

    except ValueError:

        await message.reply(
            "تاریخ وارد شده معتبر نیست. لطفاً دوباره از «روز» شروع کنید:"
        )

        set_state(message.chat.id, step="day")

        return True

    user = await get_or_create_user(
        message.chat.id,
        message.chat.first_name,
        message.chat.last_name or ""
    )

    result, error = await create_reminder_api(
        user_id=user["id"],
        service_id=state.get("service_id"),
        procedure_date=gregorian_date.isoformat()
    )

    clear_state(message.chat.id)

    if error:

        await message.reply(
            f"⚠️ {error}"
        )

        return True

    await message.reply(
        f"✅ یادآوری زمان ترمیم «{state.get('service_name')}» شما ثبت شد.\n"
        "چند روز مانده به موعد ترمیم، از طریق همین ربات به شما یادآوری خواهیم داد."
    )

    return True