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

# สร้างอินสแตนซ์ของบอทพร้อมกับการตั้งค่า shard_count
bot = Kafra(owner_id=258557300183138304, case_insensitive=True, shard_count=NUM_SHARDS)

if __name__ == "__main__":
    # ตรวจสอบว่ามีไดเรกทอรี cogs หรือไม่ ถ้าไม่มีให้สร้างขึ้นใหม่
    cogs_dir = './cogs'
    if not os.path.exists(cogs_dir):
        print("Cogs directory not found, creating one.")
        os.makedirs(cogs_dir)  # สร้างไดเรกทอรี cogs ใหม่
    
    # โหลด Cog ทั้งหมดจากโฟลเดอร์ cogs เพียงครั้งเดียว
    for file in os.listdir(cogs_dir):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    server_on()  # เรียกใช้งาน server_on เพื่อรันเซิร์ฟเวอร์
    bot.run(os.getenv('TOKEN'))  # เรียกใช้งานบอทด้วย Token จาก Environment Variable
