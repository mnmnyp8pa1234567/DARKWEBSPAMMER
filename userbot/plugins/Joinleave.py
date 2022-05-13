from REBELBOT.utils import admin_cmd, sudo_cmd
from telethon.tl import functions

from . import *


@bot.on(admin_cmd(pattern="join (.*)"))
@bot.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully join")
    except Exception as e:
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="leave (.*)"))
@bot.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "leaving")
    try:
        await event.client(functions.channels.LeaveChannelRequest(channel=bc))
        await event.edit("Succesfully left")
    except Exception as e:
        await event.edit(str(e))
