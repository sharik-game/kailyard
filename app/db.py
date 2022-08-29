# app/db.py

import databases
import ormar
import sqlalchemy
from typing import Optional

from app.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User_veg(ormar.Model):

    class Meta(BaseMeta):
        tablename = "users_veg"

    id: int = ormar.Integer(primary_key=True) 
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=255,
                                        unique=True,
                                        nullable=False)
    tomatoes: bool = ormar.Boolean(default=False)
    cucumbers: bool = ormar.Boolean(default=False)
    raspberries: bool = ormar.Boolean(default=False)
    strawberries: bool = ormar.Boolean(default=False)
    potatoes: bool = ormar.Boolean(default=False)
    sweet_cherry: bool = ormar.Boolean(default=False)
    plums: bool = ormar.Boolean(default=False)
    cherry: bool = ormar.Boolean(default=False)
    apple_tree: bool = ormar.Boolean(default=False)
    pepper: bool = ormar.Boolean(default=False)
    dill: bool = ormar.Boolean(default=False)
    parsley: bool = ormar.Boolean(default=False)
    watermelon: bool = ormar.Boolean(default=False)
    melon: bool = ormar.Boolean(default=False)

class Advice(ormar.Model):
    class Meta(BaseMeta):
        tablename = "advice_veg"

    id: int = ormar.Integer(primary_key=True)
    veg_name: str = ormar.String(max_length=128, unique=True)
    when_pinch: str = ormar.Text() # когда сажать
    how_feed: str = ormar.Text() # чем кормить
    where_pinch: str = ormar.Text() # где сажать
    how_handle: str = ormar.Text() # чем обрабатывать
    when_feed: str = ormar.Text() # когда кормить
    when_handle: str = ormar.Text() # когда обрабатывать
    when_take: str = ormar.Text() # когда собирать
    common_illness: str = ormar.Text() # распространённые болезни





engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)