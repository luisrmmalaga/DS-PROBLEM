from cryptography.fernet import Fernet
from fastapi import APIRouter

from config.db import connection
from models.user import users
from schemas.user import User

users_controller = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)


@users_controller.get("/users")
def get_all():
    return connection.execute(users.select()).fetchall()


@users_controller.get("/users/{user}")
def get(user_id: int):
    return connection.execute(users.select().where(users.c.id == user_id)).first()


@users_controller.post("/users")
def create(user: User):
    new_user = {"name": user.name, "email": user.email,
                "password": f.encrypt(user.password.encode("utf-8"))}

    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()


@users_controller.put("/users/{user}")
def update():
    return "/users/user"


@users_controller.delete("/users/{user}")
def delete():
    return "/users"


@users_controller.patch("/users/{user}")
def patch():
    return "/users"
