import asyncio

from REBELBOT.Config import Config
from REBELBOT.utils import admin_cmd, sudo_cmd

LOGGER = Config.PLUGIN_CHANNEL
SUDO_WALA = Config.SUDO_USERS


@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await asyncio.wait(
            [e.respond(str(e.text[8:])) for _ in range(int(e.text[6:8]))]
        )
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@bot.on(admin_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(sanskari):
    if not sanskari.text[0].isalpha() and sanskari.text[0] not in ("/", "#", "@", "!"):
        sanskari_msg = sanskari.text
        for _ in range(1, int(sanskari_msg[9:13])):
            await sanskari.respond(str(sanskari.text[13:]))
        await sanskari.delete()
        if LOGGER:
            await sanskari.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@bot.on(admin_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    await e.delete()
    for _ in range(int("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[1])):
        await e.respond(str("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[2]))
        await asyncio.sleep(
            float("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[0])
        )
