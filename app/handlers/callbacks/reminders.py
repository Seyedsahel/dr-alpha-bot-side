from bale import CallbackQuery

from app.api.services import get_services
from app.handlers.reminders import start_reminder_date_step


async def handle_reminder_callback(callback: CallbackQuery):

    if not callback.data.startswith("reminder_service:"):
        return False
    
    try:
        service_id = int(callback.data.split(":")[1])
    except (ValueError, IndexError):
        await callback.message.reply("⚠️ درخواست نا معتبر است")
        return

    services = await get_services()

    service = next(
        (item for item in services if item["id"] == service_id),
        None
    )

    if not service:
        await callback.message.reply("⚠️ خدمت مورد نظر یافت نشد")
        return

    service_name = service["name"]

    await start_reminder_date_step(
        callback.message,
        service_id,
        service_name
    )

    return True