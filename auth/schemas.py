from typing import Optional
import uuid

from fastapi_users import schemas

# функция для чтения юзера
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True

# функция для создания юзера
class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    role_id: int
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

