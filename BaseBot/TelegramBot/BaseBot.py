import os
import pytz
from ptbcontrib.postgres_persistence import PostgresPersistence
from telegram import ParseMode
from telegram.ext import Updater, Dispatcher, Defaults, CommandHandler
import logging

from BaseBot.Utils import SqlalchemySession
from BaseBot.TelegramBot.Handles import General as Handles


class BaseBot:
    updater = None

    def boot(self):
        token = os.getenv('TELEGRAM_TOKEN')
        persistency = os.getenv('PERSISTENCE', 'false').lower() in ('true', '1', 't')

        if persistency:
            postgres_persistence = PostgresPersistence(session=SqlalchemySession.start_session())
        else:
            postgres_persistence = None

        defaults = Defaults(parse_mode=ParseMode.HTML, tzinfo=pytz.timezone('Europe/Madrid'))

        self.updater = Updater(token=token, persistence=postgres_persistence, defaults=defaults,
                               use_context=True)  # arbitrary_callback_data=True,
        self.__populate_handles()

    def __populate_handles(self):
        dispatcher: Dispatcher = self.updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', Handles.start))

        dispatcher.add_error_handler(lambda update, callback: logging.error(callback))

    def start(self):
        self.updater.start_polling()

    def run(self):
        self.boot()
        self.start()


