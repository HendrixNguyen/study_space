from playhouse.postgres_ext import (
    IdentityField,
    CharField,
    TextField,
    JSONField,
    DateTimeField,
    DateTimeTZField,
)
from peewee import Model


from .. import configuration


class UserModel(Model):
    id = IdentityField(primary_key=True)
    userName = CharField()
    email = CharField()
    password = TextField()
    note = JSONField()
    created_at = DateTimeField()
    updated_at = DateTimeTZField("UTC+7")

    class Meta:
        database = configuration.getDb()


class RewardModel(Model):
    id = IdentityField(primary_key=True)
    name = CharField()
    rewardType = CharField()
    note = JSONField()

    class Meta:
        database = configuration.getDb()
