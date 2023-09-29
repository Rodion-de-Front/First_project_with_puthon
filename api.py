#uvicorn api:app --reload (команда для запуска FastAPI)


from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from auth.schemas import UserCreate, UserRead
from fastapi_users import fastapi_users, FastAPIUsers
from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title="Traiding app"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

fake_Users = [
   {"id": 1, "role": "admin", "name": "Bob"},
   {"id": 2, "role": "invesetor", "name": "John"},
   {"id": 3, "role": "traider", "name": "Tom", "degree": [
       {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
   ]},
]

#структура данных звания для отображения в FastApi и валидации приходящих данных
class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: str

#структура данных пользователя для отображения в FastApi и валидации приходящих данных
class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = None #или можно указать [] для вывода пустого списка

# получаем текущего юзера
current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"

#эндпоинт для получения списка пользователей
@app.get("/users/{user_id}", response_model=List[User])
#передаём user_id для получения данных этого пользователя в эндпоинт /users
#передаём структуру данных пользователя
def get_user(user_id: int):
    #проходимся по списку пользоватлей, находим и отдаём данные по нужному пользователю
    return [user for user in fake_Users if user.get("id") == user_id]


fake_Trades = [
   {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
   {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]

#эндпоинт для получения списка сделок
@app.get("/trades")
#передаём лимит и начальную цифру с какого номера выводить сделки в эндпоинт /trades
def get_trades(limit: int = 1, offset: int = 0):
    #возвращаем сделки с offset по limit
    return fake_Trades[offset:][:limit]


#эндпоинт для изменение поля имени у пользователя
@app.post("/users/{user_id}")
#передаём user_id и новое имя для смены имени пользователя и возращаем ему ответ в виде его обновлённых данных
def change_name(user_id: int, new_name: str):
    #создаём список с пользователем который хочет сменить имя
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_Users))[0]
    #меняем имя пользователя на то которое передали в функцию
    current_user["name"] = new_name
    #возвращаем ответ в виде обновлённых данных юзера
    return {"status": 200, "data": current_user}


#структура данных пользователя для отображения в FastApi и валидации приходящих данных
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float
    amount: float


#эндпоинт для записи новых сделок
@app.post("/trades")
#передаём структуру данных сделок и новые сделки для записи
def add_trades(trades: List[Trade]):
    fake_Trades.extend(trades)
    #возвращаем ответ и обновлённый список сделок
    return {"status": 200, "data": fake_Trades}
