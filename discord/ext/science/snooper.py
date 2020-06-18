import time
import logging

from .recorders.base import BaseRecorder

logger = logging.getLogger(__name__)


class ReadyTimer:
    start_time: float
    end_time: float

    def start(self):
        self.start_time = time.time()
    
    def end(self) -> float:
        self.end_time = time.time()
        return self.end_time - self.start_time


class Analyst:
    ready_timer = ReadyTimer()

    def __init__(self, recorder: BaseRecorder):
        self.recorder = recorder
    
    async def log(self, event_name, *args, **kwargs):
        handler = getattr(self, 'on_{}'.format(event_name), None)
        try:
            payload: dict = args[0]
        except IndexError:
            return
        
        if type(payload) is bytes:
            return # ping
        
        if handler is None:
            return await self.on_unknown_event(event_name, payload)
        
        if type(payload) is dict:
            await self.recorder.save_event(event_name, payload)
        # TODO: serialize dataclass objects
        await handler(*args, **kwargs)
    
    async def on_unknown_event(self, event_name: str, payload: dict):
        if type(payload) is dict:
            await self.recorder.save_event(event_name, payload, unknown=True)

    # TODO: log events

    async def on_socket_response(self, payload: dict):
        handler = getattr(self, 'on_socket_op_{}'.format(payload['op']), None)
        
        if handler:
            await handler(payload)
    
    async def on_socket_op_0(self, payload):
        event_name = payload['t']

        handler = getattr(self, 'on_socket_{}'.format(event_name), None)

        if handler:
            await handler(payload)
    
    async def on_socket_READY(self, payload):
        duration = self.ready_timer.end()
        logger.debug("Received READY event {:,.2f} milliseconds after connection.".format(duration * 1000))
