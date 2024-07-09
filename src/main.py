import shelve
from pathlib import Path

from aiocoingecko import AsyncCoinGeckoAPISession
from discord import Intents
from dotenv import dotenv_values

from utils.bot import MyBot

# Load the .env file into the file
config = dotenv_values()

# create the bot
command_prefix = "!"
intents = Intents.default()
bot = MyBot(
    command_prefix=command_prefix,
    intents=intents
)

# Pick a location for our data to be stored
database_path = Path.home() / "firstdiscordbot"
db = shelve.open(str(database_path))

coingecko_api_key = config["COINGECKO_KEY"]
cg = AsyncCoinGeckoAPISession(demo_api_key=coingecko_api_key)


# Add new Commands




# run the bot
discord_token = config["DISCORD_TOKEN"]
guild_id = int(config["GUILD_ID"])


async def setup_hook() -> None:
    """Tell Discord about slash commands """
    await bot.load_extension("extensions.hello")
    await bot.load_extension("extensions.coin_value")
    guild = await bot.fetch_guild(guild_id)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    await cg.start()


bot.setup_hook = setup_hook
bot.db = db
bot.cg = cg

with db:
    bot.run(discord_token)
