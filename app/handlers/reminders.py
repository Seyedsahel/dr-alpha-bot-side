from bale import Message


async def handle_reminders(message: Message):
    await message.reply("⏰ دکمه ثبت یادآوری زمان ترمیم فشرده شد.")