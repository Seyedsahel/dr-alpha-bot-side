from bale import Message
from app.bot import bot
from app.api.services import get_services
from app.keyboards.appointments import services_keyboard

@bot.event
async def handle_appointment_entry(message: Message):

    if message.text != "📅 ثبت نوبت":
        return False
    
    services = await get_services()

    if not services:
        await message.reply("متاسفانه در حال حاضر خدماتی برای ثبت نوبت وجود ندارد")
        return True

    await message.reply(
        "لطفاً نوع خدمات مورد نظر خود را انتخاب کنید:",
        components=services_keyboard(services)
        )
    

    return True