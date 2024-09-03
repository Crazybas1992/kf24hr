# ==================== Import Statements ====================
import discord
import os
import json
from discord.ext import commands

from myserver import server_on

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True  # จำเป็นสำหรับคำสั่ง slash

# โหลดข้อมูลจาก config
with open('config/config.json') as config:
    data = json.load(config)

# กำหนดตัวแปร GUILD_IDS
GUILD_IDS = [258360673648508938]

class kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = data["token"]
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

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