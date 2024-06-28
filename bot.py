from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
from web import keep_alive


bot = Client(

           "Renamer",

           bot_token=BOT_TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()

if __name__ == "__main__":
    keep_alive()
    app.run()
