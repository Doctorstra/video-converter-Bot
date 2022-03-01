#TG:Doctorstra_1/Dads_links_bot
#Github.com/Doctorstra

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
                      buttons=[[
                           Button.url("Channel 📢", url="https://t.me/Dads_links"),
                           Button.url("Bot Channel 🤖", url="https://t.me/Dads_links_bot")],
                           [
                           [Button.url("Developer 🙎", url="https://t.me/Doctorstra_1")],
                           [
                           Button.inline("help 🤔", data="plugins")
                           Button.inline("About 🕵️", data="info")],
                           [
                           [Button.inline("Settings ⚙️", data="menu")]
                           ])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await vc_menu(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**About me 😉 :**\n\n{info_text}\n\n⭕ @Dads_links',
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
                         Button.url("Repo 👁️‍🗨️", url="https://t.me/Doctorstra_1")]])
                         
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('{START_TEXT}',
                    buttons=[[
                         Button.inline("SET THUMB 🌆", data="sett"),
                         Button.inline("DEL THUMB 🗑️", data='remt')],
                         [
                         Button.inline("Help 🤔", data="plugins"),
                         Button.inline("RESTART 🔄", data="restart")],
                         [Button.url("Channel 📢", url="https://t.me/Dads_links")],
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
