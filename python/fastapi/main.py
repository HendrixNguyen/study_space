from typing import Union
import os

from fastapi import FastAPI
import uvicorn

from . import User, Product

app = FastAPI()

PORT = os.environ.get("PORT") or 5000


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/user")
def read_user():
    return User.getUser()


if __name__ == "__main__":
    # os.system('"uvicorn main:app --reload"')
    uvicorn.run(app, host="0.0.0.0", port=PORT, reload=True)
    print(f"Service is running on port {PORT}")
