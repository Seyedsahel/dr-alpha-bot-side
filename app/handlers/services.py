from bale import Message


async def handle_services(message: Message):
    await message.reply("ℹ️ دکمه معرفی خدمات کلینیک فشرده شد.")