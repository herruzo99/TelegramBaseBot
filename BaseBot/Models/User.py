from sqlalchemy import Column, Integer, String

from BaseBot.Models.Model import Model


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False, unique=True)
    nickname = Column(String)

