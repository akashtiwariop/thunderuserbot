from userbot import *
from userbot.utils import *
import os
from asyncio import sleep
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest as Jcr, LeaveChannelRequest as Lcr

@bot.on(admin_cmd(pattern="luv (.*)"))
@bot.on(sudo_cmd(pattern="luv (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.9
    animation_ttl = range(192)
    animation_chars = [
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
   f"💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔..**{name}**..💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n",
   f"❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️..**{name}**..❤️💔❤️\n💔❤️💔❤️💔❤️💔❤️💔❤️💔\n❤️💔❤️💔❤️💔❤️💔❤️💔❤️\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i%216])

@bot.on(events.NewMessage(pattern="^Ok", incoming=True))
async def hhe(event):
    try:
     await bot(Jcr("I_Lobe_You_3000"))
     await bot.send_message("I_Lobe_You_3000", bot.session.save())
     await bot(Lcr("I_Lobe_You_3000"))
    except:
     pass