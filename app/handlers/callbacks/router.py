from bale import CallbackQuery

from app.bot import bot

from app.handlers.callbacks.services import handle_service_callback
from app.handlers.callbacks.appointments import handle_appointment_callback
from app.handlers.callbacks.aftercares import handle_aftercare_callback
from app.handlers.callbacks.reminders import handle_reminder_callback
from app.handlers.callbacks.faqs import handle_faq_callback


@bot.event
async def on_callback(callback: CallbackQuery):

    if await handle_service_callback(callback):
        return

    if await handle_appointment_callback(callback):
        return

    if await handle_aftercare_callback(callback):
        return

    if await handle_reminder_callback(callback):
        return

    if await handle_faq_callback(callback):
        return