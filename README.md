# science

A simple event logger for [discord.py](https://github.com/Rapptz/discord.py).

## Install

```sh
$ python3 -m pip install -U discord-ext-science
```

## Extras

### [`databases`](https://github.com/encode/databases) package

You may want to manually install [`databases`](https://github.com/encode/databases) with the correct drivers installed.

## Examples

```py
from science import Scientist, EventFlags, Configuration
from science.recorders.databases import DatabasesRecorder
import logging

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)

config = Configuration(
    events=EventFlags.guilds(),
    recorder=DatabasesRecorder("url-to-my-database")
)
client = Scientist(config=config)


client.run('NzE3MDM0MDE2ODM4MTIzNjYy.XuuC3A.vffXDcn6MPA_WAnZKAbxQo2wLL0')
```
