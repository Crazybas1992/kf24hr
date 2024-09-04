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
    server_on()  # Call server_on before running the bot
    # โหลด Cog ทั้งหมดจากโฟลเดอร์หลัก (ไม่ใช่โฟลเดอร์ย่อย cogs)
    for file in os.listdir('.'):  # ใช้โฟลเดอร์หลัก
        if file.endswith('.py') and file not in ['kafra.py', 'myserver.py']:  # ข้ามไฟล์หลักและไฟล์ server_on
            bot.load_extension(file[:-3])  # โหลด Cog โดยใช้ชื่อไฟล์ (ตัด .py ออก)

    server_on()
    bot.run(os.getenv('TOKEN'))
