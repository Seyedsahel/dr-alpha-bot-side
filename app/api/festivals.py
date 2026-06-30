import aiohttp

from app.config import Config


async def get_festivals():

    url = f"{Config.BACKEND_URL}/festivals"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                print("festivals fetch error")
                return []

            return await response.json()