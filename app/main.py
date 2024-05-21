import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        'best_name': 'Max',
        "item_id": item_id
    }


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
