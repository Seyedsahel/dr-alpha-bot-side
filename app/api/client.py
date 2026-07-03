import aiohttp
from app.config import Config

async def get_or_create_user(chat_id: str, first_name: str, last_name: str = ""):
    
    url = f"{Config.BACKEND_URL}/users"

    payload = {
        "chat_id": str(chat_id),
        "first_name": first_name,
        "last_name": last_name
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            if response.status not in (200, 201):
                print("user api error:", response.status)
                return None

            return await response.json()
        

async def create_appointment_api(user_id: int, slot_id: int, service_id: int, description: str = None):

    url = f"{Config.BACKEND_URL}/appointments"

    payload = {
        "user_id": user_id,
        "slot_id": slot_id,
        "service_id": service_id,
        "description": description
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            if response.status != 201:
                print("appointment api error:", response.status)
                return None

            return await response.json()
        

async def update_user_contact(chat_id: str, first_name: str, last_name: str = "", phone: str = None):

    url = f"{Config.BACKEND_URL}/users"

    payload = {
        "chat_id": str(chat_id),
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            if response.status not in (200, 201):
                print("update user contact error:", response.status)
                return None

            return await response.json()