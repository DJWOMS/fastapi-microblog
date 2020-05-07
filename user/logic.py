from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db import database
from .models import User
from .schemas import UserDB


users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "dhfg67ewtf8wgf6ewgc8y28g8q893hc7808fwh7w4bynw74y7"

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=3600),
]
# jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

# auth_backends.append(jwt_authentication)
