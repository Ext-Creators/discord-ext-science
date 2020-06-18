import datetime
import json

from databases import Database
import sqlalchemy

from .base import BaseRecorder

metadata = sqlalchemy.MetaData()

events = sqlalchemy.Table(
    'events', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, sqlalchemy.Sequence('events_id_seq'), primary_key=True),
    sqlalchemy.Column('time', sqlalchemy.Time),
    sqlalchemy.Column('name', sqlalchemy.Text),
    sqlalchemy.Column('payload', sqlalchemy.Text),
    sqlalchemy.Column('unknown', sqlalchemy.Boolean),
)


class DatabasesRecorder(BaseRecorder):
    def __init__(self, database_url: str):
        self.db: Database = Database(database_url)
    
    async def start(self):
        await self.db.connect()
    
    async def end(self):
        await self.db.disconnect()
    
    async def save_event(self, name: str, payload: dict, *, unknown=False):
        query = events.insert().values(
            time=datetime.datetime.utcnow(),
            name=name,
            payload=json.dumps(payload),
            unknown=unknown,
        )
        await self.db.execute(query)
