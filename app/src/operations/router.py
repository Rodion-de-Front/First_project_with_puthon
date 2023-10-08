import time
from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.src.database import get_async_session
from app.src.operations.models import operation
from app.src.operations.shemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


# эндпоинт c хешированием у которого много запросов (данные хранятся 30 секунд)
@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"



class OperationSchema(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str

    class Config:
        orm_mode = True


@router.get("/", response_model=List[OperationSchema])
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    # обработка ошибок
    except Exception:
        raise HTTPException(sratus_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}