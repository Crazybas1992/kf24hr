import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta

# กำหนด guild และ channel ที่ต้องการประกาศ
CHANNEL_IDS = {
    258360673648508938: 1246314849869500480,  # กำหนด Guild ID และ Channel ID ที่ถูกต้อง
}

class DailyAnnouncement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_announcement.start()  # เริ่มต้น task loop เมื่อ Cog ถูกโหลด

    @tasks.loop(minutes=1)  # Loop ทุก 1 นาที
    async def daily_announcement(self):
        now = datetime.utcnow()
        target_time = now.replace(hour=1, minute=0, second=0, microsecond=0)  # เวลา UTC

        # ข้ามวันพฤหัสบดี
        if now.weekday() == 3:  # 3 = วันพฤหัสบดี
            return

        # ตรวจสอบเวลาเป้าหมายในวันนี้
        if now.hour == 1 and now.minute == 0:  # ตรวจสอบเวลาปัจจุบันเป็นเวลาเป้าหมายหรือไม่
            print(f"Sending announcement at {now.isoformat()}")
            expiration_date = datetime(2024, 9, 25, 18, 0)  # วันที่และเวลาหมดอายุ
            if now >= expiration_date:
                return  # หากวันที่หมดอายุผ่านไปแล้ว ให้หยุดประกาศ

            # ส่งประกาศไปยังทุก channel ที่กำหนด
            for guild_id, channel_id in CHANNEL_IDS.items():
                guild = self.bot.get_guild(guild_id)
                if guild:
                    channel = guild.get_channel(channel_id)
                    if channel:
                        embed = self.create_update_embed()
                        await channel.send("@everyone", embed=embed)
                        print(f"Announcement sent to channel {channel_id} in guild {guild_id}")

    @daily_announcement.before_loop
    async def before_daily_announcement(self):
        await self.bot.wait_until_ready()  # รอให้บอทพร้อมทำงานก่อนเริ่ม loop

    def create_update_embed(self):
        embed = discord.Embed(
            title='📢 รายการอัปเดตประจำสัปดาห์ 📢',
            color=0x66FFFF,
            description='[รายการอัปเดต วันที่ 26 กันยายน 2567](https://ro.gnjoy.in.th/patch-update-26-september-2567/?fbclid=IwY2xjawFhtRxleHRuA2FlbQIxMAABHaUyudRofWlfzNaYqkDLkR04H9PUjHQqPHBQ0c6E94_E3QkVO32vFYXq0A_aem_2ULHWrW53-L_9ytppqkrdg)',
            timestamp=discord.utils.utcnow()
        )
        
        embed.add_field(name='✨ รายการอัปเดต', value='', inline=False)
        embed.add_field(
            name='๐ Old Card Album Update List',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/old-card-album-update-list-26-sep-2024/?fbclid=IwY2xjawFhtXNleHRuA2FlbQIxMAABHY0gjJO91HFM3F6J7lnCkVhaMT7vRHX8vJPyrs9GA-XPr-z6t4yEqFULEQ_aem_Y4y3RUvZ0-hZRKEidGMbQg)',
            inline=False
        )
        
        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(
            name='✨ รายการแก้ไข',
            value=(
                '๐ แก้ไขรูป Sprite ของไอเท็ม Old Detachment Ring ให้ถูกต้อง\n'
                '๐ แก้ไขคำอธิบายของไอเท็ม Booster Pack (180,190) ให้ถูกต้อง\n'
            ),
            inline=False
        )
    
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(name='✨ Event Now!', value='', inline=False)
        embed.add_field(
            name='๐ Thanksgiving Event',
            value='> 5 กันยายน 2567 – 3 ตุลาคม 2567 [Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)',
            inline=False
        )
        embed.add_field(
            name='๐ ROS2024 Merchant',
            value='> 22 สิงหาคม 2567 – 28 พฤศจิกายน 2567[Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)',
            inline=False
        )
        embed.add_field(
            name='๐ BATTLE PASS SEASON V : Varmundt’s Mansion & Tower of Thanatos',
            value='> 18 ก.ค. – 17 ต.ค. 2567[Click](https://ro.gnjoy.in.th/battle-pass-season-v-guide/)',
            inline=False
        )
        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
        embed.add_field(name='Website RO : https://ro.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Website Gnjoy : https://www.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Instagram : https://www.instagram.com/gravitygametech_official/', value='', inline=False)
        
        embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1286202719140315211/460290319_537016578713740_276002939991631983_n.png?ex=66ed0d20&is=66ebbba0&hm=b4242d4f282f4609caaa05d05da63a5ddf9331c4eca86aced77d1f56267aa744&=&format=webp&quality=lossless&width=1050&height=700')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
