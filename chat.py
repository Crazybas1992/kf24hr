# ==================== Import Statements ====================
import discord
from discord.ext import commands
import random
import datetime
# ===========================================================

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_last_asked = {}  # Dictionary to keep track of last ask time


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return  # Ignore messages from the bot itself

        # Handle "คาฟ่าอัพเดท?" command
        if message.content.lower() == 'คาฟ่าอัพเดท?':
            # Create Embed
            embed = discord.Embed(
                title='📢 รายการอัปเดต วันที่ 12 กันยายน 2567 📢',
                color=0x66FFFF,
                description='https://ro.gnjoy.in.th/patch-update-12-sep-2567/',
                timestamp=discord.utils.utcnow()
            )

            embed.add_field(name='✨ รายการอัปเดต', value='', inline=False)
            embed.add_field(name='๐ Spend Promotion September 2024',
                            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/spend-promotion-september-2024/)',
                            inline=False)
            embed.add_field(name='๐ Malangdo Costume Limited 7Days!',
                            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/malangdo-costume-limited-7days-12.../)',
                            inline=False)
            embed.add_field(name='๐ Pre Event Class 4',
                            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/pre-class-4-event/)',
                            inline=False)
            embed.add_field(name='๐ Update Costume Enchant Stone Box 23',
                            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/update-enchant-stone-box-23-12.../)',
                            inline=False)
            embed.add_field(name='๐ Map Drop System',
                            value='> สามารถดูรายละเอียดเพิ่มเติมได้[ที่นี่](https://ro.gnjoy.in.th/map-drop-system/)',
                            inline=False)
        # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)

            embed.add_field(name='✨ รายการแก้ไข',
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
            
            # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)

            embed.add_field(name='✨ Event Now!', value='', inline=False)
            embed.add_field(name='[5 กันยายน 2567 – 3 ตุลาคม 2567]',
                            value='Thanksgiving Event [Click](https://ro.gnjoy.in.th/2024-thanksgiving-event/)',
                            inline=False)
            embed.add_field(name='[22 สิงหาคม 2567 – 28 พฤศจิกายน 2567]',
                            value='ROS2024 Merchant [Click](https://ro.gnjoy.in.th/ragnarok-stars-2024-all-events/)',
                            inline=False)
            embed.add_field(name='[18 ก.ค. – 17 ต.ค. 2567]',
                            value='๐ BATTLE PASS SEASON V : Varmundt’s Mansion & Tower of Thanatos [Click](https://ro.gnjoy.in.th/battle-pass-season-v-guide/)',
                            inline=False)
            embed.add_field(name='▂▂▂▂▂▂▂▂▂▂▂▂▂▂', value='', inline=False)
            embed.add_field(name='Website RO : https://ro.gnjoy.in.th/',
                            value='',
                            inline=False)
            embed.add_field(name='Website Gnjoy : https://www.gnjoy.in.th/',
                            value='',
                            inline=False)
            embed.add_field(name='Instagram : https://www.instagram.com/gravitygametech_official/',
                            value='',
                            inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1283715411183140936/459530795_532360245846040_289969461215777392_n.png?ex=66e4a964&is=66e357e4&hm=6130b0f234ab3c9bba66095fedcba05a5a9bd71403c1673dcf8f40550d792e70&=&format=webp&quality=lossless&width=1400&height=720')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/1119100375681736878/1275733077590671381/kf2.png?ex=66d0d9c3&is=66cf8843&hm=43609ade7253630841d10874395cf4a7730c03d28118f2751161021a1b4f493e&=&format=webp&quality=lossless&width=686&height=686')

            # Send Embed to the channel
            await message.channel.send(embed=embed)

            return  # Ensure that the function exits here to prevent duplicate responses
        
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
            lucky_place = random.choice(['Prontera', 'Payon', 'Geffen', 'Morroc', 'Izlude', 'Alberta', 'Juno', 'Aldebaran', 'Lutie', 'Amatsu', 'Kunlun', 'Nifflheim', 'Rachel', 'Valhalla'])

            response = (f"ดวงของคุณ {message.author.mention} วันนี้อยู่ที่ระดับ {fortune_percent}% "
                        f"สถานที่ให้โชคของคุณก็คือ {lucky_place}")

            await message.channel.send(response)
            return  # Ensure that the function exits here to prevent duplicate responses
        # Process other commands
        await self.bot.process_commands(message)

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
