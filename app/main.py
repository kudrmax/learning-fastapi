import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
