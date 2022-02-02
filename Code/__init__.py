import logging
import os

class Config:
    TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
    TELEGRAM_SUDO_ID=int(os.environ['TELEGRAM_SUDO_ID'])
    OWNER_USERNAME=os.environ['OWNER_USERNAME']

    if not BOT_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not API_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set, set it first")

    if not API_ID:
        raise ValueError("TELEGRAM_APP_ID not set, set it first")

    if not SUDO:
        raise ValueError("TELEGRAM_SUDO_ID not set, set it first")

    if not OWNER_USERNAME:
        raise ValueError("OWNER_USERNAME not set, set it first")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("telethon").setLevel(logging.WARNING)
