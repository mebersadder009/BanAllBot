import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from . import Config as Var

logging.basicConfig(level=logging.INFO)

print("BlackMagic...Beginnings")

Raichu = TelegramClient('Raichu', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)
