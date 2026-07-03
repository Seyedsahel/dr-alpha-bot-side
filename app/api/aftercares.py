import aiohttp

from app.config import Config


async def get_aftercares():

    url = f"{Config.BACKEND_URL}/aftercares"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                print("aftercares fetch error")
                return []

            return await response.json()


async def get_aftercare(service_id: int):

    url = f"{Config.BACKEND_URL}/aftercares/{service_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                print("aftercare fetch error")
                return None

            return await response.json()