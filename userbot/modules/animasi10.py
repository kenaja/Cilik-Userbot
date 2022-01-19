from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio
  
  
@register(outgoing=True, pattern='^.joget(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("JOGET.....")
    sleep(1)
    await typew.edit("JOGET DULU OMM!!")
    sleep(1)
    await typew.edit(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿\n"⠀⠀⠀⠀⠀⠀                        
                     "⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀\n"
                     "⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀\n"
                     "⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿\n"
                     "⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛\n")
    
    
    CMD_HELP.update({
    "animasi10":
    "`.joget`\
    \nUsage: liat aja."
})                   
