from fastapi import FastAPI
from .core.database import engine, Base

app = FastAPI()

# Создаем все таблицы в базе данных
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}
