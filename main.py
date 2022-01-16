from dotenv import load_dotenv
import alembic.config
import logging
import os

from start_bot import start_bot


def main():
    load_dotenv()
    logging_level = os.getenv('LOGGING_LEVEL')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging_level)

    alembicArgs = [
        'revision', '--autogenerate',
    ]
    alembic.config.main(argv=alembicArgs)

    alembicArgs = [
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)

    start_bot()


if __name__ == "__main__":
    main()
