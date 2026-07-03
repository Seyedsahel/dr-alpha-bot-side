from bale import CallbackQuery

from app.api.aftercares import get_aftercare


async def handle_aftercare_callback(callback: CallbackQuery):

    if not callback.data.startswith("aftercare:"):
        return False

    service_id = int(callback.data.split(":")[1])

    aftercare = await get_aftercare(service_id)

    if not aftercare:
        await callback.message.reply(
            "متاسفانه اطلاعاتی برای این خدمت ثبت نشده است."
        )
        return True

    text = (
        f"💉 مراقبت‌های بعد از {aftercare['service_name']}\n\n"
        f"{aftercare['content']}"
    )

    await callback.message.reply(text)

    return True