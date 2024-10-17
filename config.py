import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28178139"))
API_HASH = getenv("API_HASH", "85172511f45230b7f8bb304f5ed8e6d8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6541753178:AAHuw9cf5CvfBa4yVlPvlDXx675fNqibLoM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lucky:Lucky@atlascluster.f7lck9c.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))

# Chat id of a group for logging bot's activities
LOG_ID = int(getenv("LOG_ID", "-1001963452122"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001963452122"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5247304559"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/R2R3DL2R4D/NEW",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Luckyxupdate")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LuckyXSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "c7ea1cf58c5840378c47bda546329bf8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "f0acdf6d88784a159f2ed6adefd08901")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGt9tsAbo5pg93xYjpYZQt3V0jBiw_4A18S7bmdcSzcuiFi96egm-CyGvKzDQ2wH6losYr0ia8GX92aPAnvMUq7zAoeyNacsxi_BHYRGg7lYcpD0SxtFjYI-HASkU-r1JVBZslCKBJyfIKyuN9IvFvLUs5ZRBxAwyTmxDSPTcya7zo1ydfxNVI1in-O-fYly_irEMLB8UonilnpV1ketPp8h26LgFz-iDJHpTsLB0Y6j9hN6qat4BPkT9z9_I_4SX1FT-iOahJX4pdz7Wxav8frS7ltRyZ2Yo-9JecC_Q8CHIxzp-7mHIUKLPd3NdJEaLvuGs6HoEe1Ag0mMtQN34Ass3txdgAAAAFlP-m7AA")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")
STRING6 = getenv("STRING_SESSION6", "")
STRING7 = getenv("STRING_SESSION7", "")

AMBOT = [
    "💞", "🦋", "🔍", "🧪", "💖", "⚡️", "🔥", "❤️‍🔥", "🎩", "🌈", "🍷", "🥂", "👀", "🥃", "🥤", "🕊️", 
    "💔", "💘", "🎉", "🥀", "🌹", "❣️", "❤️", "🦋", "🪄", "💌", "💗", "💝", "🧨"
]


AMOP = ["нєу {0} ~\n\n ๏ ᴛʜɪs ɪs {1} !\n\n➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.",
        "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫",
        "❖ нᴇʏ, {0} ~\n│❖ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !•─┈─┈─┈─┈─┈─┈─┈─┈─┈─┈─•\n❍ ɪ ᴀᴍ {1}\n│❍ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs\n•─┈─┈─┈─┈─┈─┈─┈─┈─┈─┈─•\n│❖ ɪ ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ\n❖ A powerful stable and cute telegram music and management bot\n•─┈─┈─┈─┈─┈─┈─┈─┈─┈─┈─•",
        "ʙᴀʙʏ {0},\n ᴍʏ ꜱᴇʟꜰ {1} ..\n{1} ꜱʏꜱ ꜱᴛᴀᴛꜱ\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\nᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.",
        "ʜᴇʏ, {0} \nɪ'ᴍ {1},\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n┠ ◆ ᴀʟʟ-ɪɴ-ᴏɴᴇ ʙᴏᴛ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇs.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴍᴜʟᴛɪᴘʟᴇ ʟᴀɴɢᴜᴀɢᴇꜱ.\n┠ ◆ ɪ ᴄᴀɴ ᴍᴜᴛᴇ,ᴜɴᴍᴜᴛᴇ,ʙᴀɴ,ᴜɴʙᴀɴ,ᴋɪᴄᴋ..\n┠ ◆ ꜱᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ \n┠ ◆ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴄʟɪᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ...\n┗━━━━━━━━━━━━━━━━━⧫\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs."
       ]


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://telegra.ph/file/fc8d4ddbe24c9bb6a343a.jpg", "https://telegra.ph/file/49348001fc1835e9645f0.jpg", "https://telegra.ph/file/9c564118eccc12c14d7cb.jpg", "https://telegra.ph/file/ccc04714eb4460b28403f.jpg", "https://telegra.ph/file/2e5949fb2356287c5749c.jpg", "https://telegra.ph/file/28b515bf5fef0b66a6ab6.jpg", "https://telegra.ph/file/28e2a5752fb51bb091793.jpg", "https://telegra.ph/file/576205fd4bb6926c7efee.jpg", "https://telegra.ph/file/8bda94650ffc113aa9367.jpg", "https://telegra.ph/file/7b61375aa5aacac6d183c.jpg", "https://telegra.ph/file/12cce49a2051faaee3fad.jpg", "https://telegra.ph/file/9a40e0fbc3009c9021ec1.jpg", "https://telegra.ph/file/2c7127f1480a53c3d865a.jpg", "https://telegra.ph/file/805c2a0bf604df12f7d45.jpg", "https://telegra.ph/file/0a28461790aea75d66ede.jpg", "https://telegra.ph/file/3c79b002b8835ebb26ecd.jpg", "https://telegra.ph/file/bce8e03082b78613d463c.jpg", "https://telegra.ph/file/53a629a21937e87ea56c0.jpg", "https://telegra.ph/file/7aeb1602b544dbdd53ec6.jpg", "https://telegra.ph/file/1756c3344e81ef8834d8f.jpg"]
PING_IMG_URL = ["https://telegra.ph/file/b571bb57cc280a19b9b65.jpg", "https://telegra.ph/file/8eee775fbdc6d2fd46743.jpg", "https://telegra.ph/file/3155189915e28b648743c.jpg", "https://telegra.ph/file/74e3d1083b8ffb101ebb8.jpg", "https://telegra.ph/file/7d9fef0ad6f4099cdfddf.jpg", "https://telegra.ph/file/5d293065739283d82bdad.jpg", "https://telegra.ph/file/d29023782fe3794caca50.jpg", "https://telegra.ph/file/aace8de5907322ef99d2a.jpg", "https://telegra.ph/file/f02949b52d6d852e2ae05.jpg", "https://telegra.ph/file/18d71c4fbab5ed35eb66b.jpg", "https://telegra.ph/file/233fc5ce8095cb2baaac8.jpg", "https://telegra.ph/file/fad0d5ab13d43f08ab06d.jpg", "https://telegra.ph/file/d6ef73e9441074b4a4fad.jpg", "https://telegra.ph/file/27a3d26391f94c67147c2.jpg", "https://telegra.ph/file/44905865288401f5dac5d.jpg", "https://telegra.ph/file/02201e6f3cb0498be6fc2.jpg", "https://telegra.ph/file/4d48b6d669ab011e5a67a.jpg", "https://telegra.ph/file/9eb344772676bef77f16d.jpg", "https://telegra.ph/file/786d2d34b4a2472d65812.jpg", "https://telegra.ph/file/e61e7e244079033064c54.jpg"]
STATS_IMG_URL = ["https://telegra.ph/file/17aa4fee21d2bbfc9b937.jpg", "https://telegra.ph/file/77a57c7cc96c029c0fc06.jpg", "https://telegra.ph/file/4e290b9c0df60621d0223.jpg", "https://telegra.ph/file/673faa73fca3c66a60d9a.jpg", "https://telegra.ph/file/82b583c6a91631eb4d29f.jpg", "https://telegra.ph/file/81c0c9c55ccf7371eb85d.jpg", "https://telegra.ph/file/96ee4f692684ec8a0b948.jpg", "https://telegra.ph/file/2f9deaf4454d7b06fcef0.jpg", "https://telegra.ph/file/2402242645950cc0cdc7d.jpg", "https://telegra.ph/file/0076dcfb8d3cebabbc703.jpg", "https://telegra.ph/file/d895b4ad588d75d8fdf6c.jpg", "https://telegra.ph/file/eef0504f4f40787c25132.jpg", "https://telegra.ph/file/173f0ea06fc991d8a0438.jpg", "https://telegra.ph/file/1853894d0b30e8fa46fa4.jpg", "https://telegra.ph/file/c8a38a947dec2d025b0c5.jpg", "https://telegra.ph/file/a3561868cecbdce202776.jpg", "https://telegra.ph/file/6bbef1f4d2d6aa1fd2cbf.jpg", "https://telegra.ph/file/e49f9b2eeeccbe56fa698.jpg", "https://telegra.ph/file/4f2f520f9508be3136c85.jpg", "https://telegra.ph/file/be786ad3da93843d1a426.jpg"]
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
