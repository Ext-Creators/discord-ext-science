import logging
import asyncio

from discord import Client
from discord.gateway import ResumeWebSocket

from .config import Configuration

logger = logging.getLogger(__name__)


class Scientist(Client):
    def __init__(self, *args, **kwargs):
        self.config: Configuration = kwargs.pop('config')
        logger.debug('Initiated Scientist with %s.', self.config)

        self.analyst = self.config.anal_cls(self.config.recorder)
        super().__init__(*args, **kwargs)
    
    def dispatch(self, event, *args, **kwargs):
        self._schedule_event(self.analyst.log, 'science_logging', event, *args, **kwargs)
        super().dispatch(event, *args, **kwargs)
    
    async def start(self, *args, **kwargs):
        await self.config.recorder.start()
        await super().start(*args, **kwargs)
    
    async def close(self):
        await self.config.recorder.end()
        await super().close()
    
    async def _connect(self):
        cls = self.config.gw_cls
        coro = cls.from_client(self, shard_id=self.shard_id)
        self.ws = await asyncio.wait_for(coro, timeout=180.0)
        while True:
            try:
                await self.ws.poll_event()
            except ResumeWebSocket:
                logger.info('Got a request to RESUME the websocket.')
                self.dispatch('disconnect')
                coro = cls.from_client(self, shard_id=self.shard_id, session=self.ws.session_id,
                                                    sequence=self.ws.sequence, resume=True)
                self.ws = await asyncio.wait_for(coro, timeout=180.0)
