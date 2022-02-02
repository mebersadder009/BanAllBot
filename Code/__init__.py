import logging
from os import environ as e

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_KEY = e.get("API_KEY")
API_HASH = e.get("API_HASH")
OWNER_ID = int(e.get("OWNER_ID"))
TOKEN = e.get("TOKEN")

bot = TelegramClient(None, API_KEY, API_HASH)
