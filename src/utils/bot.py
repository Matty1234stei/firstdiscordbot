import shelve
from typing import override

from aiocoingecko import AsyncCoinGeckoAPISession
from discord.ext.commands import Bot


class MyBot(Bot):
    db: shelve.Shelf
    cg: AsyncCoinGeckoAPISession

    @override
    async def close(self) -> None:
        await super().close()
        await self.cg.close()


__all__ = ("MyBot",)
