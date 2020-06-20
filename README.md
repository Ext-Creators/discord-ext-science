# science
![package](https://img.shields.io/pypi/v/discord-ext-science.svg)
![versions](https://img.shields.io/pypi/pyversions/discord-ext-science.svg)
![dependencies](https://img.shields.io/librariesio/github/NCPlayz/discord-ext-science.svg)
![license](https://img.shields.io/pypi/l/discord-ext-science.svg)
![cloned](https://img.shields.io/pypi/dm/discord-ext-science.svg)

A simple event logger for [discord.py](https://github.com/Rapptz/discord.py).

> View the Changelog [here](https://github.com/NCPlayz/discord-ext-science/blob/master/CHANGELOG.md)!

## Install

```sh
$ python3 -m pip install -U discord-ext-science
```

## Extras

### [`databases`](https://github.com/encode/databases) package

You may want to manually install [`databases`](https://github.com/encode/databases) with the correct drivers installed.

## Examples

```py
from discord.ext.science import Scientist, EventFlags, Configuration
from discord.ext.science.recorders.databases import DatabasesRecorder
import logging

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)

config = Configuration(
    events=EventFlags.guilds(),
    recorder=DatabasesRecorder("url-to-my-database")
)
client = Scientist(config=config)


client.run('TOKEN')
```
