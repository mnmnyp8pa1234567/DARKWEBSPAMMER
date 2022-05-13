import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config((object)):
        LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", False)
        # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        # Send .get_id in any group to fill this value.
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", None)

        # This is required for the plugins involving the file system.
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", False)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", False)
        # This is required for the hash to torrent file functionality to work.
        HASH_TO_TORRENT_API = os.environ.get(
            "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
        )
        # This is required for the @telegraph functionality.
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "REBELBOT")
        # Get a Free API Key from OCR.Space
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", False)
        # Send .get_id in any group with all your administration bots (added)
        G_BAN_LOGGER_GROUP = int(os.environ.get("REBELBOT_ID", None))
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
        MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", False)
        MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", False)
        # Telegram BOT Token from @BotFather
        TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", "5177092348:AAE8PmjjnLhwnVyD7yCN-CXKq0rD4i82Gu8")
        TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", "DARK_WEB_INLINE_BOT")
        # spootifie
        SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", False)
        SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", False)
        SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", False)
        # log
        DUAL_LOG = os.environ.get("DUAL_LOG", False)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = {
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        }

        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", False)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", False)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", False)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", False)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        # pm log
        PM_LOG_GRP_ID = os.environ.get("REBELBOT_ID", None)
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        # heroku
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        # send .get_id in any channel to forward all your NEW PMs to this group
        REBELBOT_ID = os.environ.get("REBELBOT_ID", None)
        if REBELBOT_ID:
            REBELBOT_ID = int(REBELBOT_ID)
        # send .get_id in your private channel to forward all your Private messages

        TAG_LOGGER = os.environ.get("TAG_LOGGER", False)
        if TAG_LOGGER:
            TAG_LOGGER = int(TAG_LOGGER)

        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .helpme command
        BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
        # open load
        OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", False)
        OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", False)
        # number of colums of buttons to be displayed in .help command
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
        )
        # pm massage
        CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", "PLEASE DO NOT SPAM MY DM, I WILL REPLY YOU AFTER COME BACK ONLINE!")
        # emoji to be displayed  in help .help
        EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "💙")
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", None)
        HNDLR = os.environ.get("COMMAND_HAND_LER", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "1602757268 5279200868").split()}
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", False)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", False)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        TEMP_DIR = os.environ.get("TEMP_DIR", False)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", False)
        # Google Chrome Stuff
        CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
        GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
        # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", False)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", False)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", False)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", False)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            with open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w") as t_file:
                t_file.write(AUTH_TOKEN_DATA)
        CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", False)
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", False)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", False)
        # MongoDB
        MONGO_URI = os.environ.get("MONGO_URI", False)
        # alive
        ALIVE_PIC = os.environ.get("ALIVE_PIC", False)
        ALIVE_MSG = os.environ.get("ALIVE_MSG", False)
        HELP_PIC = os.environ.get("HELP_PIC", False)
        BOT_PIC = os.environ.get("BOT_PIC", False)
        PING_PIC = os.environ.get("PING_PIC", False)

        # auto bio
        BIO_MSG = os.environ.get("BIO_MSG", False)
        # Lydia API
        LYDIA_API = os.environ.get("LYDIA_API", False)
        PLUGIN_CHANNEL = int(os.environ.get("REBELBOT_ID", None))
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/TEAMREBELS/REBELBOT"
        )
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        STRING_SESSION1 = os.environ.get("STRING_SESSION1", None)
        STRING_SESSION2 = os.environ.get("STRING_SESSION2", None)
        STRING_SESSION3 = os.environ.get("STRING_SESSION3", None)
        STRING_SESSION4 = os.environ.get("STRING_SESSION4", None)
        SESSION = os.environ.get("SESSION", None)
        BOT_MODE = os.environ.get("BOT_MODE", "ON")
        BOT_TRIGGER = os.environ.get("BOT_TRIGGER", "^/")
        BOTMODE_LOG = int(os.environ.get("BOTMODE_LOG", False))
        FORCE_SUB = os.environ.get("FORCE_SUB", False)
        FORCE_CHANNEL_UN = os.environ.get("FORCE_CHANNEL_UN", False)
        FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
        EXTRA_REBELBOT = os.environ.get("EXTRA_REBELBOT", -1001221881562)
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")

else:

    class Config(object):
        DB_URI = None
