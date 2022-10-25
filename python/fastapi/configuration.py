from os import environ
from time import sleep

import peewee
from playhouse.postgres_ext import PostgresqlExtDatabase


class configuration:
    def __init__(self) -> None:
        self.db = PostgresqlExtDatabase(
            environ.get("DB_URL")
            or "postgres://postgres:postgres@localhost:5432/postgres"
        )

    def getDb(self):
        return self.db

    async def dbConfig(self):
        try:
            await self.db.connect()
            print("Connected to database")
        except:
            self.db.close()
            print("Failed to connect to database")
