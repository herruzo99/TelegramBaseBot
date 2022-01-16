from telegram import Update
from telegram.ext import CallbackContext

from BaseBot.TelegramBot.Utils import DBFacade
from BaseBot.TelegramBot.Utils.Wraps.MessagesFunctionsWraps import send_typing_action

@send_typing_action
def start(update: Update, context: CallbackContext):
    user = DBFacade.get_user_from_request(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I'm a bot, please talk to me {user.nickname}!")

