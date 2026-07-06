import asyncio

from app.bot import bot
from app.api.reminders import get_due_reminders, mark_reminder_sent
import logging

logger = logging.getLogger(__name__)

async def check_and_send_reminders():

    reminders = await get_due_reminders()

    for reminder in reminders:

        try:

            text = (
                "🔔 یادآوری زمان ترمیم\n\n"
                f"سلام {reminder['first_name']} عزیز\n"
                f"زمان ترمیم خدمت «{reminder['service_name']}» شما نزدیک است.\n"
                "لطفاً برای هماهنگی، از طریق ربات نوبت جدید ثبت کنید یا با ما تماس بگیرید."
            )

            await bot.send_message(
                reminder["chat_id"],
                text
            )

            await mark_reminder_sent(reminder["id"])

        except Exception as error:

            logger.error(f"[Reminder Send Error] {error}")


async def start_reminder_worker():

    while True:

        try:
            await check_and_send_reminders()

        except Exception as error:
            logger.error(f"[Reminder Worker Error] {error}")

        await asyncio.sleep(60)