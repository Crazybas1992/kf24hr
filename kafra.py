# ==================== Import Statements ====================
import discord
import os
import certifi
import ssl
from discord.ext import commands
from myserver import server_on

ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True  # จำเป็นสำหรับคำสั่ง slash

# กำหนดตัวแปร GUILD_IDS
GUILD_IDS = [258360673648508938]

class kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = os.getenv("TOKEN")  # ดึง Token จาก Environment Variable
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

# ==================== Create Bot Instance ====================
bot = kafra(owner_id=258557300183138304, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is Ready')

if __name__ == "__main__":
    # โหลด Cog ทั้งหมดจากโฟลเดอร์ cogs เพียงครั้งเดียว
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

server_on

token = os.getenv('DISCORD_TOKEN')
