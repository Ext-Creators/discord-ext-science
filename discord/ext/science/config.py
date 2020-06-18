import typing
from dataclasses import dataclass

from .flags import EventFlags
from .gateway import BunsenBurner
from .snooper import Analyst
from .recorders.base import BaseRecorder


@dataclass
class Configuration:
    recorder: BaseRecorder
    events: EventFlags = EventFlags.all()
    gw_cls: BunsenBurner = BunsenBurner
    anal_cls: Analyst = Analyst

Config = Configuration
