import logging
import logging.config
import os

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=150,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
                                

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot Restarting.......")


app = Bot()
app.run()
