# ==================== Import Statements ====================
import discord
import os
from discord.ext import commands
from myserver import server_on

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

GUILD_IDS = [258360673648508938]

class kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = os.getenv("TOKEN")
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

# ==================== Create Bot Instance ====================
bot = kafra(owner_id=258557300183138304, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is Ready')

if __name__ == "__main__":
    cogs_dir = './cogs'
    if not os.path.exists(cogs_dir):
        print("Cogs directory not found, creating one.")
        os.makedirs(cogs_dir)
    
    for file in os.listdir(cogs_dir):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    server_on()
    bot.run(os.getenv('TOKEN'))
