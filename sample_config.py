import os


class Var((object)):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    STRING_SESSION1 = os.environ.get("STRING_SESSION1", None)
    STRING_SESSION2 = os.environ.get("STRING_SESSION2", None)
    STRING_SESSION3 = os.environ.get("STRING_SESSION3", None)
    STRING_SESSION4 = os.environ.get("STRING_SESSION4", None)
    DB_URI = os.environ.get("DATABASE_URL", False)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", False)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", False)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", False)
    # Here for later purposes
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "1602757268 5279200868").split()}

    WHITELIST_USERS = {int(x) for x in os.environ.get("WHITELIST_USERS", "").split()}

    BLACKLIST_USERS = {int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()}

    DEVLOPERS = {int(x) for x in os.environ.get("DEVLOPERS", "").split()}
    OWNER_ID = {int(x) for x in os.environ.get("OWNER_ID", "").split()}
    SUPPORT_USERS = {int(x) for x in os.environ.get("SUPPORT_USERS", "").split()}
    PLUGIN_CHANNEL = int(os.environ.get("REBELBOT_ID", False))
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", False)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", False)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", False)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", "5177092348:AAE8PmjjnLhwnVyD7yCN-CXKq0rD4i82Gu8")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", "DARK_WEB_INLINE_BOT")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", False)
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", False)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", False)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", False)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", False)
    if AUTH_TOKEN_DATA != False:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        with open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w") as t_file:
            t_file.write(AUTH_TOKEN_DATA)
    REBELBOT_ID = os.environ.get("REBELBOT_ID", False)
    if REBELBOT_ID != False:
        try:
            REBELBOT_ID = int(REBELBOT_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )


class Development(Var):
    LOGGER = True
