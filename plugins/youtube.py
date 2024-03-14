import os
import re
from pytube import YouTube, Playlist
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from progress import format_bytes, humanbytes

VIDEO_REGEX = r'(.*)youtube.com/(.*)[&|?]v=(?P<video>[^&]*)(.*)'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'

@Client.on_message(filters.regex(VIDEO_REGEX))
async def ytdl(client, message):
    url = message.text
    yt = YouTube(url)
    thumb = yt.thumbnail_url
    ythd = yt.streams.get_highest_resolution()
    ytlow = yt.streams.get_by_resolution(resolution='360p')
    ytaudio = yt.streams.filter(only_audio=True).first()
    audio_size = f"{int(format_bytes(ytaudio.filesize)[0]):.2f}{format_bytes(ytaudio.filesize)[1]}"
    hd = f"{int(format_bytes(ythd.filesize)[0]):.2f}{format_bytes(ythd.filesize)[1]}"
    low = f"{int(format_bytes(ytlow.filesize)[0]):.2f}{format_bytes(ytlow.filesize)[1]}"
    
    result_buttons2 = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('🎬720P ' + ' ⭕️ ' + hd, callback_data='high'),
                InlineKeyboardButton('🎬 360p ' + '⭕️ ' + low, callback_data='360p')
            ],
            [
                InlineKeyboardButton('🎧 AUDIO ' + '⭕️ ' + audio_size, callback_data='audio')
            ],
            [
                InlineKeyboardButton('🖼THUMBNAIL🖼', callback_data='thumbnail')
            ]
        ]
    )
    await message.reply_photo(
        photo=thumb,
        caption="🎬 TITLE : " + yt.title + "\n\n📤 UPLOADED : " + yt.author + "\n\n📢 CHANNEL LINK " + f'https://www.youtube.com/channel/{yt.channel_id}',
        reply_markup=result_buttons2,
        quote=True
    )

@Client.on_message(filters.regex(PLAYLIST_REGEX))
async def ytdl_playlist(client, message):
    purl = message.text
    pyt = Playlist(purl)
  
    for video in pyt.videos:
        phd = video.streams.get_highest_resolution()
        
        await client.send_video(
            chat_id=message.chat.id, 
            caption=(f"⭕️ PLAYLIST : " + pyt.title + "\n📥 DOWNLOADED " + "\n✅ JOIN @TELSABOTS"),
            video=phd.download()
        )

