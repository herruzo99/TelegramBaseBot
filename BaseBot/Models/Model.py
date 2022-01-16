from sqlalchemy import Column, Integer, String

from BaseBot.Database.SqlalchemyBase.Base import Base
from BaseBot.Database.SqlalchemySession import start_session_object


class Model(Base):

    def save(self):
        session = start_session_object()
        session.add(self)
        session.commit()

    def delete(self):
        session = start_session_object()
        session.delete(self)
        session.commit()

