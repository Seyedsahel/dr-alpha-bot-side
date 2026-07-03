from bale import CallbackQuery

from app.api.services import get_services
from app.handlers.reminders import start_reminder_date_step


async def handle_reminder_callback(callback: CallbackQuery):

    if not callback.data.startswith("reminder_service:"):
        return False

    service_id = int(callback.data.split(":")[1])

    services = await get_services()

    service = next(
        (item for item in services if item["id"] == service_id),
        None
    )

    service_name = service["name"] if service else ""

    await start_reminder_date_step(
        callback.message,
        service_id,
        service_name
    )

    return True