import aiohttp
from app.config import Config


async def create_appointment_api(user_id, slot_id, service_id):

    url = f"{Config.BACKEND_URL}/appointments"

    payload = {
        "user_id": user_id,
        "slot_id": slot_id,
        "service_id": service_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            data = await response.json()

            if response.status != 201:
                return None,data.get("error", "خطا در ثبت نوبت")

            return data, None
        
async def get_user_appointments(user_id: int):

    url = f"{Config.BACKEND_URL}/appointments/{user_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                return []

            return await response.json()