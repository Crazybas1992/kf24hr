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

# กำหนด GUILD_IDS
GUILD_IDS = [258360673648508938]

class Kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = os.getenv("TOKEN")
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} is Ready')
        # ลงทะเบียนคำสั่ง Slash กับ guild ที่กำหนด
        try:
            await self.tree.sync(guild=discord.Object(id=GUILD_IDS[0]))
            print(f'Successfully synced commands for guild ID {GUILD_IDS[0]}')
        except Exception as e:
            print(f'Failed to sync commands: {e}')

# ==================== Create Bot Instance ====================

bot = Kafra(owner_id=258557300183138304, case_insensitive=True)

# ==================== Load Cogs ====================
if __name__ == "__main__":
    server_on()  # Call server_on before running the bot
    
    # โหลด Cog ทั้งหมดจากโฟลเดอร์หลัก (ไม่ใช่โฟลเดอร์ย่อย cogs)
    for file in os.listdir('.'):  # ใช้โฟลเดอร์หลัก
        if file.endswith('.py') and file not in ['kafra.py', 'myserver.py']:  # ข้ามไฟล์หลักและไฟล์ server_on
            try:
                bot.load_extension(file[:-3])  # โหลด Cog โดยใช้ชื่อไฟล์ (ตัด .py ออก)
                print(f'Successfully loaded {file}')
            except Exception as e:
                print(f'Failed to load {file}: {e}')

    server_on()
    bot.run(os.getenv('TOKEN'))
