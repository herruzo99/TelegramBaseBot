import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session


# SQLAlchemy session maker


def start_session() -> scoped_session:
    db_uri = os.getenv('DB_URI')

    engine = create_engine(db_uri, client_encoding="utf8")
    return scoped_session(sessionmaker(bind=engine))


def start_session_object() -> Session:
    session_factory = start_session()
    return session_factory()

