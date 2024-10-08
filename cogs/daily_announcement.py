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
            expiration_date = datetime(2024, 10, 9, 12, 0, tzinfo=timezone(timedelta(hours=7)))  # วันที่และเวลาหมดอายุ
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
            description='[รายการอัปเดต วันที่ 3 ตุลาคม 2567](https://ro.gnjoy.in.th/patch-update-3-october-2567/?fbclid=IwY2xjawFrLMRleHRuA2FlbQIxMAABHTS-zELVGa-c3bD0hlw3JHvPpJwgeqoAqi2Ir6t4mpHzuVEXK9tdBG9Z3w_aem_yN9-RWmGb_oKKMKj9Ds5Tw)',
        )
        
        embed.add_field(name='✨ __รายการอัปเดต__', value='', inline=False)
        embed.add_field(
            name='๐ Ragnarok Online x Shiba Says',
            value='> พบกับการเดินทางทั่วโลก RO ไปกับเพื่อนใหม่สามารถดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://ro.gnjoy.in.th/ragnarok-online-x-shibasays-event-guide/?fbclid=IwY2xjawFrqExleHRuA2FlbQIxMAABHTWr1Ttrcnft2oxytmbPDbtW0SAr4_VDhFzYv-wGRi5mF3y41JQn_c0rKQ_aem_uH_RpTdAJQgQOm_Lm4QqFA)',
            inline=False
        )
        embed.add_field(
            name='๐ Shibasays Scroll',
            value='> ไข่ใหม่สามารถดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://ro.gnjoy.in.th/shibasays-scroll/)',
            inline=False
        )
        embed.add_field(
            name='๐ Lapine Box Update! 3 October 2024',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://ro.gnjoy.in.th/lapine-box-update-3-october-2024/?fbclid=IwY2xjawFrqWpleHRuA2FlbQIxMAABHdOkg6Q1-lkT-um0t7wmnl-hqNjFbWttZ4rh-_i36xFryobORWoO3vCkaw_aem_r29WCM5ZbX8PyQuDUhHxeg)',
            inline=False
        )
        embed.add_field(
            name='๐ Daily Login 2.0 October 2024',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://ro.gnjoy.in.th/daily-login-2-0-october-2024/)',
            inline=False
        )
        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(
            name='✨ __รายการแก้ไข__',
            value=(
                '> ๐ 🛠 ในอาทิตย์นี้ไม่มีรายการแก้ไข\n'
            ),
            inline=False
        )
    
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(name='✨ __Event Now!__', value='', inline=False)
        self.add_event(
            embed,
            title="๐ 📜 Ragnarok Online x Shiba Says",
            link="ระยะเวลากิจกรรม 3 – 31 ตุลาคม 2567 (ก่อนปิดปรับปรุงเซิร์ฟเวอร์) [Click](https://ro.gnjoy.in.th/ragnarok-online-x-shibasays-event-guide/?fbclid=IwY2xjawFrql5leHRuA2FlbQIxMAABHTWr1Ttrcnft2oxytmbPDbtW0SAr4_VDhFzYv-wGRi5mF3y41JQn_c0rKQ_aem_uH_RpTdAJQgQOm_Lm4QqFA)",
            end_date=datetime(2024, 10, 31)
        )

        embed.add_field(name="\n", value="", inline=False)

        self.add_event(
            embed,
            title="๐ 📜 Pre 4th Class",
            link="ระยะเวลากิจกรรม : 12 กันยายน 2567 – 16 ตุลาคม 2567 (23:59 น.) [Click](https://ro.gnjoy.in.th/pre-class-4-event/?fbclid=IwY2xjawFpm0xleHRuA2FlbQIxMAABHazpaXIod_b2BvireEhblxkxn59mRbrHhhAF5QbydlIhH0by5RhnPaFeug_aem_1_UAYWi6pw_Jt_eQ38VuQg)",
            end_date=datetime(2024, 10, 16)
        )

        embed.add_field(name="\n", value="", inline=False)
        
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
        
        embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1291369196059623496/461931238_547162507699147_7256492221790226312_n.png?ex=67008188&is=66ff3008&hm=165020644a3a8c3f6565f3c1f1e834960067ea2db8c002a549ad24c93a0ca95f&=&format=webp&quality=lossless&width=960&height=640')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
