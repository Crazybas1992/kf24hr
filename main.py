# ==================== Import Statements ====================
import discord
from discord.ext import commands
from discord import Embed
from discord.commands import slash_command, Option
from datetime import datetime, timedelta
from kafra import GUILD_IDS


# ================================================================================= #

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ============================================================#
# ==================== Command: อาชีพคลาสสี่ ====================#
# ============================================================#

    @slash_command(guild_ids=GUILD_IDS,
        description="🗡 ข้อมูลเพิ่มเติมเกี่ยวกับคลาสสี่ที่อัพเดท ณ เวลานี้!")
    async def อาชีพคลาสสี่(self, ctx,
                    class4: Option(str, '⚔️กรุณาเลือกอาชีพ', choices=['Abyss Chaser', 'Biolo', 'Cardinal', 'Dragon Knight', 'Elemental Master', 'Imperial Guard', 'Inquisitor', 'Troubadour', 'Trouvere', 'Windhawk', 'Shadow Cross'])):
        embed = self.create_embed_for_class(class4)
        if embed:
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            await ctx.respond(f"ไม่พบข้อมูลสำหรับอาชีพ: {class4}", ephemeral=True)

    def create_embed_for_class(self, class4):
        # ข้อมูลของแต่ละคลาส
        classes_data = {
            'Abyss Chaser': {
                'title': "Abyss Chaser",
                'description': "Abyss Chaser คลาสขั้นสูงของ Shadow Chaser มีความสามารถในการใช้พลังของห้วงลึกเพื่อทำการโจมตีต่างๆ...",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/abyss-chaser-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276923227179974687/image.png",
                'image': "https://media.discordapp.net/attachments/1173912177585963048/1280017264510500894/image.png?ex=66d68c79&is=66d53af9&hm=7b21f4c2d5c4603ed0c64150b2ac8705fcc7cc7b3f03fc8c1d10775112162492&=&format=webp&quality=lossless&width=690&height=686"
            },
            'Biolo': {
                'title': "Biolo",
                'description': "Biolo คลาสขั้นสูงของ Geneticist เป็นผู้เชี่ยวชาญด้านเทคโนโลยีชีวภาพ...",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/biolo-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Cardinal': {
                'title': "Cardinal",
                'description': "Cardinal คลาสขั้นสูงของ Arch Bishop มีความเชี่ยวชาญในบทบาทสนับสนุน เช่น การรักษาและเสริมพลังให้กับพันธมิตรด้วยบัฟต่างๆ พวกเขายังมีเวทมนตร์ศักดิ์สิทธิ์ที่ทรงพลังสำหรับการขับไล่มอนสเตอร์ชั่วร้ายอีกด้วย",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/cardinal-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Dragon Knight': {
                'title': "Dragon Knight",
                'description': "Dragon Knights เป็นการวิวัฒนาการขั้นสุดท้ายของคลาส Rune Knight ชื่อของพวกเขามักจะย่อและเรียกว่า 'DK' พวกเขาได้แลกเปลี่ยนมังกรที่ใช้เป็นพาหนะสำหรับมังกรที่มีอายุมากขึ้น และพร้อมที่จะสร้างความเสียหายอย่างรุนแรงด้วยอาวุธใหม่ที่ทรงพลัง ขณะเดียวกันก็มีค่าพลังชีวิต (HP) สูงที่สุดเมื่อเปรียบเทียบกับคลาสอื่นๆ",
                'link': '(https://sigmathefallen.blogspot.com/2024/08/dragon-knight-2nd-version.html)',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Elemental Master': {
                'title': "Elemental Master",
                'description': "Elemental Master เป็นคลาสที่สี่ของ Sorcerer เชี่ยวชาญในการควบคุมธาตุธรรมชาติ คุณสามารถเรียกวิญญาณที่มีความสามารถขั้นสูงและพันธมิตรสนับสนุนด้วยเวทมนตร์ต่างๆ",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/elemental-master-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Imperial Guard': {
                'title': "Imperial Guard",
                'description': "Imperial Guards เป็นคลาสที่สี่ของ Royal Guard\nความเชื่อที่ไม่สามารถเคลื่อนไหวของ Imperial Guard ได้มอบพลังที่แท้จริงให้กับพวกเขา นี่คืออาชีพที่มุ่งมั่นในการปกป้องพันธมิตรแทนการทำลาย พวกเขาถูกติดตั้งด้วยดาบและโล่ รวมถึงการโจมตีศักดิ์สิทธิ์ที่ทรงพลัง",
                'link': 'https://sigmathefallen.blogspot.com/2024/08/imperial-guard-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Inquisitor': {
                'title': "Inquisitor",
                'description': "Inquisitor คลาสที่พัฒนาขึ้นสำหรับ Sura เป็นตัวแทนของการตัดสินของพระเจ้า ด้วยความเชื่อที่มั่นคง พวกเขาสามารถปลดปล่อยการตัดสินของพระเจ้าต่อผู้ที่กระทำความชั่วได้",
                'link': 'https://sigmathefallen.blogspot.com/2024/08/inquisitor-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Troubadour': {
                'title': "Troubadour",
                'description': "Troubadour คลาสที่พัฒนาขึ้นสำหรับ Maestro เล่นเพลงที่สวยงามเพื่อเพิ่มขวัญและกำลังใจให้กับพันธมิตร นี่คืออาชีพที่เปลี่ยนทิศทางของการต่อสู้บนสนามรบผ่านเสียงเพลงและดนตรี",
                'link': 'https://sigmathefallen.blogspot.com/2024/06/troubadour-trouvere-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Trouvere': {
                'title': "Trouvere",
                'description': "Trouvere คลาสที่พัฒนาขึ้นสำหรับ Wanderer เต้นรำที่ดึงดูดใจเพื่อเพิ่มขวัญและกำลังใจให้กับพันธมิตร นี่คืออาชีพที่เปลี่ยนทิศทางของการต่อสู้บนสนามรบผ่านเพลงและการเต้น",
                'link': 'https://sigmathefallen.blogspot.com/2024/06/troubadour-trouvere-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Windhawk': {
                'title': "Windhawk",
                'description': "Wind Hawk คลาสที่พัฒนาขึ้นสำหรับ Ranger สามารถใช้พลังของลมได้อย่างเต็มที่ ด้วยทักษะในการยิงลูกศรลมที่ทรงพลัง พวกเขายังสามารถสื่อสารกับสัตว์ป่า ทำให้สามารถใช้ Warg และ Falcon ร่วมกันได้",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/windhawk-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            'Shadow Cross': {
                'title': "Shadow Cross",
                'description': "Shadow Cross เป็นคลาสงานที่สี่ของ Assassin/Assassin Cross/Guillotine Cross สำหรับโจมตีศัตรู พวกเขายังคงใช้อาวุธสองชิ้นแยกกัน (จากมีดไปจนถึงดาบมือเดียว) หรือ Katars แต่พวกเขาจะได้รับความสามารถใหม่ชื่อของ Shadow Cross มักจะถูกย่อและย่อเป็น 'SX' ซึ่ง 'X' เหมือนกับสัญลักษณ์กากบาท",
                'link': 'https://sigmathefallen.blogspot.com/2024/07/windhawk-2nd-version.html',
                'thumbnail': "https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png"
            },
            # เพิ่มข้อมูลของคลาสอื่น ๆ เช่นเดียวกัน
        }

        # ตรวจสอบว่ามีข้อมูลสำหรับคลาสที่เลือกหรือไม่
        if class4 in classes_data:
            class_info = classes_data[class4]
            embed = discord.Embed(
                title=class_info['title'],
                description=f"```{class_info['description']}```\nรายละเอียดเพิ่มเติม [คลิก]({class_info['link']})",
                color=discord.Color.green()
            )
            # เพิ่มรูปภาพ thumbnail
            embed.set_thumbnail(url=class_info['thumbnail'])
            
            # เพิ่มรูปภาพหลัก
            embed.set_image(url=class_info['image'])

            return embed
        else:
            return None

# =================================================================================== #
#//////////////////////////// Cmd ภายในเกม ///////////////////////////////////////////#
# =================================================================================== #

    @slash_command(guild_ids=GUILD_IDS, 
                   description="🗒 รวมคำสั่งที่ใช้แล้ว จะช่วยทำให้ผู้เล่นสะดวกมากยิ่งขึ้นในเกม Ragnarok Online")
    async def คำสั่งภายในเกม(
        self,
        ctx):
        # สร้าง Embed
        embed = discord.Embed(
            title="✨__**[RO-GGT] คำสั่งที่ช่วยให้เล่นได้สะดวกขึ้น**__",
            description=(
                "⚙️ นี่เป็นเพียง Option บางส่วนที่เราแนะนำกับคุณ ยังมีคำสั่งอื่นๆอีกมากมายให้คุณได้ปรับแต่งเพิ่มเติมเพียงแค่ กด `Alt+Y`\n\n"
                "```/mineffect```🔼\t\tลดหรือเปลี่ยน การแสดง Effect บางอย่าง เพื่อลดอาการกระตุกในการเล่น\n\n"
                "```/aura```🔼\t\tเปิด/ปิด การลดแสดงแสง Aura\n\n"
                "```/aura2```🔼\t\tเปิด/ปิด การแสดงแสง Aura\n\n"
                "```/fog```🔼\t\tเปิด/ปิด การแสดงหมอก\n\n"
                "```/quake```🔼\tเปิด/ปิด การแสดง Effect จอสั่น\n\n"
                "```/lightmap```🔼\t\tเปิด/ปิด การแสดง Effect เกียวกับแสงบนแผนที่\n\n"
                "```/zoom```🔼\t\tเปิด/ปิด ระดับการ Zoom เพิ่มเติมอีก 3 ช่อง\n\n"
                "```/skip```🔼\t\tถ้าค่าเป็น Off ตัวเกมจะพยายามแสดงทุก ๆ Frame ที่สามารถ Render ออกมาได้ ถ้าค่าเป็น On ตัวเกมจะข้ามบาง Frame ที่ Render ออกมา เพื่อจำกัด FPS ไว้"
            ),
            color=0x00ff00  # เปลี่ยนเป็นสีที่คุณต้องการ
        )
# เพิ่ม Thumbnail
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png?ex=66c79f43&is=66c64dc3&hm=3ae2485177851a34a868cdfd90b69ddf33f0acbcf47adcdac4b3d09e1031d1cb&=&format=webp&quality=lossless&width=1138&height=1138")  # เปลี่ยน URL เป็น URL ของภาพที่คุณต้องการ
        embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66c99960&is=66c847e0&hm=32267fa1884cb28fd910c4f7ca5994452c657e9f5f65e399a5a4d826c185adc4&=&format=webp&quality=lossless&width=2160&height=82')
        # ส่ง Embed

        await ctx.respond(embed=embed, ephemeral=True)

# =================================================================================== #
#//////////////////////////// Cmd รางวัลของฉัน  ////////////////////////////////////////#
# =================================================================================== #

    # Helper function สำหรับสร้าง embed ของรางวัล
    def create_reward_embed(self, rewards):
        now = datetime.now()
        embed = discord.Embed(
            title="🏆 __**รางวัลของฉันจากกิจกรรมต่างๆ**__ 🏆",
            description="📍 สามารถเติม item code ได้ที่หน้าเว็บไซต์ [Click](https://www.gnjoy.in.th/Manage/Coupon)",
            color=discord.Color.gold()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1173912177585963048/1279367614178787339/reward.png?ex=66d42f70&is=66d2ddf0&hm=48f49db16257ec2625c133d3dd3f88fa3c449450981dab332886551a32a37ca2&=&format=webp&quality=lossless")

        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        # Loop ผ่านรางวัลทั้งหมดและเพิ่มไปใน embed
        for reward in rewards:
            name = reward["name"]
            description = reward["description"]
            start_date = reward["start_date"]
            end_date = reward["end_date"]

            if now < start_date:
                time_left = start_date - now
                description_text = f"{description}\n📅 กิจกรรมจะเริ่มใน {time_left.days} วัน {time_left.seconds // 3600} ชั่วโมง"
            elif now > end_date:
                description_text = f"{description}\n⚠️ รางวัลนี้ได้หมดอายุแล้วเมื่อวันที่ {end_date.strftime('%d-%m-%Y')}"
            else:
                time_left = end_date - now
                days_left = time_left.days
                hours_left = time_left.seconds // 3600
                description_text = f"{description}\n⌛ เหลือเวลาอีก {days_left} วัน {hours_left} ชั่วโมง"

            embed.add_field(
                name=f"{name}",
                value=description_text,
                inline=False
            )

        embed.set_footer(text="")
        return embed

    # Slash Command สำหรับ "รางวัลของฉัน"
    @commands.slash_command(guild_ids=GUILD_IDS, description="🎁 ดูรางวัลของคุณ")
    async def รางวัลของฉัน(self, ctx: discord.ApplicationContext):
        # ตัวอย่างข้อมูลรางวัล (ควรดึงข้อมูลจริงจากฐานข้อมูลหรือ API)
        rewards = [
            {
                "name": "🎁 Item Code: ROS 2024 Coin จำนวน 100 เหรียญ",
                "description": "```6EE9-54C9-44BF-9555```",
                "start_date": datetime(2024, 8, 29),
                "end_date": datetime(2024, 9, 5),
            },
        ]

        # ใช้ helper function เพื่อสร้าง embed ของรางวัล
        embed = self.create_reward_embed(rewards)
        await ctx.respond(embed=embed, ephemeral=True)

# ================================================================================= #
#//////////////////////////// Cmd กิจกรรม ///////////////////////////////////////////#
# ================================================================================= #

    @commands.slash_command(guild_ids=GUILD_IDS,
                            description="🗓 ข้อมูลเพิ่มเติมของกิจกรรมต่างๆ ณ เวลานี้")
    async def กิจกรรม(self, ctx):
        # Defer the response to avoid timing out
        await ctx.defer(ephemeral=True)

        now = datetime.now()
        embed = discord.Embed(
            title="🗓 __**กิจกรรมทั้งหมด ณ เวลานี้**__ 🗓\n",
            color=discord.Color.green()
        )

        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        # กิจกรรม Cat Hand Gift Packager
        self.add_event(embed, 
                    "✨ Thanksgiving Event ✨",
                    "⏰ [5 กันยายน 2567 - 3 ตุลาคม 2567]\t[Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)",
                    datetime(2024, 10, 3),
                    now)

        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        self.add_event(embed, 
                    "✨ Cat Hand Gift Packager ✨",
                    "⏰ [29 สิงหาคม 2567 - 12 กันยายน 2567]\t[Click](https://ro.gnjoy.in.th/special-event-refine-certificate-packager/)",
                    datetime(2024, 9, 12),
                    now)

        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        # กิจกรรม BATTLE PASS SEASON V
        self.add_event(embed, 
                    "✨ BATTLE PASS SEASON V ✨",
                    "⏰ [18 ก.ค. - 17 ต.ค. 2567]\t[Click](https://ro.gnjoy.in.th/battle-pass-season-v-guide/)",
                    datetime(2024, 10, 17),
                    now)

        # เว้นระยะห่างหนึ่งบรรทัด
        embed.add_field(name="\n", value="\n", inline=False)

        # กิจกรรม RAGNAROK STARS 2024
        self.add_event(embed, 
                    "✨ RAGNAROK STARS 2024 ✨",
                    "⏰ [22 สิงหาคม 2567 - 28 พฤศจิกายน 2567]\t[Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)",
                    datetime(2024, 11, 28),
                    now)

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1173912177585963048/1278254083878424587/pngwing.com.png?ex=66d02262&is=66ced0e2&hm=480a6c93c57b4180ccdc168d3c1ef1b6e0d6a982a3c82991aee2456d22cb86b3&=&format=webp&quality=lossless")  # เปลี่ยน URL เป็น URL ของภาพที่คุณต้องการ
        embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66c99960&is=66c847e0&hm=32267fa1884cb28fd910c4f7ca5994452c657e9f5f65e399a5a4d826c185adc4&=&format=webp&quality=lossless&width=2160&height=82')

        await ctx.respond(embed=embed, ephemeral=True)

    def add_event(self, embed, title, link, end_date, now):
        time_left = end_date - now
        if time_left.total_seconds() > 0:
            description = f"{link}```\nเหลือเวลาของกิจกรรมอีก {time_left.days} วัน {time_left.seconds // 3600} ชั่วโมง```"
        else:
            description = f"```กิจกรรมนี้ได้สิ้นสุดลงแล้วเมื่อวันที่ {end_date.strftime('%d %B %Y')}```"
        
        embed.add_field(name=title, value=description, inline=False)
        
# ===================================================================================== #

def setup(bot):
    bot.add_cog(main(bot))
