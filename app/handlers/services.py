from bale import Message
from app.bot import bot
from app.api.services import get_services
from app.keyboards.services import services_keyboard

# @bot.event
async def services_handler(message: Message):
    if message.text != "ℹ️ معرفی خدمات کلینیک":
        return

    services = await get_services()

    if not services:
        await message.reply("متاسفانه در حال حاضر خدماتی برای معرفی وجود ندارد")
        return
    
    await message.reply(
        "لطفاً یکی از خدمات زیر را انتخاب کنید:",
        components=services_keyboard(services)
    )