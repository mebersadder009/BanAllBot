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
from Code import bot as Blaze, OWNER_ID


GANDU = []
for x in OWNER_ID: 
    GANDU.append(x)

@Blaze.on(events.NewMessage(pattern="^/ping"))  
async def pingme(e):
    if e.sender_id in GANDU:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm Active🔥\n\n Start Fucking Any Group** \n\n **__ᏢᎾᏁᎶ🏓__ !!** `{ms}` ms")
