from datetime import date

from pydantic import BaseModel

a = {'hendrix': '48:68:4a:79:a4:3c'}

class Pc_List(BaseModel):
  pc_name: str
  descrtions: str

def getToday() -> str:
  return str(date.today())

async def getAllPc() -> object:
  return a

async def getPcName(pc_name: str) -> str:
    if pc_name == '': return "Error Pc ServerName"
    return  str(a.get(pc_name))