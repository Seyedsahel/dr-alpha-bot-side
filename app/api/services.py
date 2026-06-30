import aiohttp

from app.config import Config


async def get_services():

    url = f"{Config.BACKEND_URL}/services"

    


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                print("services fetch error")
                return []

            return await response.json()