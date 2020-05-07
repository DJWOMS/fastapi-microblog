from fastapi_users import FastAPIUsers
from user.logic import user_db, auth_backends, SECRET
from user.schemas import User, UserCreate, UserUpdate, UserDB


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
    SECRET,
)
