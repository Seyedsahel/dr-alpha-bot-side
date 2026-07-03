from bale import Message

from app.api.faqs import get_faqs
from app.keyboards.faqs import faqs_keyboard


async def handle_faq(message: Message):

    if message.text != "❓ سوالات متداول":
        return False

    faqs = await get_faqs()

    if not faqs:
        await message.reply(
            "در حال حاضر سوال متداولی ثبت نشده است."
        )
        return True

    await message.reply(
        "لطفاً یکی از سوالات زیر را انتخاب کنید:",
        components=faqs_keyboard(faqs)
    )

    return True