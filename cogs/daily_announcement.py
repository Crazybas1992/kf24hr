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
            expiration_date = datetime(2024, 10, 30, 12, 0, tzinfo=timezone(timedelta(hours=7)))  # วันที่และเวลาหมดอายุ
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
            description = f"{link}\n```เหลือเวลาของกิจกรรมอีก {time_left.days} วัน {time_left.seconds // 3600} ชั่วโมง```"
        else:
            description = f"❌``กิจกรรมนี้ได้สิ้นสุดลงแล้วเมื่อวันที่ {end_date.strftime('%d %B %Y')}``"

        embed.add_field(name=title, value=description, inline=False)

    def create_update_embed(self):
        """
        ฟังก์ชันสร้าง embed ที่ปรับปรุงแล้วซึ่งใช้ฟังก์ชัน add_event เพื่อเพิ่มหัวข้อ Event
        """
        embed = discord.Embed(
            title='📢 __รายการอัปเดตประจำสัปดาห์__ 📢',
            color=0x66FFFF,
            description='[รายการอัปเดต วันที่ 24 ตุลาคม 2567](https://ro.gnjoy.in.th/patch-update-24-october-2567/)',
        )
        
        embed.add_field(name='✨ __รายการอัปเดต__', value='', inline=False)
        embed.add_field(
            name='๐ Ragnarok Online X The Ragnarok',
            value='> สามารถดูรายละเอียดเพิ่มเติมได้ [ที่นี่](https://ro.gnjoy.in.th/ragnarok-online-x-the-ragnarok/?fbclid=IwY2xjawGHU7dleHRuA2FlbQIxMAABHYZochtUBTya4wKCRmh1N9uxJuT7Ejf1a3rjmWPl3abayfVWRwWNbo7Skg_aem_5a3lE9PUbunCYRtkRrQm6g)',
            inline=False
        )
        embed.add_field(
            name='๐ Ragnarok Festa Reward',
            value='> NPC Valkyries (กลางเมือง izlude) \n ตำแหน่ง : /navi izlude 130/16 \n เมื่อใช้งาน [Event] 4th Test Pass จะเปลี่ยนอาชีพคลาส 4 ให้กับผู้เล่น',
            inline=False
        )

        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
        
        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)
            
        embed.add_field(
            name='✨ __รายการแก้ไข__',
            value=(
                '> ๐ 🛠 ในอาทิตย์นี้ไม่มีรายการแก้ไข\n'
            ),
            inline=False
        )

        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)

        
        embed.add_field(name="\n", value="\n", inline=False)

        embed.add_field(name='✨ __Event Now!__', value='', inline=False)
        self.add_event(
            embed,
            title="๐ 📜 Ragnarok Online x Shiba Says",
            link="> ⏰ ระยะเวลากิจกรรม 3 – 31 ตุลาคม 2567 \n (ก่อนปิดปรับปรุงเซิร์ฟเวอร์) [Click](https://ro.gnjoy.in.th/ragnarok-online-x-shibasays-event-guide/?fbclid=IwY2xjawFrql5leHRuA2FlbQIxMAABHTWr1Ttrcnft2oxytmbPDbtW0SAr4_VDhFzYv-wGRi5mF3y41JQn_c0rKQ_aem_uH_RpTdAJQgQOm_Lm4QqFA)",
            end_date=datetime(2024, 10, 31)
        )

        embed.add_field(name="\n", value="", inline=False)

        self.add_event(
            embed,
            title="๐ 📜 2024 Halloween Event",
            link="> ⏰ ระยะเวลากิจกรรม : 17 ตุลาคม 2567 – 14 พฤศจิกายน 2567 [Click](https://ro.gnjoy.in.th/2024-halloween-event/)",
            end_date=datetime(2024, 11, 14)
        )

        embed.add_field(name="\n", value="", inline=False)
        
        self.add_event(
            embed,
            title="๐ 📜 Pao-Ying-Chub Top Up Promotion",
            link="> ⏰ ระยะเวลากิจกรรม : 17 ตุลาคม 2567 – 11 ธันวาคม 2567 (23.59น.) [Click](https://event.gnjoy.in.th/RagnarokOnline/RO4thClasses/Minigame)",
            end_date=datetime(2024, 12, 11)
        )

        embed.add_field(name="\n", value="", inline=False)

        self.add_event(
            embed,
            title="๐ 📜 ROS2024 Merchant",
            link="> ⏰ ระยะเวลากิจกรรม : 22 สิงหาคม 2567 – 28 พฤศจิกายน 2567 \n (ก่อนปิดปรับปรุงเซิร์ฟเวอร์) [Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)",
            end_date=datetime(2024, 11, 28)
        )

        # เพิ่มข้อมูลพื้นฐานอื่นๆ
        embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
        embed.add_field(name='Website RO : https://ro.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Website Gnjoy : https://www.gnjoy.in.th/', value='', inline=False)
        embed.add_field(name='Instagram : https://www.instagram.com/gravitygametech_official/', value='', inline=False)
        
        embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1299044744093106186/464333560_562127592869305_1188082432395752027_n.png?ex=671bc532&is=671a73b2&hm=93c12d4fcbcbe75bd7a6af3e3532fc2a253e8cad5421d322a00f6dd71c79accb&=&format=webp&quality=lossless&width=1050&height=700')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

        return embed

def setup(bot):
    bot.add_cog(DailyAnnouncement(bot))
