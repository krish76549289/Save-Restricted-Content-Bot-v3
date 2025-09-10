# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "21567814")
API_HASH = os.getenv("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7649708076:AAGMkQpHWeSXFPfs278LORVqk5_9xH0qPlI")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://krishna56478910:KWPaEQfwoHbzan5g@strangerboykrishna.tux94dy.mongodb.net/")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "8167879352").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "stranger_save_bot)
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002583554860")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002583554860")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "1000"))
