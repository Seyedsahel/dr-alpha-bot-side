import aiohttp

from app.config import Config
import logging

logger = logging.getLogger(__name__)


async def get_festivals():

    url = f"{Config.BACKEND_URL}/festivals"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                logger.error("festivals fetch error")
                return []

            return await response.json()