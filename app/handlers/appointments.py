from bale import Message


async def handle_appointments(message: Message):
    await message.reply("📅 دکمه ثبت نوبت فشرده شد.")