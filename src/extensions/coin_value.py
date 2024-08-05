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

    @tasks.loop(seconds=30.0)
    async def printer(self):
        for guild in self.bot.guilds:
            coin = self.bot.db.get(f"{guild.id}-coin")

            if coin is None:
                continue

            try:
                coin_data = await self.cg.get_price(ids=coin, vs_currencies="usd")
                if not coin_data.get(coin):
                    raise Exception
            except Exception as e:
                print(e)
                continue

            price = coin_data[coin]['usd']

            await guild.me.edit(nick=f"{coin.title()}: ${price}")


    @hybrid_command()
    async def get_coin_value(self, ctx: Context, coin: str) -> None:
        """ Get the value of a coin"""
        await ctx.defer()
        try:
            coin_data = await self.cg.get_price(ids=coin, vs_currencies="usd")
            if not coin_data.get(coin):
                raise Exception
        except:
            await ctx.send("error!")
            raise
        else:
            await ctx.send(f"{coin.title()} is worth {coin_data[coin]['usd']} USD")

    @hybrid_command()
    async def setcoinvalue(self, ctx: Context, coin: str) -> None:
        """ Set the servers coin value """
        await ctx.defer()
        self.bot.db[f"{ctx.guild.id}-coin"] = coin
        await ctx.send(f"sevrer coin set to: {coin}")

        


async def setup(bot: Bot) -> None:
    await bot.add_cog(CoinValueCog(bot))


async def teardown(bot: Bot) -> None:
    await bot.remove_cog("CoinValueCog")
