import aiohttp

from app.config import Config


async def create_reminder_api(user_id: int, service_id: int, procedure_date: str):

    url = f"{Config.BACKEND_URL}/reminders"

    payload = {
        "user_id": user_id,
        "service_id": service_id,
        "procedure_date": procedure_date
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            data = await response.json()

            if response.status != 201:
                return None, data.get("error", "خطا در ثبت یادآوری")

            return data, None


async def get_user_reminders(user_id: int):

    url = f"{Config.BACKEND_URL}/reminders/{user_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                return []

            return await response.json()
        

async def get_due_reminders():

    url = f"{Config.BACKEND_URL}/reminders/due"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                return []

            return await response.json()


async def mark_reminder_sent(reminder_id: int):

    url = f"{Config.BACKEND_URL}/reminders/{reminder_id}/mark-sent"

    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:

            return response.status == 200