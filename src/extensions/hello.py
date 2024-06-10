from discord.ext.commands import Cog, Bot, hybrid_command, Context

from utils.bot import MyBot


class HelloCog(Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        self.db = bot.db

    @hybrid_command()
    async def helloworld(self, ctx: Context) -> None:
        """Says hi """
        await ctx.send(self.db.get("hello", "hi"))

    @hybrid_command()
    async def sethello(self, ctx: Context, *, message: str) -> None:
        """Sets the hello message"""
        self.db["hello"] = message
        await ctx.send(f"Hello message set to: {message}")


async def setup(bot: Bot) -> None:
    await bot.add_cog(HelloCog(bot))


async def teardown(bot: Bot) -> None:
    await bot.remove_cog("HelloCog")
