from bale import Message

from app.api.aftercares import get_aftercares
from app.keyboards.aftercares import aftercares_keyboard


async def handle_aftercares(message: Message):

    if message.text != "💉 مراقبت‌های بعد از خدمات":
        return False

    aftercares = await get_aftercares()

    if not aftercares:
        await message.reply(
            "در حال حاضر مطلبی برای مراقبت‌های بعد از خدمات ثبت نشده است."
        )
        return True

    await message.reply(
        "لطفاً خدمت مورد نظر خود را انتخاب کنید:",
        components=aftercares_keyboard(aftercares)
    )

    return True