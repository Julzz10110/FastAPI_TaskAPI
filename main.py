from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("БД очищена")
    await create_tables()
    print("БД готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)