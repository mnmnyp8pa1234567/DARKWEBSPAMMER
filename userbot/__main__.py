import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import REBELversion, bot, bot1, bot2, bot3, bot4
from userbot.utils import load_module
from var import Var

os.system("pip install -U telethon")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
    bot1.disconnect()
    bot2.disconnect()
    bot3.disconnect()
    bot4.disconnect()
else:
    bot.tgbot = None
    bot1.tgbot = None
    bot2.tgbot = None
    bot3.tgbot = None
    bot4.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT ᗪᗩᖇK ᗯᗴᗷ🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡ᗪᗩᖇK ᗯᗴᗷ ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()
        bot1.start()
        bot2.start()
        bot3.start()
        bot4.start()


import glob

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print(
    f"""Hello sir i am !!  VERSION :- 50 YOUR  IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @DARK_WEB_ARMY ."""
)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
    bot1.disconnect()
    bot2.disconnect()
    bot3.disconnect()
    bot4.disconnect()
else:
    bot.run_until_disconnected()
    bot1.run_until_disconnected()
    bot2.run_until_disconnected()
    bot3.run_until_disconnected()
    bot4.run_until_disconnected()
