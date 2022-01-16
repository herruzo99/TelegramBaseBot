from functools import wraps

from telegram import ChatAction


def send_action(func, action):
    """Sends action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
        return func(update, context, *args, **kwargs)

    return command_func


def send_typing_action(func):
    return send_action(func, ChatAction.TYPING)
