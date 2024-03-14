from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import requests


# Start command handler
@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📢 Channel 📢', url='https://t.me/iPepkornUpdate')
            ],
            [
                InlineKeyboardButton('Help', callback_data='help'),
                InlineKeyboardButton('About', callback_data='about')
            ]
        ]
    )
    await message.reply_text(
        text=script.START_TEXT.format(message.from_user.mention)
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

# Help command handler
@Client.on_message(filters.command("help"))
async def help(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📢 Channel 📢', url='https://t.me/iPepkornUpdate')
            ],
            [
                InlineKeyboardButton('Help', callback_data='help'),
                InlineKeyboardButton('About', callback_data='about')
            ]
        ]
    )
    await message.reply_text(
        text=script.HELP_TEXT.format(message.from_user.mention)
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

# About command handler
@Client.on_message(filters.command("about"))
async def about(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📢 Channel 📢', url='https://t.me/iPepkornUpdate')
            ],
            [
                InlineKeyboardButton('Help', callback_data='help'),
                InlineKeyboardButton('About', callback_data='about')
            ]
        ]
    )
    await message.reply_text(
        text=script.ABOUT_TEXT.format(message.from_user.mention)
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

# Source command handler
@Client.on_message(filters.command("source"))
async def source(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('✅SOURCE✅', url='https://youtu.be/xyW5fe0AkXo')
            ]
        ]
    )
    await message.reply_text(
        text=script.SOURCE_TEXT.format(message.from_user.mention)
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
