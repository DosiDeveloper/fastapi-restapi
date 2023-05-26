from utils import get_password_hash
from config.db import conn
from fastapi import APIRouter, Response, status
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

user_routes = APIRouter()

"""
User REST API
"""


@user_routes.get('/users', response_model=list[User], tags=["Users"])
def get_all_users():
    return conn.execute(users.select()).fetchall()


@user_routes.get("/users/{id}", response_model=User, tags=["Users"])
def get_id_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user_routes.post('/users', response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {"username": user.username, "email": user.email}
    new_user["password"] = get_password_hash(user.password)
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user_routes.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user_routes.put('/users/{id}', response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password)
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
