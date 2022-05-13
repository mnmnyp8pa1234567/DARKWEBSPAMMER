import sys
from os import execl

from REBELBOT.utils import admin_cmd, sudo_cmd

from userbot import bot, bot1, bot2, bot3, bot4


@bot.on(admin_cmd(pattern="restart$"))
@bot.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="restart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "Restarted. `.ping` me or `.help` to check if I am online, actually it takes 1 min for restarting",
    )
    await bot.disconnect()
    await bot1.disconnect()
    await bot2.disconnect()
    await bot3.disconnect()
    await bot4.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)
