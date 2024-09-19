# ==================== Import Statements ==================== #
import discord
from discord.ext import commands
import random
import datetime
# =========================================================== #

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_last_asked = {}  # Dictionary to keep track of last ask time


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return  # Ignore messages from the bot itself

        # =========================================================== #

        # Handle "คาฟ่าอัพเดท?" command
        if message.content.lower() == 'คาฟ่าอัพเดท?':
            # Create Embed
            embed = discord.Embed(
                title='📢 รายการอัปเดตประจำสัปดาห์ 📢',
                color=0x66FFFF,
                description='[รายการอัปเดต วันที่ 19 กันยายน 2567](https://ro.gnjoy.in.th/patch-update-19-september-2567/?fbclid=IwY2xjawFYkm1leHRuA2FlbQIxMAABHbkFG4KjRYsq_WixMHOS_YRsAHlBDt8azM3Ifj52NawIr079LqLy94o9Aw_aem_i-UVzUg-g3M0x_Ugt5AQWQ)',
                timestamp=discord.utils.utcnow()
            )
            
            embed.add_field(name='✨ รายการอัปเดต', value='', inline=False)
            embed.add_field(
                name='๐ Saint Crown Scroll [19Sep – 3Oct]',
                value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/saint-crown-scroll/)',
                inline=False
            )
            embed.add_field(
                name='๐ Special Sparkling Gold Exchange [19Sep – 17Oct]',
                value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/roright/exchange-machine-update/)',
                inline=False
            )
            embed.add_field(
                name='๐ Spend Promotion September 2024 (V2) [19 – 25Sep]',
                value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/spendpromotion-september-2024-v2/)',
                inline=False
            )
            
            # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)
    
            embed.add_field(
                name='✨ รายการแก้ไข',
                value=(
                    '๐ แก้ไข NPC Pre Event 4th Class Event ให้ทำงานให้ถูกต้อง\n'
                    '> แก้ไขให้สามารถ Enchant Costume ที่มี Enchant อยู่แล้วได้\n'
                    '> แก้ไขให้เมื่อ Enchant แล้วหิน Slot อื่นไม่หายไป อาทิเช่น effect Stone, Dual Stone, Loft Stone เป็นต้น\n'
                ),
                inline=False
            )
            
            embed.add_field(name="\n", value="\n", inline=False)
    
            embed.add_field(name='✨ Event Now!', value='', inline=False)
            embed.add_field(
                name='๐ Choco Adventure สดุดีราชาวานร EXP UP +150% (250%)',
                value='5 กันยายน 2567 – 3 ตุลาคม 2567',
                inline=False
            )
            embed.add_field(
                name='๐ Thanksgiving Event',
                value='19 - 23 กันยายน 2567 [Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)',
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
            
            embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1286202719140315211/460290319_537016578713740_276002939991631983_n.png?ex=66ed0d20&is=66ebbba0&hm=b4242d4f282f4609caaa05d05da63a5ddf9331c4eca86aced77d1f56267aa744&=&format=webp&quality=lossless&width=1050&height=700')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png')

            # Send Embed to the channel
            await message.channel.send(embed=embed)

            return  # Ensure that the function exits here to prevent duplicate responses

        # =========================================================== #
        
        # Handle "คาฟ่าดวงของฉันวันนี้?" command
        if message.content.lower() == 'คาฟ่าดวงของฉันวันนี้?':
            user_id = message.author.id
            current_time = datetime.datetime.now()

            # Check if the user has asked today
            if user_id in self.user_last_asked:
                last_asked = self.user_last_asked[user_id]
                if last_asked.date() == current_time.date():
                    await message.channel.send('คุณได้ถามคำถามนี้ไปแล้วในวันนี้!')
                    return

            # Update the last asked time
            self.user_last_asked[user_id] = current_time

            # Generate fortune
            fortune_percent = random.randint(1, 100)
            
            response = (f"ดวงของคุณ {message.author.mention} วันนี้อยู่ที่ระดับ {fortune_percent}% อยากลองเสี่ยงอะไรดูสักหน่อยมั้ยล่ะ?")

            await message.channel.send(response)
            return  # Ensure that the function exits here to prevent duplicate responses
        # Process other commands
        await self.bot.process_commands(message)
        
        # =========================================================== #

        # เงื่อนไขสำหรับข้อความที่ต้องการ
        if message.content.lower() == 'คาฟ่าเรียกลุงมายด์!':
            # ส่งรูปภาพจาก URL
            image_url = "https://media.discordapp.net/attachments/1173912177585963048/1280029153931821110/NPC_mild.png?ex=66d6978c&is=66d5460c&hm=af088c6f8937b622b77d715dc0382b22f6365af1a68e703fe5b882fe1d8ea35f&=&format=webp&quality=lossless&width=386&height=686"  # ใส่ URL ของรูปภาพที่ต้องการ
            await message.channel.send(image_url)
            return

        await self.bot.process_commands(message)

    @commands.command()
    async def reset_fortune(self, ctx):
        """Command to reset the fortune asking limits (for testing)."""
        user_id = ctx.author.id
        if user_id in self.user_last_asked:
            del self.user_last_asked[user_id]
            await ctx.send('ข้อมูลการถามคำถามของคุณได้ถูกรีเซ็ตแล้ว!')
        else:
            await ctx.send('คุณยังไม่เคยถามคำถามนี้')

def setup(bot):
    bot.add_cog(Chat(bot))
