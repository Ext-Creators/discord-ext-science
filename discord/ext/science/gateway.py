from discord.gateway import DiscordWebSocket


class BunsenBurner(DiscordWebSocket):
    @classmethod
    async def from_client(cls, client, **kwargs):
        client.analyst.ready_timer.start()
        return await super().from_client(client, **kwargs)
