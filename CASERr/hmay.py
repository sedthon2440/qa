import asyncio
import os
import random
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram import enums
from typing import Union, List, Iterable
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram import Client as client
from pyrogram.errors import FloodWait
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned, caserid, photosource
from random import choice
from telegraph import upload_file

loloalbhos = []

alkl = []

@Client.on_message(filters.command(["قفل الحمايه", "تعطيل الحمايه"], ""))
async def lllocj7865j(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status == ChatMemberStatus.OWNER or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in alkl:
            return await message.reply_text("الحمايه معطل من قبل✅")
        alkl.append(message.chat.id)
        return await message.reply_text("تم تعطيل الحمايه بنجاح✅🔒")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح الحمايه", "تفعيل الحمايه"], ""))
async def idljjop546ss(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status == ChatMemberStatus.OWNER or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id not in alkl:
            return await message.reply_text("الحمايه مفعل من قبل✅")
        alkl.remove(message.chat.id)
        return await message.reply_text("تم فتح الحمابه بنجاح✅🔓")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
       
@Client.on_message(filters.command(["فتح الكل", "قفل الكل","الحمايه", "قفل المنشن", "فتح المنشن", "قفل الفديو", "فتح الفديو", "فتح الروابط", "قفل الروابط", "قفل التوجيه", "فتح التوجيه", "قفل الملصقات", "فتح الملصقات", "قفل الصور", "فتح الصور"], ""), group=71328934)
async def gigshkdnnj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in alkl:
      return await message.reply_text(f"عذرا عزيزي [{message.from_user.mention}] الامر معطل من قبل مالك الجروب ✨✅")
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("الـــحــمــايـــه ⚡", callback_data=f"jzhfjgh5")]])
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}" if f"@{message.chat.username}" else "لا يوجود"   
    await message.reply_text(f"الإعــدادات\n\n¦ لمجموعة: {chat_name}\n¦ ايدي المجموعة: -{chat_idd}\n¦ معرف المجموعة: {chat_username}\n\nاضغط علي الحمايه بالاسفل", reply_markup=keybord)
    
@Client.on_callback_query(filters.regex("jzhfjgh5"))
async def h24mgdgbie(client: Client, CallbackQuery):
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    button = [[InlineKeyboardButton(text="قفل الصور ⚡", callback_data=f"stop_photo"), InlineKeyboardButton(text="فتح الصور ⚡", callback_data=f"photoun")],[InlineKeyboardButton(text="قفل الفديو ⚡", callback_data=f"stop_video"), InlineKeyboardButton(text="فتح الفديو ⚡", callback_data=f"viddelet")],[InlineKeyboardButton(text="قفل التوجيه ⚡", callback_data=f"stop_forward"), InlineKeyboardButton(text="فتح التوجيه ⚡", callback_data=f"frwdelet")],[InlineKeyboardButton(text="قفل الروابط ⚡", callback_data=f"stop_link"), InlineKeyboardButton(text="فتح الروابط ⚡", callback_data=f"rwadelet")],[InlineKeyboardButton(text="قفل المنشن ⚡", callback_data=f"stop_mention"), InlineKeyboardButton(text="فتح المنشن ⚡", callback_data=f"mendelet")],[InlineKeyboardButton(text="قفل الملصقات ⚡", callback_data=f"stop_sticker"), InlineKeyboardButton(text="فتح الملصقات ⚡", callback_data=f"moldelet")],[InlineKeyboardButton(text="قفل الكل ⚡", callback_data=f"stop_alkl"), InlineKeyboardButton(text="فتح الكل ⚡", callback_data=f"opn_alkl")]]
    await CallbackQuery.edit_message_text(f" الان تحكم باوامر الحمايه بالاسفل 👇", reply_markup=InlineKeyboardMarkup(button))

###قفل الحمايه
@Client.on_callback_query(filters.regex(pattern=r"^(stop_photo|stop_video|stop_forward|stop_link|stop_mention|stop_sticker|stop_alkl)$"))
async def groupdd655udc(client: Client, CallbackQuery):
    bot_username = client.me.username
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "stop_photo":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"photo_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"photo_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"photo_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))    
    if command == "stop_video":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"video_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"video_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"video_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))    
    if command == "stop_forward":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"forward_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"forward_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"forward_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))    
    if command == "stop_link":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"link_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"link_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"link_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))    
    if command == "stop_mention":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"mention_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"mention_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"mention_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))    
    if command == "stop_sticker":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"sticker_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"sticker_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"sticker_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))        	
    if command == "stop_alkl":
     button = [[InlineKeyboardButton(text="بالكتم", callback_data=f"alkl_unmut1")],[InlineKeyboardButton(text="بالحظر", callback_data=f"alkl_unban1")],[InlineKeyboardButton(text="بمسح الرساله", callback_data=f"alkl_lock")],[InlineKeyboardButton(text="رجوع", callback_data=f"jzhfjgh5")]]
     await CallbackQuery.edit_message_text(f"اختار القيود الان ✨♥", reply_markup=InlineKeyboardMarkup(button))  
     
