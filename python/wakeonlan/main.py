import asyncio
from logging import info
from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()

#48:68:4a:79:a4:3c

@app.get("/")
async def read_root() -> object:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/wakeup/{pc_name}")


async def main(port = 5000) -> None:
    config = uvicorn.Config("main:app", port=port, log_level="info")
    info('Server is Running on', port)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == '__main__':
  asyncio.run(main())
