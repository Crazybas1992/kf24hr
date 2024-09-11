import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta
from kafra import GUILD_IDS

class DailyAnnouncement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_announcement.start()  # เริ่มต้น task loop เมื่อ Cog ถูกโหลด

    @tasks.loop(hours=24)  # Loop ทุก 24 ชั่วโมง
    async def daily_announcement(self):
        now = datetime.now()
        # ตั้งเวลาเป้าหมายที่ต้องการให้ประกาศ เช่น 06:00 น.
        target_time = now.replace(hour=12, minute=0, second=0, microsecond=0)
        if now >= target_time:
            target_time += timedelta(days=1)  # หากเวลาปัจจุบันผ่านเวลาเป้าหมาย ให้เลื่อนไปอีกวันหนึ่ง

        await asyncio.sleep((target_time - now).seconds)  # รอจนถึงเวลาเป้าหมาย

        expiration_date = datetime(2024, 9, 16, 12, 0)  # วันที่และเวลาหมดอายุ
        if now >= expiration_date:
            return  # หากวันที่หมดอายุผ่านไปแล้ว ให้หยุดประกาศ

        for guild_id in GUILD_IDS:
            guild = self.bot.get_guild(guild_id)
            if guild:
                # หาช่องที่ตรงกับชื่อที่ต้องการในแต่ละเซิร์ฟเวอร์
                channel = discord.utils.get(guild.text_channels, name='ประกาศ')  # ใช้ชื่อช่องที่ต้องการ
                if channel:
                    embed = self.create_update_embed()
                    await channel.send("@everyone", embed=embed)

    @daily_announcement.before_loop
    async def before_daily_announcement(self):
        await self.bot.wait_until_ready()  # รอให้บอทพร้อมทำงานก่อนเริ่ม loop

    def create_update_embed(self):
        # สร้าง Embed สำหรับการประกาศ
        embed = discord.Embed(
            title='📢 ประกาศรายวัน 📢',
            color=0x66FFFF,
            description='✨ **EXP UP +150%:Empty:Drop UP +50%**\n'
                        'ระยะเวลา : 9 - 16 กันยายน 2567 (12:00 น.)\n'
                        'อย่าพลาดกิจกรรมนี้เพื่อเพิ่มประสบการณ์และดรอปของคุณ!',
            timestamp=discord.utils.utcnow()
        )
        
        embed.add_field(name='⏳ วันหมดอายุ:', value='16 กันยายน 2567 (12:00 น.)', inline=False)
        
        embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66df5a20&is=66de08a0&hm=adb9030b0b08f30df5be5687d9b51b79107e0e6ce71b4811674e44ae8bc4947d&=&format=webp&quality=lossless&width=960&height=37')  # แทนที่ด้วย URL รูปภาพที่ต้องการ
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png?ex=66df5a43&is=66de08c3&hm=a05418da54a56c998a8050e97a6ab1d3e5960fcf9c8d1f319f8f87c97a595e9e&=&format=webp&quality=lossless&width=686&height=686')  # แทนที่ด้วย URL รูปภาพที่ต้องการ

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
