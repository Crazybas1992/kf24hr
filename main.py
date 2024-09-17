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

    @slash_command(
        guild_ids=GUILD_IDS,
        description="🗡 ข้อมูลเพิ่มเติมเกี่ยวกับคลาสสี่ที่อัพเดท ณ เวลานี้!"
    )
    async def อาชีพคลาสสี่(self, ctx, class4: Option(str, '⚔️กรุณาเลือกอาชีพ', choices=[
        'Abyss Chaser', 'Arch Mage', 'Biolo', 'Cardinal', 'Dragon Knight', 'Elemental Master', 
        'Imperial Guard', 'Inquisitor', 'Meister', 'Troubadour & Trouvere', 'Windhawk', 'Shadow Cross'
    ])):
        await ctx.defer(ephemeral=True)  # ใช้ defer เพื่อยืดเวลาในการประมวลผล
        embed = self.create_embed_for_class(class4)
        if embed:
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            await ctx.respond(f"ไม่พบข้อมูลสำหรับอาชีพ: {class4}", ephemeral=True)

    def create_embed_for_class(self, class4):
        # เพิ่มข้อมูล 'image' ในทุกคลาส
        classes_data = {
            'Abyss Chaser': {
                'title': 'Abyss Chaser',
                'description': 'Abyss Chaser คลาสขั้นสูงของ Shadow Chaser มีความสามารถในการใช้พลังของห้วงลึกเพื่อทำการโจมตีต่างๆ...',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/abyss-chaser-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1276923227179974687/image.png',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281453642125410455/E0B8A3E0B8B9E0B89B20Abyss20Chaser1.png?ex=66dbc634&is=66da74b4&hm=336ca762ec7bb48ca4e63859b004d856ff2d1ca2c635f434a3491637d05d7e42&=&format=webp&quality=lossless&width=1606&height=1138'
            },
            'Arch Mage': {
                'title': 'Arch Mage',
                'description': 'Arch Mage คือคลาสที่พัฒนาขึ้นจาก Warlock ซึ่งนำเสนอมายากลสุดพิเศษที่ผสมผสานความสวยงามเข้ากับพลังเวทมนตร์ที่ทรงพลัง คุณสามารถสร้างทั้งทุ่งดอกไม้เพลิง หรือสายฝนผลึกน้ำแข็งอันบริสุทธิ์ เมื่อถึงช่วง Climax เหล่านักเวทย์สามารถร่ายเวทที่ทรงพลังยิ่งขึ้นได้',
                'link': 'https://sigmathefallen.blogspot.com/search?q=Arch+Mage',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281458349258309673/Arch_Mage.png?ex=66dbca96&is=66da7916&hm=66fe9b19a2c870e16eb526962d42d328789f0dca706c06afcfdf1812c6fc2c55&=&format=webp&quality=lossless&width=202&height=204',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281458095637266502/E0B8A3E0B8B9E0B89B20Arch20Mage1.png?ex=66dbca5a&is=66da78da&hm=74a6246ee26114d744a0d5734ca098f7cde4a018b86c83e546ebf588f4b14fc8&=&format=webp&quality=lossless&width=1608&height=1138'
            },
            'Biolo': {
                'title': 'Biolo',
                'description': 'Biolo คลาสขั้นสูงของ Geneticist เป็นผู้เชี่ยวชาญด้านเทคโนโลยีชีวภาพ...',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/biolo-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1276925153170690112/image.png',
                'image': 'https://images-ext-1.discordapp.net/external/pxmyG-5GlMlitYvhLudATUHJZDpOBXr21VbzoV83QKQ/https/www.realro.net/home/ckfinder/userfiles/images/%28%25E0%25B8%25A3%25E0%25B8%25B9%25E0%25B8%259B%29%2520Biolo%282%29.png?format=webp&quality=lossless&width=1842&height=1138'
            },
            'Cardinal': {
                'title': 'Cardinal',
                'description': 'Cardinal คลาสขั้นสูงของ Arch Bishop มีความเชี่ยวชาญในบทบาทสนับสนุน เช่น การรักษาและเสริมพลังให้กับพันธมิตรด้วยบัฟต่างๆ พวกเขายังมีเวทมนตร์ศักดิ์สิทธิ์ที่ทรงพลังสำหรับการขับไล่มอนสเตอร์ชั่วร้ายอีกด้วย',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/cardinal-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281462624684478494/Cardinal.png?ex=66dbce92&is=66da7d12&hm=5d1138d34ee1cca572d0838dc8b794f5f24692d526ad990f1192e1ddd9f487fc&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281462959503179798/Screenshot_2567-09-06_at_10.56.05.png?ex=66dbcee1&is=66da7d61&hm=2ece34f7e7c4b2ebad9c66cd87f95559520141997ef757cdab6a0b9797148d74&=&format=webp&quality=lossless&width=550&height=686'
            },
            'Dragon Knight': {
                'title': 'Dragon Knight',
                'description': 'Dragon Knights เป็นการวิวัฒนาการขั้นสุดท้ายของคลาส Rune Knight ชื่อของพวกเขามักจะย่อและเรียกว่า DK พวกเขาได้แลกเปลี่ยนมังกรที่ใช้เป็นพาหนะสำหรับมังกรที่มีอายุมากขึ้น และพร้อมที่จะสร้างความเสียหายอย่างรุนแรงด้วยอาวุธใหม่ที่ทรงพลัง ขณะเดียวกันก็มีค่าพลังชีวิต (HP) สูงที่สุดเมื่อเปรียบเทียบกับคลาสอื่นๆ',
                'link': 'https://sigmathefallen.blogspot.com/2024/08/dragon-knight-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281463389993828454/Dragon_Knight.png?ex=66dbcf48&is=66da7dc8&hm=eebcfb72f4b6c036fd3af6ca43d707292ed605b165860af96f6ee773becf44d2&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281454234281316453/E0B8A3E0B8B9E0B89B20Dragon20Knight2.png?ex=66dbc6c1&is=66da7541&hm=0ad11be3b4f0beca1c292de179d0d69cb87fdd4070d01df9529c6a5f1cae52df&=&format=webp&quality=lossless&width=1960&height=1100'
            },
            'Elemental Master': {
                'title': 'Elemental Master',
                'description': 'Elemental Master เป็นคลาสที่สี่ของ Sorcerer เชี่ยวชาญในการควบคุมธาตุธรรมชาติ คุณสามารถเรียกวิญญาณที่มีความสามารถขั้นสูงและพันธมิตรสนับสนุนด้วยเวทมนตร์ต่างๆ',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/elemental-master-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281463561264037888/Elemental_Master.png?ex=66dbcf71&is=66da7df1&hm=8e9a873bf0fbd00a7a577f5bff3c631f9f997015cdf31e90b157f0256006c5d3&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281454401143439380/E0B8A3E0B8B9E0B89B20Elemental20Master1.png?ex=66dbc6e9&is=66da7569&hm=d7ac1a17a824729e0c08a21f2bc7af7e5ce536ece83bcf9a9448198c5ec447aa&=&format=webp&quality=lossless&width=1328&height=1138'
            },
            'Imperial Guard': {
                'title': 'Imperial Guard',
                'description': 'Imperial Guards เป็นคลาสที่สี่ของ Royal Guard\nความเชื่อที่ไม่สามารถเคลื่อนไหวของ Imperial Guard ได้มอบพลังที่แท้จริงให้กับพวกเขา นี่คืออาชีพที่มุ่งมั่นในการปกป้องพันธมิตรแทนการทำลาย พวกเขาถูกติดตั้งด้วยดาบและโล่ รวมถึงการโจมตีศักดิ์สิทธิ์ที่ทรงพลัง',
                'link': 'https://sigmathefallen.blogspot.com/2024/08/imperial-guard-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281463830958051378/Imperial_Guard.png?ex=66dbcfb1&is=66da7e31&hm=2b91c99ee9788c2db26df1ba718b9e3c514e2987bb5e3ca4cdb41061596bae35&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281454608291598398/E0B8A3E0B8B9E0B89B20Imperial20Guard1.png?ex=66dbc71a&is=66da759a&hm=dc1ec75b0eecda467e8ae97c734d827383f1c6e1cccba4e226403c14a3841ef3&=&format=webp&quality=lossless&width=2152&height=1138'
            },
            'Inquisitor': {
                'title': 'Inquisitor',
                'description': 'Inquisitor คลาสที่พัฒนาขึ้นสำหรับ Sura เป็นตัวแทนของการตัดสินของพระเจ้า ด้วยความเชื่อที่มั่นคง พวกเขาสามารถปลดปล่อยการตัดสินของพระเจ้าต่อผู้ที่กระทำความชั่วได้',
                'link': 'https://sigmathefallen.blogspot.com/2024/08/inquisitor-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281464080552558765/image.png?ex=66dbcfed&is=66da7e6d&hm=218e45d53fb4e757f3052aee3d7c9e81f00e270621718c42ed23aac6e00acc9a&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281454833500426250/E0B8A3E0B8B9E0B89B20Inquisitor1.png?ex=66dbc750&is=66da75d0&hm=3f54b5df08fb9b25c7a5f7473f37290b648bf2941397613b253e547f14b58d1d&=&format=webp&quality=lossless&width=1100&height=660'
            },
            'Meister': {
                'title': 'Meister',
                'description': 'Meister เป็นคลาสที่พัฒนาจาก Mechanic โดดเด่นด้านวิศวกรรมกล สามารถเรียกหุ่นยนต์ Auto Battle มาช่วยต่อสู้และเสริมพลังให้พันธมิตรด้วยอุปกรณ์ต่างๆ',
                'link': 'https://sigmathefallen.blogspot.com/search?q=Meister',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281459869890646016/image.png?ex=66dbcc01&is=66da7a81&hm=170bbe388cd9c052f84a4cd694fb21fb56e71b03fcd3805ccead57585cf030ad&=&format=webp&quality=lossless&width=206&height=210',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281460072182054922/E0B8A3E0B8B9E0B89B20Meister1.png?ex=66dbcc31&is=66da7ab1&hm=dc5ffc6842e0c304e1efaa2d79c25f06f218a41d2428cf2e28307b45482363a5&=&format=webp&quality=lossless&width=1100&height=654'
            },
            'Shadow Cross': {
                'title': 'Shadow Cross',
                'description': 'Shadow Cross เป็นคลาสงานที่สี่ของ Assassin/Assassin Cross/Guillotine Cross สำหรับโจมตีศัตรู พวกเขายังคงใช้อาวุธสองชิ้นแยกกัน (จากมีดไปจนถึงดาบมือเดียว) หรือ Katars แต่พวกเขาจะได้รับความสามารถใหม่ชื่อของ Shadow Cross มักจะถูกย่อและย่อเป็น SX ซึ่ง X เหมือนกับสัญลักษณ์กากบาท',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/windhawk-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281464340092031077/Shadow_Cross.png?ex=66dbd02b&is=66da7eab&hm=bfae705227919785272053f69567dd33e8b4d302555813054deca01fdc39fdae&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281456865036730419/E0B8A3E0B8B9E0B89B20Shadow20Cross1.png?ex=66dbc934&is=66da77b4&hm=ee83f266d7676790546bcf4d52a287ec3681d10fc73cfc4e4467122fe49c222f&=&format=webp&quality=lossless&width=1528&height=1138'
            },
            'Troubadour & Trouvere': {
                'title': 'Troubadour & Trouvere',
                'description': 'Troubadour เป็นคลาสที่พัฒนามาจาก Maestro ใช้เสียงเพลงเพื่อเพิ่มขวัญและกำลังใจให้กับพันธมิตร พลิกสถานการณ์การต่อสู้ผ่านดนตรี และ Trouvere เป็นคลาสที่พัฒนามาจาก Wanderer ใช้การเต้นรำเพื่อเพิ่มขวัญและกำลังใจให้กับพันธมิตร เปลี่ยนทิศทางการต่อสู้ด้วยเพลงและการเต้น',
                'link': 'https://sigmathefallen.blogspot.com/2024/06/troubadour-trouvere-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281466145714470952/artworks-0N8TSyOgr3nn3U4I-dHMinQ-t500x500.png?ex=66dbd1d9&is=66da8059&hm=1b208232be2a4cccb15efee817ccd62f17dc980e2390ceb951ef8068b7da8926&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281456367756116038/E0B8A3E0B8B9E0B89B20Troubadour202620Trouvere1.png?ex=66dbc8be&is=66da773e&hm=af5ee95e4880cb9daa06cbe3146ee1913ae5930c70941c3b4b4f340bd9b804de&=&format=webp&quality=lossless&width=1970&height=1138'
            },
            'Windhawk': {
                'title': 'Wind Hawk',
                'description': 'Wind Hawk คลาสที่พัฒนาขึ้นสำหรับ Ranger สามารถใช้พลังของลมได้อย่างเต็มที่ ด้วยทักษะในการยิงลูกศรลมที่ทรงพลัง พวกเขายังสามารถสื่อสารกับสัตว์ป่า ทำให้สามารถใช้ Warg และ Falcon ร่วมกันได้',
                'link': 'https://sigmathefallen.blogspot.com/2024/07/windhawk-2nd-version.html',
                'thumbnail': 'https://media.discordapp.net/attachments/1173912177585963048/1281462045547434034/Windhawk.png?ex=66dbce08&is=66da7c88&hm=4e68e57708dcd0c4b1d4ddecc6f517727efaeb2346606e82ca5fb4805e766a22&=&format=webp&quality=lossless',
                'image': 'https://media.discordapp.net/attachments/1173912177585963048/1281456711772930180/E0B8A3E0B8B9E0B89B20Wind20Hawk1.png?ex=66dbc910&is=66da7790&hm=bfc3a95b8cb21c1bf928451e7824dc894d248022e9633f0c79b33495d7946da4&=&format=webp&quality=lossless&width=2152&height=1138'
            }
        }

        if class4 in classes_data:
            class_info = classes_data[class4]
            embed = discord.Embed(
                title=class_info['title'],
                description=f"`{class_info['description']}`\nรายละเอียดเพิ่มเติม [คลิก]({class_info['link']})",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=class_info['thumbnail'])
            embed.set_image(url=class_info['image'])  # เพิ่มการตั้งค่าภาพให้ครบทุกคลาส
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
                "name": "🎁 Item Code: ROS 2024 Coin จำนวน 50 เหรียญ",
                "description": "```BD06-2F8C-4DE6-A3EA```",
                "start_date": datetime(2024, 9, 9),
                "end_date": datetime(2024, 9, 12),
            },
            {
                "name": "🎁 Item Code: ROS 2024 Coin จำนวน 100 เหรียญ",
                "description": "```1112-3C73-4491-AF94```",
                "start_date": datetime(2024, 9, 9),
                "end_date": datetime(2024, 9, 12),
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
