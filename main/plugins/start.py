#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 Doctorstra ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/Doctorstra/VIDEO-converter/blob/public/LICENSE> .

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from ethon.mystarts import vc_menu
from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("♻️ Menu ♻️", data="menu")]
                              ])


@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.edit("𝐇𝐞𝐥𝐥𝐨! 🙋‍♂️\n\n𝐈 𝐚𝐦 𝐀 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐕𝐢𝐝𝐞𝐨 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 𝐁𝐨𝐭 𝐭𝐡𝐚𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐬 𝐄𝐧𝐜𝐨𝐝𝐢𝐧𝐠 | 𝐇𝐄𝐕𝐂 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬 | 𝐅𝐀𝐒𝐓 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬 | 𝐑𝐞𝐧𝐚𝐦𝐞 | 𝐒𝐒𝐇𝐎𝐓𝐒 | 𝐓𝐫𝐢𝐦 | 𝐜𝐨𝐧𝐯𝐞𝐫 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐯𝐢𝐝𝐞𝐨,𝐯𝐢𝐝𝐞𝐨 𝐭𝐨 𝐟𝐢𝐥𝐞 | 𝐞𝐱𝐭𝐫𝐚𝐜𝐭 𝐯𝐢𝐝𝐞𝐨 𝐚𝐮𝐝𝐢𝐨)\n\n𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐂𝐚𝐧 𝐔𝐩𝐥𝐨𝐚𝐝 𝐕𝐢𝐝𝐞𝐨/𝐅𝐢𝐥𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐰𝐢𝐭𝐡 𝐀𝐝𝐝𝐞𝐝 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭.\n\n𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🙎 @Doctorstra_1\n\n𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 𝐛𝐲 ❤️ @Dads_links 𝗔𝗱𝗺𝗶𝗻.",
                    buttons=[[
                         Button.inline("About 🕵️", data="info"),
                         Button.inline("NOTICE 📄", data="notice")],
                         [
                         Button.inline("SOURCE 🛑", data="source"),
                         Button.inline("Settings ⚙", data="help")],
                         [
                         Button.url("DEVELOPER 🙎", url=f"{DEV}")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**DADS LINKS VIDEO CONVERTER 🎥**\n\n{info_text}\n\nMade by ❤️ @Dads_links 𝗔𝗱𝗺𝗶𝗻',
                    buttons=[[
                         Button.inline("🏡 Home", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="source"))
async def source(event):
    await event.edit(source_text,
                    buttons=[[
                         Button.url("Source code 🛑", url="https://t.me/Doctorstra_1"),
                         Button.url("Repo 👁️‍🗨️ ", url="https://t.me/Doctorstra_1")],
                         [
                         Button.inline("🏡 Home", data="menu")]])
                         
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('𝐇𝐞𝐥𝐥𝐨! 🙋‍♂️\n\n𝐈 𝐚𝐦 𝐀 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐕𝐢𝐝𝐞𝐨 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 𝐁𝐨𝐭 𝐭𝐡𝐚𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐬 𝐄𝐧𝐜𝐨𝐝𝐢𝐧𝐠 | 𝐇𝐄𝐕𝐂 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬 | 𝐅𝐀𝐒𝐓 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬 | 𝐑𝐞𝐧𝐚𝐦𝐞 | 𝐒𝐒𝐇𝐎𝐓𝐒 | 𝐓𝐫𝐢𝐦 | 𝐜𝐨𝐧𝐯𝐞𝐫 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐯𝐢𝐝𝐞𝐨,𝐯𝐢𝐝𝐞𝐨 𝐭𝐨 𝐟𝐢𝐥𝐞 | 𝐞𝐱𝐭𝐫𝐚𝐜𝐭 𝐯𝐢𝐝𝐞𝐨 𝐚𝐮𝐝𝐢𝐨)\n\n𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐂𝐚𝐧 𝐔𝐩𝐥𝐨𝐚𝐝 𝐕𝐢𝐝𝐞𝐨/𝐅𝐢𝐥𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐰𝐢𝐭𝐡 𝐀𝐝𝐝𝐞𝐝 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭.\n\n𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🙎 @Doctorstra_1\n\n𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 𝐛𝐲 ❤️ @Dads_links 𝗔𝗱𝗺𝗶𝗻.',
                    buttons=[[
                         Button.inline("SET THUMB 🌆", data="sett"),
                         Button.inline("DEL THUMB 🗑️", data='remt')],
                         [
                         Button.inline("Help 👤", data="plugins"),
                         Button.inline("RESTART 🔄", data="restart")],
                         [Button.url("Channel 📢", url="https://t.me/Dads_links_bot")],
                         [
                         Button.inline("🏡 Home", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[Button.inline("🏡 Home", data="menu")]])
                   
 #-----------------------------------------------------------------------------------------------                            
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await set_thumbnail(event, x.media)
        await xx.delete()
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.delete()
    await rem_thumbnail(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("Only authorized user can restart!")
    result = await heroku_restart()
    if result is None:
        await event.edit("You have not filled `HEROKU_API` and `HEROKU_APP_NAME` vars.")
    elif result is False:
        await event.edit("An error occured!")
    elif result is True:
        await event.edit("Restarting app, wait for a minute.")
