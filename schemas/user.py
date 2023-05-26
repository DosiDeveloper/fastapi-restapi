from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    id: Optional[str]
    username: str
    password: str
    email: str | None = None
    disabled: bool | None = False


class UserInDB(User):
    hashed_password: str
