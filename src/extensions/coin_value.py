from discord.ext import tasks
from discord.ext.commands import Cog, Bot, hybrid_command, Context

from utils.bot import MyBot


class CoinValueCog(Cog):

    def __init__(self, bot: MyBot):
        self.bot = bot
        self.cg = bot.cg
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(1)

    @hybrid_command()
    async def get_coin_value(self, ctx: Context, coin: str) -> None:
        """ Get the value of a coin"""
        coin_data = await self.cg.get_price(ids=coin, vs_currencies="usd")
        await ctx.send(f"{coin} is worth {coin_data[coin]['usd']} USD")


async def setup(bot: Bot) -> None:
    await bot.add_cog(CoinValueCog(bot))


async def teardown(bot: Bot) -> None:
    await bot.remove_cog("CoinValueCog")
