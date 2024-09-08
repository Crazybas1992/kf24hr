# ==================== Import Statements ====================
import discord
import os
from discord.ext import commands
from myserver import server_on

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True  # จำเป็นสำหรับคำสั่ง slash

# กำหนดตัวแปร GUILD_IDS และจำนวน shards
GUILD_IDS = [258360673648508938]
NUM_SHARDS = 2  # เปลี่ยนตามจำนวน shards ที่คุณต้องการ

class Kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} is Ready')
        # Sync คำสั่งกับ Discord
        synced = await self.tree.sync(guild=discord.Object(id=GUILD_IDS[0]))
        print(f'Synced {len(synced)} commands.')

# สร้างอินสแตนซ์ของบอทพร้อมกับการตั้งค่า shard_count
bot = Kafra(owner_id=258557300183138304, case_insensitive=True, shard_count=NUM_SHARDS)

if __name__ == "__main__":
    # โหลด Cogs จากโฟลเดอร์ cogs (สมมุติว่าทั้งหมดอยู่ในที่เดียวกับไฟล์หลัก)
    for file in os.listdir('.'):
        if file.endswith('.py') and file not in ['kafra.py', 'myserver.py']:  # ข้ามไฟล์ myserver.py
            bot.load_extension(f'{file[:-3]}')

    server_on()  # เรียกใช้งาน server_on เพื่อรันเซิร์ฟเวอร์
    bot.run(bot.token)  # เรียกใช้งานบอทด้วย Token จาก Environment Variable
