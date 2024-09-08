# ==================== Import Statements ====================
import discord
import os
from discord.ext import commands
from myserver import server_on

# ตั้งค่า Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

# กำหนด GUILD_IDS
GUILD_IDS = [258360673648508938]  # เพิ่ม guild id ของคุณ

class Kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = os.getenv("TOKEN")
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} is Ready')

        # ลองใช้การ sync คำสั่ง Slash เฉพาะเมื่อจำเป็น
        try:
            synced = await self.tree.sync(guild=discord.Object(id=GUILD_IDS[0]))
            print(f'Successfully synced commands for guild ID {GUILD_IDS[0]}, {len(synced)} commands synced.')
        except discord.HTTPException as e:
            print(f'Failed to sync commands: {e}')

# สร้าง Instance ของ Bot
bot = Kafra(owner_id=258557300183138304, case_insensitive=True)

# โหลด Cogs
if __name__ == "__main__":
    server_on()  # เรียกใช้งาน server_on

    # โหลด Cog จากไฟล์ในโฟลเดอร์หลัก ยกเว้นไฟล์หลักและไฟล์ server_on
    for file in os.listdir('.'):
        if file.endswith('.py') and file not in ['main.py', 'myserver.py']:
            try:
                bot.load_extension(file[:-3])  # โหลด Cog โดยใช้ชื่อไฟล์ (ตัด .py ออก)
                print(f'Successfully loaded {file}')
            except Exception as e:
                print(f'Failed to load {file}: {e}')

    server_on()
    bot.run(os.getenv('TOKEN'))
