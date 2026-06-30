from bale import CallbackQuery

from app.bot import bot
from app.api.services import get_services
from bale import InlineKeyboardMarkup, InlineKeyboardButton


@bot.event
async def on_callback(callback: CallbackQuery):
    print(callback.data)
    if not callback.data.startswith("service:"):
        return

    service_id = int(callback.data.split(":")[1])

    services = await get_services()

    service = next(
        (
            item
            for item in services
            if item["id"] == service_id
        ),
        None
    )

    if service is None:
        await callback.message.reply(
            "این سرویس یافت نشد."
        )
        return

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="📅 ثبت نوبت",
            callback_data=f"appointment:{service_id}"
        )
    )

    price = (
        f"{service['price']:,} تومان"
        if service["price"]
        else "تماس بگیرید"
    )

    text = (
        f"💉 {service['name']}\n\n"
        f"{service['description']}\n\n"
        f"💰 قیمت: {price}"
    )

    await callback.message.reply(
        text,
        components=keyboard
    )