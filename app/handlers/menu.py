from bale import Message

from app.handlers.appointments import handle_appointment_entry
from app.handlers.consultations import handle_consultations
from app.handlers.aftercares import handle_aftercares
from app.handlers.reminders import handle_reminders
from app.handlers.festivals import festivals_handler
from app.handlers.faq import handle_faq
from app.handlers.services import services_handler


async def handle_menu(message: Message):

    if not message.text:
        return False

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

    else:
        return False

    return True