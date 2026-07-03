from bale import Message

from app.api.client import get_or_create_user
from app.api.appointments import get_user_appointments
from app.api.consultations import get_user_consultations
from app.api.reminders import get_user_reminders
from app.utils.formatter import to_jalali_date


STATUS_LABELS = {
    "pending": "در انتظار بررسی",
    "called": "تماس گرفته شده",
    "closed": "بسته شده",
    "confirmed": "تایید شده",
    "cancelled": "لغو شده"
}


async def handle_my_info(message: Message):

    if message.text != "ℹ️ اطلاعات من":
        return False

    user = await get_or_create_user(
        message.chat.id,
        message.chat.first_name,
        message.chat.last_name or ""
    )

    appointments = await get_user_appointments(user["id"])
    reminders = await get_user_reminders(user["id"])
    consultations = await get_user_consultations(user["id"])

    text = "📋 اطلاعات شما\n\n"

    text += "📅 نوبت‌های شما:\n"

    if not appointments:
        text += "موردی ثبت نشده است.\n"
    else:
        for item in appointments:

            status_label = STATUS_LABELS.get(
                item.get("status"),
                item.get("status")
            )

            text += (
                f"• {item.get('service_name') or '-'} | "
                f"{to_jalali_date(item.get('slot_time'))} | "
                f"{status_label}\n"
            )

    text += "\n⏰ یادآوری‌های فعال:\n"

    if not reminders:
        text += "موردی ثبت نشده است.\n"
    else:
        for item in reminders:

            text += (
                f"• {item.get('service_name') or '-'} | "
                f"موعد یادآوری: {to_jalali_date(item.get('reminder_date'))}\n"
            )

    text += "\n📞 درخواست‌های مشاوره:\n"

    if not consultations:
        text += "موردی ثبت نشده است.\n"
    else:
        for item in consultations:

            status_label = STATUS_LABELS.get(
                item.get("status"),
                item.get("status")
            )

            text += (
                f"• {to_jalali_date(item.get('created_at'))} | {status_label}\n"
            )

    await message.reply(text)

    return True