photo_locked = []
photo_mut = []
photo_ban = []
mention_locked = []
mention_mut = []
mention_ban = []
video_locked = []
video_mut = []
video_ban = []
forward_locked = []
forward_ban = []
forward_mut = []
sticker_locked = []
sticker_ban = []
sticker_mut = []
link_locked = []
link_mut = []
link_ban = []

###فتح الحمايه
@Client.on_callback_query(filters.regex(pattern=r"^(viddelet|photoun|frwdelet|rwadelet|mendelet|moldelet|opn_alkl)$"))
async def groupddu65dc(client: Client, CallbackQuery):
    bot_username = client.me.username
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data=f"jzhfjgh5")]])
    chat_id = CallbackQuery.message.chat.id
    if command == "photoun":
     try: 
      photo_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try: 
      photo_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try: 
      photo_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")     
     await CallbackQuery.edit_message_text(" تم فتح الصور بنجاح ✨♥", reply_markup=keybord)
    if command == "opn_alkl":
     try: 
      photo_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try: 
      photo_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try: 
      photo_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")     
     try: 
      sticker_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")
     try: 
      sticker_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")
     try: 
      sticker_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")     
     try: 
      video_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")
     try: 
      video_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")
     try: 
      video_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")     
     try: 
      forward_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try: 
      forward_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try: 
      forward_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")     
     try: 
      link_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")
     try: 
      link_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")
     try: 
      link_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")     
     try: 
      mention_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try: 
      mention_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try: 
      mention_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")           
     await CallbackQuery.edit_message_text(" تم فتح الكل بنجاح ✨♥", reply_markup=keybord)     
    if command == "viddelet":
     try: 
      video_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")
     try: 
      video_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")
     try: 
      video_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فيد")     
     await CallbackQuery.edit_message_text(" تم فتح الفديو بنجاح ✨♥", reply_markup=keybord)
    if command == "frwdelet":
     try: 
      forward_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try: 
      forward_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try: 
      forward_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")     
     await CallbackQuery.edit_message_text(" تم فتح التوجيه بنجاح ✨♥", reply_markup=keybord)   
    if command == "rwadelet":
     try: 
      link_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")
     try: 
      link_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")
     try: 
      link_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("روابط")     
     await CallbackQuery.edit_message_text(" تم فتح الروابط بنجاح ✨♥", reply_markup=keybord)    	
    if command == "mendelet":
     try: 
      mention_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try: 
      mention_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try: 
      mention_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")     
     await CallbackQuery.edit_message_text(" تم فتح المنشن بنجاح ✨♥", reply_markup=keybord)
    if command == "moldelet":
     try: 
      sticker_locked.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")
     try: 
      sticker_mut.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")
     try: 
      sticker_ban.remove(CallbackQuery.message.chat.id)
     except Exception as e:
      print("ملصقات")     
     await CallbackQuery.edit_message_text(" تم فتح الملصقات بنجاح ✨♥", reply_markup=keybord)

