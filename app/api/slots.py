import aiohttp
from app.config import Config


async def get_slots():

    url = f"{Config.BACKEND_URL}/slots"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                return []

            return await response.json()