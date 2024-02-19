from AnnieRobot.core.bot import AnnieBot
from AnnieRobot.core.dir import dirr
from AnnieRobot.core.git import git
from AnnieRobot.core.userbot import Userbot
from AnnieRobot.misc import dbb, heroku, sudo
from AnnieRobot.platforms import *
from .logging import LOGGER
import asyncio
import os
import re
from typing import Union
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from yt_dlp import YoutubeDL
from youtubesearchpython.__future__ import VideosSearch





# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AnnieBot()

# Assistant Client
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
