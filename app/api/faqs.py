import aiohttp

from app.config import Config


async def get_faqs():

    url = f"{Config.BACKEND_URL}/faqs"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                print("faqs fetch error")
                return []

            return await response.json()