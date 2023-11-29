#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9432690
API_HASH = "1be1a9e84468a6cacd002c9d9c25adb1"
BOT_TOKEN = "5428461440:AAEplXJR1qI6HQfNKO8_NudiIV5Re0ts-Rk"
SESSION = "BQCP7nIAJBUsG-3pTRg7KheN1CC5lW0vDqQNZyP8R2N7GSxy7Y5Trtt8Om6KXZe6gQZw75DRZQUfP3qizQSS_dwDDW2kMS5iBKHuKAPjwzP9cKgAMh8FebJxyIPRUZZ8KCQ6OhtVUe-_PIMAPXm7w1tqWbj2fRmsMhJik5Gg2U4RKaZEaHmuhngBg7lnfaaBA80Vtzu-BGqjLKZyIikCkUZ4Ox6TikvlNsj_dqZXxo-Xu9ywCGZ6RJ4o2V4YPy5HWcH8riCYwOVHEBvWZ1Q_IxHxUt8S-AeqVU-GHTclmZu9gz_TFuCCf7ZjL83kRISlk46xspro4cOxzbYTvdUitXaj6pBQDQAAAAAk7XCJAA"
FORCESUB = "letzsave1"
AUTH = 619540617

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
