from telegram import Update

from BaseBot.Models.User import User
from BaseBot.Utils.SqlalchemySession import start_session_object


def get_user_from_request(update: Update):
    telegram_id = update.effective_user.id
    nickname = update.effective_user.name
    session = start_session_object()
    user = session.query(User).filter(User.telegram_id == telegram_id).first()

    if user is None:
        user = User(telegram_id=telegram_id, nickname=nickname)
        session.add(user)
        session.commit()
    return user

