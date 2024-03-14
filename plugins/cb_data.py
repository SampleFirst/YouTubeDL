import time
from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup
from progress import progress_for_pyrogram

start_time = time.time()

@Client.on_callback_query()
async def cb_data(bot, query):
    message = query.message
    
    if query.data == 'high':
        try:
            await bot.send_video(
                chat_id=message.chat.id,
                video=ythd.download(),
                caption=result_text,
                reply_markup=result_buttons,
                progress=progress_for_pyrogram,
                progress_args=("Upload Starts...", message, start_time)
            )
            await message.delete()
        except:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**😔 1080P QUALITY IS NOT AVAILABLE\n CHOOSE ANY OTHER QUALITIES**"
            )

    elif query.data == '360p':
        try:
            await bot.send_video(
                chat_id=message.chat.id,
                video=ytlow.download(),
                caption=result_text,
                reply_markup=result_buttons,
                progress=progress_for_pyrogram,
                progress_args=("Upload Starts...", message, start_time)
            )
            await message.delete()
        except:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**😔 360P QUALITY IS NOT AVAILABLE \n CHOOSE ANY OTHER QUALITIES**"
            )

    elif query.data == 'audio':
        await bot.send_audio(
            chat_id=message.chat.id,
            audio=f"{str(yt.title)}.mp3",
            caption=result_text,
            duration=yt.length,
            reply_markup=result_buttons,
            progress=progress_for_pyrogram,
            progress_args=("Upload Starts...", message, start_time)
        )
        await message.delete()

    elif query.data == 'thumbnail':
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=thumb,
            caption="Thumbnail set"
        )
        await message.delete()

    elif query.data == "home":
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
        await message.edit_text(
            text=script.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

    elif query.data == "help":
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
        await message.edit_text(
            text=script.HELP_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

    elif query.data == "about":
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
        await message.edit_text(
            text=script.ABOUT_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

    else:
        await message.delete()
