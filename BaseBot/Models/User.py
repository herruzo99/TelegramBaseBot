from sqlalchemy import Column, Integer, String

from BaseBot.Database.SqlalchemyBase.Base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False, unique=True)
    nickname = Column(String)

