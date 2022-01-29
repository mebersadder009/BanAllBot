import logging
from . import bot
from pyrogram import Client, idle
from pyrogram import filters
from Code.helpers.Decorators import authorized_users_only


# Start Bot Command Management

START_TEXT = "𝗧𝗵𝗶𝘀 𝗜𝘀 𝗕𝗮𝗻𝗔𝗹𝗹 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗕𝗼𝘁 𝗢𝗻𝗹𝘆 𝗙𝗼𝗿 𝗧𝗵𝗲 𝗨𝘀𝗲𝗿𝘀 𝗪𝗵𝗼 𝗗𝗮𝗿𝗲 𝗧𝗼 𝗗𝗲𝗽𝗹𝗼𝘆 𝗜𝘁 𝗜𝗻 𝗣𝗹𝗮𝗰𝗲𝘀 𝗔𝗻𝗱 𝗔𝗹𝘀𝗼 𝗜𝗻 𝗧𝗼𝗸𝗲𝗻, 𝗧𝗵𝗶𝘀 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗕𝘆 @TeamRaichu 𝗪𝗶𝘁𝗵 ♥️♥️, 𝗗𝗼𝗻'𝘁 𝗙𝗼𝗿𝗴𝗲𝘁 𝗧𝗼 𝗚𝗶𝘃𝗲 𝘀𝘁𝗮𝗿𝘀 𝗢𝗻 𝗥𝗲𝗽𝗼"
START_BUTTON = [
    [
        InlineKeyboardButton("Gʀᴏᴜᴘ", url="t.me/RaichuOfficial"),
        InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="t.me/RaichuUpdates")
    ], 
    [
        InlineKeyboardButton("Owned By", url="t.me/{own}"),
        InlineKeyboardButton("More Bots", url="t.me/RaichuBots"),
    ], 
    [
        InlineKeyboardButton("Source", url="https://github.com/TeamRaichu/BanAllBot"),
    ]
 ]

@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    text = START_TEXT
    reply_markup = InlineKeyboardMarkup(START_BUTTON)
    message.reply(
    text=text,
    reply_markup=reply_markup,
    disable_web_page_preview=True                        
  )
       
# BanAll  Bot Command Management
@bot.on_message(filters.command("banall") & filters.group)
@authorized_users_only
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            bot.send_message("kicked {} from {}".format(i.user.id,message.chat.id))
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")

bot.run()
idle() 
