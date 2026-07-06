import asyncio

from bale import Message

from app.bot import bot
from app.keyboards.main_menu import main_menu_keyboard
from app.handlers.menu import handle_menu
from app.scheduler.reminder_worker import start_reminder_worker
import logging

logger = logging.getLogger(__name__)

@bot.event
async def on_ready():

    logger.info(f"{bot.user.username} is Ready!")

    asyncio.create_task(
        start_reminder_worker()
    )


@bot.event
async def on_message(message: Message):

    if message.content == "/start":

        await bot.send_message(
            message.chat.id,
            "به ربات مطب دکتر کامرانی خوش آمدید 🌸\n\n"
            "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
            components=main_menu_keyboard()
        )

        return

    await handle_menu(message)