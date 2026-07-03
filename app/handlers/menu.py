from bale import Message

from app.handlers.appointments import handle_appointment_entry
from app.handlers.consultations import handle_consultations, handle_consultation_text
from app.handlers.aftercares import handle_aftercares
from app.handlers.reminders import handle_reminders, handle_reminder_text
from app.handlers.festivals import festivals_handler
from app.handlers.faq import handle_faq
from app.handlers.services import services_handler
from app.handlers.my_info import handle_my_info

from app.states.consultation import clear_state as clear_consultation_state
from app.states.reminder import clear_state as clear_reminder_state


MENU_COMMANDS = {
    "📅 ثبت نوبت",
    "📞 درخواست مشاوره",
    "💉 مراقبت‌های بعد از خدمات",
    "⏰ ثبت یادآوری زمان ترمیم",
    "🎉 جشنواره‌ها",
    "❓ سوالات متداول",
    "ℹ️ معرفی خدمات کلینیک",
    "ℹ️ اطلاعات من"
}


async def handle_menu(message: Message):

    if not message.text:
        return False

    if message.text not in MENU_COMMANDS:

        if await handle_consultation_text(message):
            return True

        if await handle_reminder_text(message):
            return True

    else:

        clear_consultation_state(message.chat.id)
        clear_reminder_state(message.chat.id)

    if message.text == "📅 ثبت نوبت":
        await handle_appointment_entry(message)

    elif message.text == "📞 درخواست مشاوره":
        await handle_consultations(message)

    elif message.text == "💉 مراقبت‌های بعد از خدمات":
        await handle_aftercares(message)

    elif message.text == "⏰ ثبت یادآوری زمان ترمیم":
        await handle_reminders(message)

    elif message.text == "🎉 جشنواره‌ها":
        await festivals_handler(message)

    elif message.text == "❓ سوالات متداول":
        await handle_faq(message)

    elif message.text == "ℹ️ معرفی خدمات کلینیک":
        await services_handler(message)

    elif message.text == "ℹ️ اطلاعات من":
        await handle_my_info(message)

    else:
        return False

    return True