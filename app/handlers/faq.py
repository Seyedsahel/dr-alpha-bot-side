from bale import Message


async def handle_faq(message: Message):
    await message.reply("❓ دکمه سوالات متداول فشرده شد.")