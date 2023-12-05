import asyncio
from datetime import date
from logging import info
from typing import List, Union

import uvicorn
from fastapi import FastAPI

from wakeonlan import send_magic_packet

#user define
from .app.controller import Pc_List, getAllPc, getPcName, getToday

app = FastAPI()

#48:68:4a:79:a4:3c
version = "0.0.1a"

@app.get("/")
async def read_root() -> object:
    return {"Hello": "Project"}

@app.get("/ping")
async def get_ping() -> str:
    a = getToday()
    return f"{a} -- version: {version}"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/get-pc")
async def get_pcs() -> object:
    list_pc = await getAllPc()
    print(list_pc)
    return list_pc

@app.post("/get-pc/")
async def wol_pc(pc_name: Pc_List) -> str:
    mac_add = await getPcName(pc_name.pc_name)
    send_magic_packet(mac_add)
    return f"PC Name: {pc_name} is turned on"

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=5000, log_level="info")
