from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__

