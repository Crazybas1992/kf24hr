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

# โหลดข้อมูลจาก config
with open('config/config.json') as config:
    data = json.load(config)

# กำหนดตัวแปร GUILD_IDS และจำนวน shards
GUILD_IDS = [1119100374842884126]
NUM_SHARDS = 2  # เปลี่ยนตามจำนวน shards ที่คุณต้องการ

def get_shard_id(guild_id):
    """
    ฟังก์ชันในการคำนวณ shard_id สำหรับ guild_id
    """
    return (guild_id >> 22) % NUM_SHARDS

class KafraBeta(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = data["token"]
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} is Ready')

# สร้างอินสแตนซ์ของบอทพร้อมกับการตั้งค่า shard_count
bot = KafraBeta(owner_id=1280916207884832899, case_insensitive=True, shard_count=NUM_SHARDS)

if __name__ == "__main__":
    # โหลด Cogs จากโฟลเดอร์ cogs
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    server_on()
    bot.run(os.getenv('TOKEN'))
