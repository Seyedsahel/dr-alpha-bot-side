import aiohttp

from app.config import Config


async def create_consultation_api(user_id: int, service: str = None, note: str = None):

    url = f"{Config.BACKEND_URL}/consultations"

    payload = {
        "user_id": user_id,
        "service": service,
        "note": note
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:

            if response.status != 201:
                print("consultation api error:", response.status)
                return None

            return await response.json()