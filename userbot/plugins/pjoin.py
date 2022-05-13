from REBELBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from . import *


@bot.on(admin_cmd(pattern="pjoin (.*)"))
@bot.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
async def _(e):
    venom = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        bc = venom[0]
        text = "Joining...."
        event = await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await e.client(ImportChatInviteRequest(bc))
            await event.edit("Succesfully Joined")
        except Exception as e:
            await event.edit(str(e))
    else:
        await e.reply(usage, parse_mode=None, link_preview=None)


@bot.on(admin_cmd(pattern="pleave (.*)"))
@bot.on(sudo_cmd(pattern="pleave (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="pleave (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="pleave (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="pleave (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="pleave (.*)", allow_sudo=True))
async def _(e):
    venom = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        bc = venom[0]
        text = "leaving...."
        event = await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await e.client(LeaveChannelRequest(bc))
            await event.edit("Succesfully leave")
        except Exception as e:
            await event.edit(str(e))
    else:
        await e.reply(usage, parse_mode=None, link_preview=None)
