from bale import Message


async def handle_consultations(message: Message):
    await message.reply("📞 دکمه درخواست مشاوره فشرده شد.")