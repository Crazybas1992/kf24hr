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
            expiration_date = datetime(2024, 9, 18, 18, 0)  # วันที่และเวลาหมดอายุ
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
            description='[รายการอัปเดต วันที่ 12 กันยายน 2567](https://ro.gnjoy.in.th/patch-update-12-sep-2567/)',
            timestamp=discord.utils.utcnow()
        )
        
        embed.add_field(name='✨ รายการอัปเดต', value='', inline=False)
        embed.add_field(
            name='๐ Spend Promotion September 2024',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/spend-promotion-september-2024/)',
            inline=False
        )
        embed.add_field(
            name='๐ Malangdo Costume Limited 7Days!',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/malangdo-costume-limited-7days-12.../)',
            inline=False
        )
        embed.add_field(
            name='๐ Pre Event Class 4',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/pre-class-4-event/)',
            inline=False
        )
        embed.add_field(
            name='๐ Update Costume Enchant Stone Box 23',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/update-enchant-stone-box-23-12.../)',
            inline=False
        )
        embed.add_field(
            name='๐ Map Drop System',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/map-drop-system/)',
            inline=False
        )
        
        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(
            name='✨ รายการแก้ไข',
            value=(
                '๐ แก้ไขให้สามารถใช้ Megaphone กับไอเท็ม Document ได้แล้ว\n'
                '๐ แก้ไขบัคไม่พบรูปภาพของไอเท็ม Illusion Sprint Shoes ขณะยังไม่ได้ใช้ Magnifier\n'
                '๐ แก้ไขให้ไอเท็มดังต่อไปนี้สามารถแลกเปลี่ยนได้\n'
                '> Costume The Winner of ROS 2024\n'
                '> Costume 1st Runner Up of ROS 2024\n'
                '> Costume 2nd Runner Up of ROS 2024\n'
                '> Costume 3rd Runner Up of ROS 2024\n'
            ),
            inline=False
        )
        
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(name='✨ Event Now!', value='', inline=False)
        embed.add_field(
            name='๐ Thanksgiving Event',
            value='5 กันยายน 2567 – 3 ตุลาคม 2567[Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)',
            inline=False
        )
        embed.add_field(
            name='๐ ROS2024 Merchant',
            value='22 สิงหาคม 2567 – 28 พฤศจิกายน 2567[Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)',
            inline=False
        )
        embed.add_field(
            name='๐ BATTLE PASS SEASON V : Varmundt’s Mansion & Tower of Thanatos',
            value='18 ก.ค. – 17 ต.ค. 2567[Click](https://ro.gnjoy.in.th/battle-pass-season-v-guide/)',
            inline=False
        )
        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
        embed.add_field(name='Website RO : https://ro.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Website Gnjoy : https://www.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Instagram : https://www.instagram.com/gravitygametech_official/', value='', inline=False)
        
        embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1283715411183140936/459530795_532360245846040_289969461215777392_n.png')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