@Client.on_callback_query(filters.regex(pattern=r"^(photo_unmut1|photo_lock|photo_unban1|link_unmut1|link_lock|link_unban1|video_unmut1|video_lock|video_unban1|forward_unmut1|forward_lock|forward_unban1|sticker_unmut1|sticker_lock|sticker_unban1|mention_unmut1|mention_lock|mention_unban1|alkl_unmut1|alkl_lock|alkl_unban1)$"))
async def mearhjc(client: Client, CallbackQuery):
    bot_username = client.me.username
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data=f"jzhfjgh5")]])
    chat_id = CallbackQuery.message.chat.id
    ##الكل
    if command == "alkl_unmut1":
     try:
      photo_mut.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try:      
      video_mut.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فديو")     
     try:      
      mention_mut.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try:     
      forward_mut.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try:   
      link_mut.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("رابط")
     try:   
      sticker_mut.append(CallbackQuery.message.chat.id)    
     except Exception as e:
      print("استيكر") 
     return await CallbackQuery.edit_message_text(" تم قفل الكل بنجاح ✨♥", reply_markup=keybord)
    if command == "alkl_unban1":
     try:
      photo_ban.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try:      
      video_ban.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فديو")     
     try:      
      mention_ban.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try:     
      forward_ban.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try:   
      link_ban.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("رابط")
     try:   
      sticker_ban.append(CallbackQuery.message.chat.id)    
     except Exception as e:
      print("استيكر") 
     return await CallbackQuery.edit_message_text(" تم قفل الكل بنجاح ✨♥", reply_markup=keybord)
    if command == "alkl_lock":
     try:
      photo_locked.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("صور")
     try:      
      video_locked.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("فديو")     
     try:      
      mention_locked.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("منشن")
     try:     
      forward_locked.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("توجيه")
     try:   
      link_locked.append(CallbackQuery.message.chat.id)
     except Exception as e:
      print("رابط")
     try:   
      sticker_locked.append(CallbackQuery.message.chat.id)    
     except Exception as e:
      print("استيكر") 
     return await CallbackQuery.edit_message_text(" تم قفل الكل بنجاح ✨♥", reply_markup=keybord)
    ##الصور
    if command == "photo_unmut1":
     if chat_id in photo_mut:
      return await CallbackQuery.message.reply_text("الصور مقفول بالفعل ✨♥")
     photo_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الصور بنجاح ✨♥", reply_markup=keybord)
    if command == "photo_unban1":
     if chat_id in photo_ban:
      return await CallbackQuery.message.reply_text("الصور مقفول بالفعل ✨♥")
     photo_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الصور بنجاح ✨♥", reply_markup=keybord)
    if command == "photo_lock":
     if chat_id in photo_locked:
      return await CallbackQuery.message.reply_text("الصور مقفول بالفعل ✨♥")
     photo_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الصور بنجاح ✨♥", reply_markup=keybord)
    ##الفديو
    if command == "video_unmut1":
     if chat_id in video_mut:
      return await CallbackQuery.message.reply_text("الفديو مقفول بالفعل ✨♥")
     video_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الفديو بنجاح ✨♥", reply_markup=keybord)
    if command == "video_unban1":
     if chat_id in video_ban:
      return await CallbackQuery.message.reply_text("الفديو مقفول بالفعل ✨♥")
     video_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الفديو بنجاح ✨♥", reply_markup=keybord)
    if command == "video_lock":
     if chat_id in video_locked:
      return await CallbackQuery.message.reply_text("الفديو مقفول بالفعل ✨♥")
     video_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الفديو بنجاح ✨♥", reply_markup=keybord)
    ##المنشن
    if command == "mention_unmut1":
     if chat_id in mention_mut:
      return await CallbackQuery.message.reply_text("المنشن مقفول بالفعل ✨♥")
     mention_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل المنشن بنجاح ✨♥", reply_markup=keybord)
    if command == "mention_unban1":
     if chat_id in mention_ban:
      return await CallbackQuery.message.reply_text("المنشن مقفول بالفعل ✨♥")
     photo_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل المنشن بنجاح ✨♥", reply_markup=keybord)
    if command == "mention_lock":
     if chat_id in mention_locked:
      return await CallbackQuery.message.reply_text("المنشن مقفول بالفعل ✨♥")
     mention_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل المنشن بنجاح ✨♥", reply_markup=keybord)
    ##التوجيه
    if command == "forward_unmut1":
     if chat_id in forward_mut:
      return await CallbackQuery.message.reply_text("التوجيه مقفول بالفعل ✨♥")
     forward_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل التوجيه بنجاح ✨♥", reply_markup=keybord)
    if command == "forward_unban1":
     if chat_id in forward_ban:
      return await CallbackQuery.message.reply_text("التوجيه مقفول بالفعل ✨♥")
     forward_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل التوجيه بنجاح ✨♥", reply_markup=keybord)
    if command == "forward_lock":
     if chat_id in forward_locked:
      return await CallbackQuery.message.reply_text("التوجيه مقفول بالفعل ✨♥")
     forward_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل التوجيه بنجاح ✨♥", reply_markup=keybord)
    ##الروابط
    if command == "link_unmut1":
     if chat_id in link_mut:
      return await CallbackQuery.message.reply_text("الروابط مقفول بالفعل ✨♥")
     link_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الروابط بنجاح ✨♥", reply_markup=keybord)
    if command == "link_unban1":
     if chat_id in link_ban:
      return await CallbackQuery.message.reply_text("الروابط مقفول بالفعل ✨♥")
     link_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الروابط بنجاح ✨♥", reply_markup=keybord)
    if command == "link_lock":
     if chat_id in link_locked:
      return await CallbackQuery.message.reply_text("الروابط مقفول بالفعل ✨♥")
     link_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الروابط بنجاح ✨♥", reply_markup=keybord)
    ##الملصقات
    if command == "sticker_unmut1":
     if chat_id in sticker_mut:
      return await CallbackQuery.message.reply_text("الملصقات مقفول بالفعل ✨♥")
     sticker_mut.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الملصقات بنجاح ✨♥", reply_markup=keybord)
    if command == "sticker_unban1":
     if chat_id in sticker_ban:
      return await CallbackQuery.message.reply_text("الملصقات مقفول بالفعل ✨♥")
     sticker_ban.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الملصقات بنجاح ✨♥", reply_markup=keybord)
    if command == "sticker_lock":
     if chat_id in sticker_locked:
      return await CallbackQuery.message.reply_text("الملصقات مقفول بالفعل ✨♥")
     sticker_locked.append(CallbackQuery.message.chat.id)
     return await CallbackQuery.edit_message_text(" تم قفل الملصقات بنجاح ✨♥", reply_markup=keybord)
     
