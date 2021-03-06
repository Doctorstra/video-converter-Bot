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
                              [Button.inline("ā»ļø Menu ā»ļø", data="menu")]
                              ])


@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.edit("ššš„š„šØ! šāāļø\n\nš šš¦ š ššØš°šš«šš®š„ šš¢šššØ ššØš§šÆšš«š­šš« ššØš­ š­š”šš­ š¬š®š©š©šØš«š­š¬ šš§ššØšš¢š§š  | šššš ššØš¦š©š«šš¬š¬ | šššš ššØš¦š©š«šš¬š¬ | ššš§šš¦š | šššššš | šš«š¢š¦ | ššØš§šÆšš« šš¢š„š š­šØ šÆš¢šššØ,šÆš¢šššØ š­šØ šš¢š„š | šš±š­š«ššš­ šÆš¢šššØ šš®šš¢šØ)\n\nšš”š¢š¬ ššØš­ ššš§ šš©š„šØšš šš¢šššØ/šš¢š„š ššØš«š¦šš­ š­šØ ššš„šš š«šš¦ š°š¢š­š” ššššš ššš«š¦šš§šš§š­ šš”š®š¦šš§šš¢š„ šš®š©š©šØš«š­.\n\nšššÆšš„šØš©šš« š @Doctorstra_1\n\nšššš š°š¢š­š” šš² ā¤ļø @Dads_links šš±šŗš¶š».",
                    buttons=[[
                         Button.inline("About šµļø", data="info"),
                         Button.inline("NOTICE š", data="notice")],
                         [
                         Button.inline("SOURCE š", data="source"),
                         Button.inline("Settings ā", data="help")],
                         [
                         Button.url("DEVELOPER š", url=f"{DEV}")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**DADS LINKS VIDEO CONVERTER š„**\n\n{info_text}\n\nMade by ā¤ļø @Dads_links šš±šŗš¶š»',
                    buttons=[[
                         Button.inline("š” Home", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="source"))
async def source(event):
    await event.edit(source_text,
                    buttons=[[
                         Button.url("Source code š", url="https://t.me/Doctorstra_1"),
                         Button.url("Repo šļøāšØļø ", url="https://t.me/Doctorstra_1")],
                         [
                         Button.inline("š” Home", data="menu")]])
                         
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('ššš„š„šØ! šāāļø\n\nš šš¦ š ššØš°šš«šš®š„ šš¢šššØ ššØš§šÆšš«š­šš« ššØš­ š­š”šš­ š¬š®š©š©šØš«š­š¬ šš§ššØšš¢š§š  | šššš ššØš¦š©š«šš¬š¬ | šššš ššØš¦š©š«šš¬š¬ | ššš§šš¦š | šššššš | šš«š¢š¦ | ššØš§šÆšš« šš¢š„š š­šØ šÆš¢šššØ,šÆš¢šššØ š­šØ šš¢š„š | šš±š­š«ššš­ šÆš¢šššØ šš®šš¢šØ)\n\nšš”š¢š¬ ššØš­ ššš§ šš©š„šØšš šš¢šššØ/šš¢š„š ššØš«š¦šš­ š­šØ ššš„šš š«šš¦ š°š¢š­š” ššššš ššš«š¦šš§šš§š­ šš”š®š¦šš§šš¢š„ šš®š©š©šØš«š­.\n\nšššÆšš„šØš©šš« š @Doctorstra_1\n\nšššš š°š¢š­š” šš² ā¤ļø @Dads_links šš±šŗš¶š».',
                    buttons=[[
                         Button.inline("SET THUMB š", data="sett"),
                         Button.inline("DEL THUMB šļø", data='remt')],
                         [
                         Button.inline("Help š¤", data="plugins"),
                         Button.inline("RESTART š", data="restart")],
                         [Button.url("Channel š¢", url="https://t.me/Dads_links_bot")],
                         [
                         Button.inline("š” Home", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[Button.inline("š” Home", data="menu")]])
                   
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
