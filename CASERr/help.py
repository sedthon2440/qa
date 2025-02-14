import asyncio
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from datetime import datetime
from pyrogram import enums
from typing import Union, List, Iterable
from pyrogram import Client as client
from pyrogram.errors import FloodWait
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned


@Client.on_message(filters.command("فحص المساعد", ""), group=5865)
async def userrrrr(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in caes:
    client = await get_userbot(bot_username)
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = client.me
    usere = Meh.mention
    async for dialog in client.get_dialogs():
        type = dialog.chat.type
        if enums.ChatType.PRIVATE == type:
            u += 1
        elif enums.ChatType.BOT == type:
            b += 1
        elif enums.ChatType.GROUP == type:
            g += 1
        elif enums.ChatType.SUPERGROUP == type:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status == enums.ChatMemberStatus.ADMINISTRATOR or user_s.status == enums.ChatMemberStatus.OWNER:
                a_chat += 1
        elif enums.ChatType.CHANNEL == type:
            c += 1
        else:
          print(type)

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ .**
.**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ {} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )

@Client.on_message(filters.command("تغير الاسم الاول", ""), group=58650)
async def changefisrt(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان الاسم الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم \n {es}")
     
@Client.on_message(filters.command("تغير البايو", ""), group=586505)
async def changebio(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان البايو الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو \n {es}")


@Client.on_message(filters.command("تغير اسم المستخدم", ""), group=586502)
async def changeusername(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان اسم المستخدم الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم \n {es}")


@Client.on_message(filters.command(["اضافه صوره"], ""), group=5865067)
async def changephoto(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  user = await get_userbot(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    m = await client.ask(message.chat.id, "قم بإرسال الصوره الجديده الان")
    photo = m.photo
    photo = await client.download_media(photo)
    await user.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح ..**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره \n {es}")

@Client.on_message(filters.command(["ازاله صوره"], ""), group=5865084)
async def changephotos(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
       try:
        user = await get_userbot(bot_username)
        async for photos in user.get_chat_photos("me"):
         await user.delete_profile_photos([p.file_id for p in photos[1:]])
         await message.reply_text("**تم ازاله صوره بنجاح ..**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره \n {es}")


@Client.on_message(filters.command("دعوه المساعد الي الانضمام", ""), group=5865024)
async def joined(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان الرابط")
    name = name.text
    if "https" in name:
     if not "+" in name: 
       name = name.replace("https://t.me/", "")
    client = await get_userbot(bot_username)
    await client.join_chat(name)
    await message.reply_text("**تم انضمام الحساب المساعد بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء الانضمام \n {es}")

@Client.on_message(filters.command(["توجيه عام بالمساعد", "اذاعه عام بالمساعد"], ""), group=58650417)
async def cast5(client: Client, message):
  command = message.command[0]
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   kep = ReplyKeyboardMarkup([["الغاء"], ["عوده لقسم المساعد"], ["رجوع للتحكم الكامل"]], resize_keyboard=True)
   ask = await client.ask(message.chat.id, "قم بإرسال الاذاعه الخاصه بك", reply_markup=kep)
   x = ask.id
   y = message.chat.id
   if ask.text == "الغاء":
     return await ask.reply_text("**تم الالغاء بنجاح ✅**")
   pn = await client.ask(message.chat.id, "هل تريد تثبيت الاذاعه\nارسل « نعم » او « لا »")
   await message.reply_text("**جاري الاذاعه انتظر بعض الوقت ...**")
   text = ask.text
   dn = 0
   fd = 0
   if command == "اذاعه عام بالمساعد":
     user = await get_userbot(bot_username)
     async for i in user.get_dialogs():
         try:
           m = await user.send_message(chat_id=i.chat.id, text=text)
           dn += 1
           if pn.text == "نعم":
                try:
                 await m.pin(disable_notification=False)
                except:
                   continue
         except FloodWait as e:
                    flood_time = int(e.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح ..**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "توجيه عام بالمساعد":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         try:
           m = await client.forward_messages(
               chat_id=i.chat.id,
               from_chat_id=message.chat.username,
               message_ids=int(x),
               )
           dn += 1
           if pn.text == "نعم":
                try:
                 await m.pin(disable_notification=False)
                except:
                   continue
         except FloodWait as e:
                    flood_time = int(e.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح ..**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")

@Client.on_message(filters.command(["حذف"], ""), group=5676417)
async def arejg6574ply(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    chat_id = message.chat.id  
    text = int(message.text.split(None, 1)[1])
    async for h in user.get_chat_history(message.chat.id, limit=text):
        await client.delete_messages(chat_id, h.id)
    await client.send_message(chat_id, f"تم حذف {text} رسالة بنجاح.")     