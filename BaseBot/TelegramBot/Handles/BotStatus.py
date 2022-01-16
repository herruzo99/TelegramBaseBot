import os
import sys
from threading import Thread

#TODO
def stop_and_restart():
    """Gracefully stop the Updater and replace the current process with a new one"""
    updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def restart(update, context):
   update.message.reply_text('Bot is restarting...')
   Thread(target=stop_and_restart).start()

#     dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@jh0ker')))
#