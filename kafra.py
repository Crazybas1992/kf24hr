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
    # โหลด Cog จากโฟลเดอร์ cogs และโฟลเดอร์ย่อยทั้งหมด
    for root, dirs, files in os.walk('./cogs'):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                cog_path = os.path.relpath(os.path.join(root, file), start='./cogs')
                cog_module = cog_path.replace(os.sep, '.').replace('.py', '')
                bot.load_extension(f'cogs.{cog_module}')

    server_on()
    bot.run(os.getenv('TOKEN'))
