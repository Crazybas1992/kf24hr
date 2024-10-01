import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta, timezone

# กำหนด guild และ channel ที่ต้องการประกาศ
CHANNEL_IDS = {
    258360673648508938: 1246314849869500480,  # กำหนด Guild ID และ Channel ID ที่ถูกต้อง
}

class DailyAnnouncement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_announcement.start()

    @tasks.loop(minutes=1)
    async def daily_announcement(self):
        print("Task loop กำลังทำงาน...")
        now = datetime.now(timezone(timedelta(hours=7)))  # เวลาที่ถูกต้องในไทย
        target_time = now.replace(hour=8, minute=30, second=0, microsecond=0) #UTC 1 = 8 โมงเช้า

        # ข้ามวันพฤหัสบดี
        if now.weekday() == 3:  # 3 = วันพฤหัสบดี
            return

        # ตรวจสอบเวลาเป้าหมายในวันนี้
        if now.hour == 8 and now.minute == 30: 
            print(f"Sending announcement at {now.isoformat()}")
            expiration_date = datetime(2024, 10, 2, 12, 0, tzinfo=timezone(timedelta(hours=7)))  # วันที่และเวลาหมดอายุ
            if now >= expiration_date:
                return  # หากวันที่หมดอายุผ่านไปแล้ว ให้หยุดประกาศ

            # ส่งประกาศไปยังทุก channel ที่กำหนด
            for guild_id, channel_id in CHANNEL_IDS.items():
                guild = self.bot.get_guild(guild_id)
                if guild:
                    print(f"Found guild: {guild.name}")
                    channel = guild.get_channel(channel_id)
                    if channel:
                        print(f"Found channel: {channel.name}")
                        embed = self.create_update_embed()
                        await channel.send("@everyone", embed=embed)
                        print(f"Announcement sent to channel {channel_id} in guild {guild_id}")
                    else:
                        print(f"Channel ID {channel_id} not found in guild {guild_id}")
                else:
                    print(f"Guild ID {guild_id} not found")

    @daily_announcement.before_loop
    async def before_daily_announcement(self):
        await self.bot.wait_until_ready()  # รอให้บอทพร้อมทำงานก่อนเริ่ม loop

    def add_event(self, embed, title, link, end_date):
        """
        ฟังก์ชันสำหรับเพิ่ม event ลงใน embed
        """
        now = datetime.utcnow()
        time_left = end_date - now
        if time_left.total_seconds() > 0:
            description = f"{link}\n⏳``เหลือเวลาของกิจกรรมอีก {time_left.days} วัน {time_left.seconds // 3600} ชั่วโมง``⏳"
        else:
            description = f"❌``กิจกรรมนี้ได้สิ้นสุดลงแล้วเมื่อวันที่ {end_date.strftime('%d %B %Y')}``❌"

        embed.add_field(name=title, value=description, inline=False)

    def create_update_embed(self):
        """
        ฟังก์ชันสร้าง embed ที่ปรับปรุงแล้วซึ่งใช้ฟังก์ชัน add_event เพื่อเพิ่มหัวข้อ Event
        """
        embed = discord.Embed(
            title='📢 __รายการอัปเดตประจำสัปดาห์__ 📢',
            color=0x66FFFF,
            description='[รายการอัปเดต วันที่ 26 กันยายน 2567](https://ro.gnjoy.in.th/patch-update-26-september-2567/)',
        )
        
        embed.add_field(name='✨ __รายการอัปเดต__', value='', inline=False)
        embed.add_field(
            name='๐ Old Card Album Update List',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/old-card-album-update-list-26-sep-2024/?fbclid=IwY2xjawFhtXNleHRuA2FlbQIxMAABHY0gjJO91HFM3F6J7lnCkVhaMT7vRHX8vJPyrs9GA-XPr-z6t4yEqFULEQ_aem_Y4y3RUvZ0-hZRKEidGMbQg)',
            inline=False
        )
        
        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(
            name='✨ __รายการแก้ไข__',
            value=(
                '> ๐ 🛠 แก้ไขรูป Sprite ของไอเท็ม Old Detachment Ring ให้ถูกต้อง\n'
                '> ๐ 🛠 แก้ไขคำอธิบายของไอเท็ม Booster Pack (180,190) ให้ถูกต้อง\n'
            ),
            inline=False
        )
    
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(name='✨ __Event Now!__', value='', inline=False)
        self.add_event(
            embed,
            title="๐ 📜 ROAD TO 4th CLASS กิจกรรมเก็บเลเวลเตรียมความพร้อมสู่คลาสสี่",
            link="EXP UP +150% (ก่อนปิดปรับปรุงเซิร์ฟเวอร์) [Click](https://www.facebook.com/photo?fbid=541902978225100&set=a.266706959078038)",
            end_date=datetime(2024, 10, 3)
        )

        embed.add_field(name="\n", value="", inline=False)


        self.add_event(
            embed,
            title="๐ 📜 Thanksgiving Event",
            link="เทศกาลเก็บเกี่ยว [Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)",
            end_date=datetime(2024, 10, 3)
        )
        
        embed.add_field(name="\n", value="", inline=False)

        self.add_event(
            embed,
            title="๐ 📜 ROS2024 Merchant",
            link="Ragnarok Stars 2024 รายละเอียดกิจกรรมทั้งหมด [Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)",
            end_date=datetime(2024, 11, 28)
        )

        embed.add_field(name="\n", value="", inline=False)

        self.add_event(
            embed,
            title="๐ 📜 BATTLE PASS SEASON V",
            link="Varmundt’s Mansion & Tower of Thanatos [Click](https://ro.gnjoy.in.th/battle-pass-season-v-guide/)",
            end_date=datetime(2024, 10, 17)
        )

        # เพิ่มข้อมูลพื้นฐานอื่นๆ
        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
        embed.add_field(name='Website RO : https://ro.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Website Gnjoy : https://www.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Instagram : https://www.instagram.com/gravitygametech_official/', value='', inline=False)
        
        embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1288706536700645407/461277287_541964994885565_233848135711251112_n.png?ex=66fcc07d&is=66fb6efd&hm=6a770fe49d7114f398b9b0f4ce2787b18ebcf6393ddc03d32cf901b78a3b5188&=&format=webp&quality=lossless&width=1029&height=686')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
