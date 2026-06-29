import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BACKEND_URL = os.getenv("BACKEND_URL")

    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")