import aiohttp
import logging
from app.config import Config

logger = logging.getLogger(__name__)


async def get_aftercares():

    url = f"{Config.BACKEND_URL}/aftercares"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                logger.error("aftercares fetch error")
                return []

            return await response.json()


async def get_aftercare(service_id: int):

    url = f"{Config.BACKEND_URL}/aftercares/{service_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                logger.error("aftercare fetch error")
                return None

            return await response.json()