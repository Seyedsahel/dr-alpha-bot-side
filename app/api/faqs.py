import aiohttp

from app.config import Config
import logging

logger = logging.getLogger(__name__)


async def get_faqs():

    url = f"{Config.BACKEND_URL}/faqs"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                logger.error("faqs fetch error")
                return []

            return await response.json()