###الصور
@Client.on_message(filters.photo & filters.create(lambda _, __, message: message.chat.id in photo_mut))
async def deletkse_fgmet55ion(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("صور")

@Client.on_message(filters.photo & filters.create(lambda _, __, message: message.chat.id in photo_ban))
async def deletkse65_65fgon(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("صور")
    except Exception as e:
     print("صور")

@Client.on_message(filters.photo & filters.create(lambda _, __, message: message.chat.id in photo_locked))
async def deletks55e55_fgon(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    print("صور")

###الفديو
@Client.on_message(filters.video & filters.create(lambda _, __, message: message.chat.id in video_mut))
async def deletkse_video(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("فديو")

@Client.on_message(filters.video & filters.create(lambda _, __, message: message.chat.id in video_ban))
async def deletkse_video(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("فيد")
    except Exception as e:
     print("فيد")

@Client.on_message(filters.video & filters.create(lambda _, __, message: message.chat.id in video_locked))
async def deletkse_video(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    print("فيد")

###التوجيه
@Client.on_message(filters.forwarded & filters.create(lambda _, __, message: message.chat.id in forward_mut))
async def deletkse_forward(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("توجيه")

@Client.on_message(filters.forwarded & filters.create(lambda _, __, message: message.chat.id in forward_ban))
async def deletkse_forward(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("توجيه")
    except Exception as e:
     print("توجيه")

@Client.on_message(filters.forwarded & filters.create(lambda _, __, message: message.chat.id in forward_locked))
async def deletkse_forward(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    print("توجيه")

###الملصقات
@Client.on_message(filters.sticker & filters.create(lambda _, __, message: message.chat.id in sticker_mut))
async def deletkse_sticker(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("ملصق")

@Client.on_message(filters.sticker & filters.create(lambda _, __, message: message.chat.id in sticker_ban))
async def deletkse_sticker(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("ملصق")
    except Exception as e:
     print("ملصق")

@Client.on_message(filters.sticker & filters.create(lambda _, __, message: message.chat.id in sticker_locked))
async def deletkse_sticker(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
    await message.delete()
    print("ملصق")
    
###المنشن
@Client.on_message(group=676531)
async def deletkse_mention(client, message):
   if not message.chat.id in mention_mut:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "@" in message.text:
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("@")

@Client.on_message(group=67653167)
async def deletkse_mention(client, message):
   if not message.chat.id in mention_ban:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "@" in message.text:
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("@")
    except Exception as e:
     print("@")

@Client.on_message(group=676531548)
async def deletkse_mention(client, message):
   if not message.chat.id in mention_locked:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "@" in message.text:
    await message.delete()
    print("@")
    
###الروابط
@Client.on_message(group=54534)
async def deletkse_link(client, message):
   if not message.chat.id in link_mut:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "https:" in message.text:
    await message.delete()
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
    else:
      print("رابط")

@Client.on_message(group=5453454)
async def deletkse_link(client, message):
   if not message.chat.id in link_ban:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "https:" in message.text:
    await message.delete()
    try:
     await client.ban_chat_member(message.chat.id, message.from_user.id)
     print("رابط")
    except Exception as e:
     print("رابط")

@Client.on_message(group=5453464245)
async def deletkse_link(client, message):
   if not message.chat.id in link_locked:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "https:" in message.text:
    await message.delete()
    print("رابط")
       
saap_locked = []
     
@Client.on_message(filters.command(["قفل السب"], "") & filters.group, group=573555665565)
async def lllovvmcjj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    for x in get_channel(bot_username):
     ch = x[0]
     keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{ch}")]])
     try:
      await hos.get_chat_member(ch, message.from_user.id)
     except:
      return await message.reply_text(f"🚦عذرا عزيزي {message.from_user.mention} يجب عليك الاشترك في القناة اولا..\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{ch} ⤸", reply_markup=keyboard)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in saap_locked:
          return await message.reply_text("السب مقفول بالفعل ✨♥")
       saap_locked.append(message.chat.id)
       return await message.reply_text(" تم قفل السب بنجاح ✨♥")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
        
@Client.on_message(filters.command(["فتح السب"], "") & filters.group, group=57355566556)
async def idljjojmcbpss(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    for x in get_channel(bot_username):
     ch = x[0]
     keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{ch}")]])
     try:
      await hos.get_chat_member(ch, message.from_user.id)
     except:
      return await message.reply_text(f"🚦عذرا عزيزي {message.from_user.mention} يجب عليك الاشترك في القناة اولا..\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{ch} ⤸", reply_markup=keyboard)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if not message.chat.id in saap_locked:
          return await message.reply_text("السب مفتوح بالفعل ✨♥")
       saap_locked.remove(message.chat.id)
       return await message.reply_text(" تم فتح السب بنجاح ✨♥")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(group=5735545566)
async def deleeon(client, message):
   if not message.chat.id in saap_locked:
      return
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
     return
   if "احا" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "خخخ" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "كسك" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "كسمك" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "عرص" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "خول" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "يبن" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "كلب" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "علق" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "كسم" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "انيك" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "انيكك" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "اركبك" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")
   elif "زبي" in message.text:
       await message.delete()
       await message.reply_text(f"• عذراً عزيزي ↤︎「 {message.from_user.mention}  」\n • تم قفل ارسال السب هنا .")

@Client.on_message(filters.command(["تليجراف", "تليغراف", "ميديا"], ""), group=973) 
async def telegr1aph(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    replied = message.reply_to_message
    if not replied:
        return await message.reply("الرد على ملف وسائط مدعوم ")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 55242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 55242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 55242880)):
        return await message.reply("غير مدعوم !")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton("فتح الرابط 🔗", url=f"https://telegra.ph{response[0]}")]])
        await message.reply(f"**الرابط »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)
       
hmses = {}

@Client.on_message(filters.reply & filters.regex("همسه") & filters.group, group=579)
async def reply_with_link(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{bot_username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("- اضغط لإرسال الهمسه!", url=start_link)]
        ]
    )  
    await message.reply_text("\n╢ إضغط لإرسال همسه!\n", reply_markup=reply_markup)

waiting_for_hms = False

@Client.on_message(filters.command("start"), group=5790)
async def hms_start(client, message): 
  bot_username = client.me.username
  if message.text.split(" ", 1)[-1].startswith("hms"):
    global waiting_for_hms, hms_ids
    hms_ids = message.text
    waiting_for_hms = True
    await message.reply_text(
      "-> أرسل الهمسه الآن.\n√", 
      reply_markup = InlineKeyboardMarkup ([[
        InlineKeyboardButton ("إلغاء ❌️", callback_data="hms_cancel")
      ]])
    )
    return

@Client.on_message(filters.private & filters.text & ~filters.command("start"), group=576)
async def send_hms(client, message): 
  bot_username = client.me.username
  global waiting_for_hms
  if waiting_for_hms:    
    to_id = int(hms_ids.split("to")[-1].split("in")[0])
    from_id = int(hms_ids.split("hms")[-1].split("to")[0])
    in_id = int(hms_ids.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    user = await client.get_users(to_id)
    user_id = user.id
    user_mention = user.mention()  
    hmses[str(to_id)] = { "hms" : message.text, "bar" : in_id }   
    await message.reply_text("-> تم ارسال الهمسه.\n√")
    await client.send_message(chat_id=in_id, text=f"تم استلام همسه جديده ✨♥\nلروئيه الهمسه في الزر بالاسفل ✨♥\nفقط هذا الشخص  [{user_mention}] الي يقدر يشوفها 🔐", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("- اضغط لرؤية الهمسه 🥺", callback_data = "hms_answer")],[InlineKeyboardButton("مستلم الهمسه✨♥", url=f"tg://openmessage?user_id={to_id}")],[InlineKeyboardButton("مرسل الهمسه✨♥", url=f"{from_url}")]]))     
    waiting_for_hms = False
  
@Client.on_callback_query(filters.regex("hms_answer"), group=5766565)
def display_hms(client, callback):  
  bot_username = client.me.username
  in_id = callback.message.chat.id
  who_id = callback.from_user.id  
  if hmses.get(str(who_id)) is not None:
    if hmses.get(str(who_id))["bar"] == in_id:
      callback.answer( hmses.get(str(who_id))["hms"], show_alert = True )
  else:
    callback.answer( "بطل لعب ف حاجه مش بتاعتك يابابا 🗿", show_alert = True )
    
@Client.on_callback_query(filters.regex("hms_cancel"), group=57967)
def cancel_hms(client, callback):  
  bot_username = client.me.username
  global waiting_for_hms
  waiting_for_hms = False  
  client.edit_message_text(
  chat_id = callback.message.chat.id,
  message_id = callback.message.id,
  text = "-> تم إلغاء الهمسه!\n√")    

@Client.on_message(filters.video_chat_members_invited)
async def zoharyy(client, message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass               

@client.on_chat_member_updated(group=713)
async def welc_o_me(client, chat_member_updated):
    bot_username = client.me.username
    chat_id = chat_member_updated.chat.id
    user_id = chat_member_updated.from_user.id
    target_user_id = caserid    
    if user_id == target_user_id:
       try: 
        await client.promote_chat_member(
             chat_id=chat_id,
             user_id=user_id,
             privileges=ChatPrivileges(
                 can_promote_members=True,
                 can_manage_video_chats=True,
                 can_pin_messages=True,
                 can_invite_users=True,
                 can_restrict_members=True,
                 can_delete_messages=True,
                 can_change_info=True
             )
        )     
        await client.set_administrator_title(chat_id, user_id, "مطور السورس")
        await client.send_photo(chat_member_updated.chat.id, photo=photosource, caption=f"**انضم مطور السورس الي هنا\nيرجي من الاعضاء احترامه⚡♥**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"مطور السورس ⚡♥", user_id=f"{user_id}")]]))    
       except Exception as e:
         await client.send_photo(chat_member_updated.chat.id, photo=photosource, caption=f"**انضم مطور السورس الي هنا\nيرجي من الاعضاء احترامه⚡♥**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"مطور السورس ⚡♥", user_id=f"{user_id}")]]))    
         
welcome_enabled = True

@client.on_chat_member_updated()
async def welco57me(client, chat_member_updated):
    bot_username = client.me.username
    if not welcome_enabled:
        return    
    if chat_member_updated.new_chat_member is not None and chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرا لا يمكنني تنزيل الشخص بسبب رتبته"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"        
        await client.send_message(chat_member_updated.chat.id, message)
        
@Client.on_message(filters.command("رفع مشرف", "") & filters.channel)
async def hxh5457(client, message):
  bot_username = client.me.username
  ask = await client.ask(message.chat.id, "ارسل ايدي الان", timeout=300)
  ZOMBIE = ask.text
  chat_id = message.chat.id
  await client.promote_chat_member(
    chat_id=chat_id,
    user_id=ZOMBIE,
    privileges=ChatPrivileges(
    can_promote_members=False,
	can_manage_video_chats=True,
	can_post_messages=True,
	can_invite_users=True,
	can_edit_messages=True,
	can_delete_messages=True,
	can_change_info=False))
  await message.reply("تم رفع العضو مشرف بنجاح")

mannof = []

@Client.on_message(filters.command(["قفل رفع المشرفين", "تعطيل رفع المشرفين"], ""))
async def lllocjj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in mannof:
            return await message.reply_text("رفع المشرفين معطل من قبل✅")
        mannof.append(message.chat.id)
        return await message.reply_text("تم تعطيل رفع المشرفين بنجاح✅🔒")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح رفع المشرفين", "تفعيل رفع المشرفين"], ""))
async def idljjopss(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id not in mannof:
            return await message.reply_text("رفع المشرفين مفعل من قبل✅")
        mannof.remove(message.chat.id)
        return await message.reply_text("تم فتح رفع المشرفين بنجاح✅🔓")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

mangof = []
  
@Client.on_message(filters.command("رفع مشرف", "") & filters.group)
async def tasfaya(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in mannof:
            return await message.reply_text(f"عذرا عزيزي [{message.from_user.mention}] الامر معطل من قبل مالك الجروب ✨✅")
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.first_name
        ask = await client.ask(message.chat.id, "ارسل اللقب الذي تود رفع المشرف به:", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=200)
        CASERA = ask.text
        if not message.reply_to_message and not message.text:
            await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في رفعه")
            return
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            userd = message.reply_to_message.from_user.username
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id 
            userd = user.username 
            user_mention = user.mention()
        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            privileges=ChatPrivileges(
                can_promote_members=False,
                can_manage_video_chats=True,
                can_pin_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_delete_messages=True,
                can_change_info=False
            )
        )
        await client.set_administrator_title(
            chat_id=message.chat.id,
            user_id=user_id,
            title=CASERA
        )
        await message.reply_text(f"• تم رفع العضو {user_mention}\n※ بواسطة {CASER}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
 
@Client.on_message(filters.command(["لقبي"], ""))
async def tit5le(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")

@Client.on_message(filters.command(["لقبه"], ""), group=6465)
async def title(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")
    
@Client.on_message(filters.command(["صلاحياتي"], ""))
async def caesarprivileges(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    chat_id = message.chat.id
    user_id = message.from_user.id
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if status == ChatMemberStatus.OWNER:
        await message.reply_text("أنت مالك الجروب")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("أنت عضو حقير")
    else:
        privileges = cae.privileges if cae else None 
        can_promote_members = "✅" if (privileges and privileges.can_promote_members) else "❌"
        can_manage_video_chats = "✅" if (privileges and privileges.can_manage_video_chats) else "❌"
        can_pin_messages = "✅" if (privileges and privileges.can_pin_messages) else "❌"
        can_invite_users = "✅" if (privileges and privileges.can_invite_users) else "❌"
        can_restrict_members = "✅" if (privileges and privileges.can_restrict_members) else "❌"
        can_delete_messages = "✅" if (privileges and privileges.can_delete_messages) else "❌"
        can_change_info = "✅" if (privileges and privileges.can_change_info) else "❌"
        hossam = f"صلاحياتك في الجروب:\n\n"
        hossam += f"ترقية الأعضاء: {can_promote_members}\n"
        hossam += f"إدارة الدردشات الصوتية: {can_manage_video_chats}\n"
        hossam += f"تثبيت الرسائل: {can_pin_messages}\n"
        hossam += f"دعوة المستخدمين: {can_invite_users}\n"
        hossam += f"تقييد الأعضاء: {can_restrict_members}\n"
        hossam += f"حذف الرسائل: {can_delete_messages}\n"
        hossam += f"تغيير معلومات الجروب: {can_change_info}\n"
        await message.reply_text(hossam)    

@Client.on_message(filters.command(["رتبتي"], ""))
async def rotpty(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    chat_id = message.chat.id
    user_id = message.from_user.id
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if message.from_user.username in caes:
        await message.reply_text("**مطور السورس شخصيا 🫡♥**")
    elif message.from_user.id == OWNER_ID:
        await message.reply_text("**انت مطوري روح قلبي 🥹♥**")
    elif status == ChatMemberStatus.OWNER:
        await message.reply_text("**أنت مالك الخرابه 😂♥**")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("**انت مجرد عضو 🙂**")
    else:
        await message.reply_text(f"**انت مشرف في الجروب 🌚♥**")


unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

muttof = []

@Client.on_message(filters.command(["تنزيل مشرف"], "")) 
async def m54u54te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
     if message.chat.id in muttof:
       return   
     try:	   	
      await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
      await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
     except:
      await message.reply_text(f"لم استطع تنزيله")
     await message.reply_text(f"تم تنزيل المشرف بنجاح ✨♥")
     
@Client.on_message(filters.command(["قفل التقييد", "تعطيل التقييد"], "")) 
async def muttlock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
      if message.chat.id in muttof:
        return await message.reply_text("تم معطل من قبل🔒")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقييد بنجاح ✅🔒")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح التقييد", "تفعيل التقييد"], "")) 
async def muttopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
      if not message.chat.id in muttof:
        return await message.reply_text("التقييد مفعل من قبل ✅")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقييد بنجاح ✅🔓")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
        
        
@Client.on_message(filters.command(["الغاء تقييد","الغاء التقييد"], "")) 
async def mu54te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
     if message.chat.id in muttof:
       return   	   	
     await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
     await message.reply_text(f"✅ ¦ تـم الغاء التقييد بـنجـاح\n {message.reply_to_message.from_user.mention} ")


restricted_users = []

@Client.on_message(filters.command(["تقييد"], ""))
async def m6765ute(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.username in caes:
            await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=mute_permission)
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await message.reply_text(f"✅ ¦ تـم التقييد بـنجـاح\n {restricted_user.mention} ")

@Client.on_message(filters.command(["مسح المقيدين"], ""))
async def unm54ute(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
     global restricted_users
     user_id = message.from_user.id
     count = len(restricted_users)
     for user in restricted_users:
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=user, permissions=unmute_permissions)
        restricted_users.remove(user)
     await message.reply_text(f"↢ تم مسح {count} من المقيديد")
    

@Client.on_message(filters.command(["المقيدين"], "")) 
async def get_restr_users(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
     global restricted_users
     count = len(restricted_users)
     user_ids = [str(user.id) for user in restricted_users]
     response = f"⌔ قائمة المقيدين وعددهم : {count}\n"
     response += "⋖⊶◎⊷⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗤𝗔𝗜𝗗⌯⊶◎⊷⋗\n"
     response += "\n".join(user_ids)
     await message.reply_text(response)       

gaaof = []

@Client.on_message(filters.command(["تعطيل الحظر", "تعطيل الطرد"], "")) 
async def gaalock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
       if message.chat.id in gaaof:
         return await message.reply_text("تم معطل من قبل🔒")
       gaaof.append(message.chat.id)
       return await message.reply_text("تم تعطيل الطرد و الحظر بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر"], "")) 
async def gaaopen(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
      if not message.chat.id in gaaof:
        return await message.reply_text("الطرد و الحظر مفعل من قبل ✅")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح ✅🔓")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
        
banned_users = []
@Client.on_message(filters.command(["حظر", "طرد"], ""), group=9764)
async def mut54575e(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
        return
    if message.chat.id in gaaof:
        return
    if not message.reply_to_message and not message.text:
        await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في حظره")
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        userna = message.reply_to_message.from_user.username
        user_mention = message.reply_to_message.from_user.mention
    else:
        username = message.text.split(" ", 1)[1]
        user = await client.get_users(username)
        user_id = user.id
        userna = user.username
        user_mention = user.mention()
    if userna in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        return
    if user_id == OWNER_ID:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور البوت")
        return
    hhoossam = await client.get_chat_member(message.chat.id, user_id)
    if hhoossam.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply_text("• عذرآ لا يمكنك حظر المشرفين")
        return    
    else:
        banned_users.append(user_id)
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ ¦ تـم الحظر بـنجـاح\n {user_mention} ")

@Client.on_message(filters.command(["مسح المحظورين"], ""), group=9738)
async def unban55_all(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if await johned(client, message):
     return
   group_id = message.chat.id
   chek = await client.get_chat_member(message.chat.id, message.from_user.id)
   if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0
    for member in banned_users.copy():
        if isinstance(member, int):
            user_id = member
        else:
            user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المحظورين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين محظورين ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المحظورين")
        
@Client.on_message(filters.command(["الغاء حظر","/unban"], ""), group=9765)
async def mu65te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id
            user_mention = user.mention()
        await client.unban_chat_member(message.chat.id, user_id) 
        await message.reply_text(f"✅ ¦ تـم الغاء الحظر بـنجـاح\n {user_mention} ")


@Client.on_message(filters.command(["المحظورين"], "")) 
async def get_restricted_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    global banned_users
    count = len(banned_users)
    user_ids = [str(user) for user in banned_users]
    response = f"⌔ قائمة المحظورين وعددهم : {count}\n"
    response += "⋖⊶◎⊷⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗤𝗔𝗜𝗗⌯⊶◎⊷⋗\n"
    response += "\n".join(user_ids)
    await message.reply_text(response)

@Client.on_message(filters.command(["طرد البوتات"], "") & filters.group, group=97365)
async def ban_bots(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"تم طرد {count} بوت بنجاح✅♥")
    else:
        await message.reply_text("لا توجد بوتات لطردها.")
  
@Client.on_message(filters.command(["تليجراف","/telegraph", "/tm", "/tgm"], ""), group=973) 
async def telegraph(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    replied = message.reply_to_message
    if not replied:
        return await message.reply("الرد على ملف وسائط مدعوم ")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 55242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 55242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 55242880)):
        return await message.reply("غير مدعوم !")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton("فتح الرابط 🔗", url=f"https://telegra.ph{response[0]}")]])
        await message.reply(f"**الرابط »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)

@Client.on_message(filters.command(["الغاء تثبيت","غ ث"], ""), group=97365) 
async def unpin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id  
        try:
            await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
            await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")
    else:
        await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["تثبيت", "ث"], ""), group=97354) 
async def pin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id
        try:
            await client.pin_chat_message(chat_id, reply_msg_id)
            await message.reply_text("تم تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")
    else:
        await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

muted_users = {}

@Client.on_message(filters.command(["كتم"], ""))
async def mute_user_from_username(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
    if not message.reply_to_message and not message.text:
        await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في كتمه.")
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        userna = message.reply_to_message.from_user.username
        user_mention = message.reply_to_message.from_user.mention
    else:
        username = message.text.split(" ", 1)[1]
        user = await client.get_users(username)
        user_id = user.id
        userna = user.username
        user_mention = user.mention()
    if userna in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        return
    if user_id == OWNER_ID:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مالك البوت")
        return
    hhoossam = await client.get_chat_member(group_id, user_id)
    if hhoossam.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply_text("• عذرآ لا يمكنك كتم المشرفين.")
        return
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
        await message.reply_text(f"تم كتم العضو {user_mention} بنجاح.", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الغاء الكتم", callback_data=f"unmute{user_id}")]])
        )
    else:
        await message.reply_text("المستخدم مكتوم بالفعل.", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الغاء الكتم", callback_data=f"unmute{user_id}")]])
        )

@Client.on_callback_query(filters.regex(r"unmute(\d+)"), group=97354)
async def unmute_user(client, callback_query):
    global muted_users
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    chat_member = await client.get_chat_member(chat_id, user_id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id != 6264438859:
        return await callback_query.answer("يجب أن تكون مشرفًا لاستخدام هذا الأمر", show_alert=True)
    user_id = int(callback_query.matches[0].group(1))
    if chat_id in muted_users and user_id in muted_users[chat_id]:
        muted_users[chat_id].remove(user_id)
        await callback_query.message.edit_text(f"تم إلغاء  الكتم المستخدم بوساطه: {callback_query.from_user.mention}")
    else:
        await callback_query.message.edit_text("المستخدم غير مكتوم بالفعل.") 
            
@Client.on_message(filters.command(["الغاء الكتم", "الغاء كتم"], ""), group=9735544576)
async def unm64ute_user(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    chat_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if chat_id not in muted_users:
            muted_users[chat_id] = []
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id
            user_mention = user.mention()
        if user_id in muted_users[chat_id]:
            muted_users[chat_id].remove(user_id)
            if user_mention:
                await message.reply_text(f"تم الغاء كتم المستخدم {user_mention}")
        else:
            await message.reply_text("المستخدم غير مكتوم.")

@Client.on_message(group=9736588)
async def handle_message(client, message):
    global muted_users
    chat_id = message.chat.id
    if chat_id in muted_users and message.from_user and message.from_user.id in muted_users[chat_id]:
        await client.delete_messages(chat_id=chat_id, message_ids=message.id)

@Client.on_message(filters.command(["المكتومين"], ""), group=973655)
async def get_rmuted_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    global muted_users
    chat_id = message.chat.id
    if chat_id in muted_users:
        count = len(muted_users[chat_id])
        user_mentions = [str(user) for user in muted_users[chat_id]]
        response = f"⌔ قائمة المكتومين وعددهم : {count}\n"
        response += "⋖⊶◎⊷⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗤𝗔𝗜𝗗⌯⊶◎⊷⋗\n"
        response += "\n".join(user_mentions)
        await message.reply_text(response)
    else:
      await message.reply_text("↢ لا يوجد مستخدمين مكتومين")
      
@Client.on_message(filters.command(["مسح المكتومين"], ""), group=973546)
async def unmute_a54ll(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
     try:    	
       muted_users[message.chat.id].clear()
     except Exception as e:
       print(f"{e}")
     await message.reply_text("تم مسح المكتومين بنجاح ✨♥")