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


# กำหนดตัวแปร GUILD_IDS และจำนวน shards
GUILD_IDS = [258360673648508938]
NUM_SHARDS = 2  # เปลี่ยนตามจำนวน shards ที่คุณต้องการ

class Kafra(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = data.get("token")
        if not self.token:
            raise ValueError("Token not found in configuration")
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} is Ready')
        # การซิงค์คำสั่ง Slash (หากใช้)
        try:
            await self.tree.sync(guild=discord.Object(id=GUILD_IDS[0]))
        except Exception as e:
            print(f"Error syncing commands: {e}")

# สร้างอินสแตนซ์ของบอทพร้อมกับการตั้งค่า shard_count
bot = Kafra(owner_id=258557300183138304, case_insensitive=True, shard_count=NUM_SHARDS)

if __name__ == "__main__":
    # ตรวจสอบว่ามีไฟล์ cogs หรือไม่
    cog_path = './cogs'
    if not os.path.isdir(cog_path):
        raise FileNotFoundError(f"Cog directory '{cog_path}' not found")

    # โหลด Cogs จากโฟลเดอร์ cogs
    for file in os.listdir(cog_path):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    # เรียกใช้ server_on() หากจำเป็น
    if 'server_on' in globals():
        server_on()

    # รันบอท
    bot.run(bot.token)
