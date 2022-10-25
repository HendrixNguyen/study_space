from http.client import HTTPResponse
from typing import Union
import os

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

from configuration import configuration
from services.Model import RewardModel, UserModel


class server:
    app = FastAPI()

    def __init__(self) -> None:
        self.reload = False
        self.PORT = os.getenv("PORT") or 5000

    @app.get("/ping")
    def ping():
        return PlainTextResponse(status_code=200, content="ping is OK!")

    @app.on_event(event_type="startup")
    async def startup(self):
        print("Starting up")
        await configuration().dbConfig()
        configuration().getDb().create_tables([UserModel, RewardModel])
        if os.getenv("STAGE") == "dev":
            self.reload = True

    @app.on_event(event_type="shutdown")
    def shutdown() -> None:
        print("Shutting server down")
        configuration().getDb().close()

    # app.include_router(router)

    def start(self) -> None:
        uvicorn.run(self.app, host="127.0.0.1", port=int(self.PORT), reload=self.reload)
        print(f"Service is running on port {self.PORT}")


if __name__ == "__main__":
    # os.system('"uvicorn main:app --reload"')
    def start():
        server().start()
