from bale import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.api.faqs import get_faqs
from app.handlers.consultations import start_consultation_flow


async def handle_faq_callback(callback: CallbackQuery):

    if callback.data == "request_consultation":
        await start_consultation_flow(callback.message)
        return True

    if not callback.data.startswith("faq:"):
        return False

    faq_id = int(callback.data.split(":")[1])

    faqs = await get_faqs()

    faq = next(
        (item for item in faqs if item["id"] == faq_id),
        None
    )

    if faq is None:
        await callback.message.reply(
            "این سوال یافت نشد."
        )
        return True

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            text="📞 درخواست مشاوره",
            callback_data="request_consultation"
        )
    )

    text = (
        f"❓ {faq['question']}\n\n"
        f"{faq['answer']}"
    )

    await callback.message.reply(
        text,
        components=keyboard
    )

    return True