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
        if message.content.lower() == 'คาฟ่าฉันต้องการผู้ช่วย!':
            # Create Embed
            embed = discord.Embed(
                title='✨ __รวมไอดีของลุงมายด์__ ✨',
                color=0x66FFFF,
                description='> หากคุณกำลังประสบกับปัญหา เกราะแตก , ตีมอนไม่เข้า , ตั๋ววาร์ปหมด ปัญหาเหล่านี้จะหมดไปเมื่อมีไอดีลุงมายด์!',
            )
            
            embed.add_field(name=':man_scientist: ไอดี Genetic เคลือบเกราะ', value='', inline=False)
            embed.add_field(
                name='๐ ตัวละคร Genetic',
                value='> Id : ```mildro01```' \t Password : ```Mild1234``` \t รหัส4ตัว : ``1423``,
                inline=False
            )
            
            # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)

            embed.add_field(name=':mage: ไอดี Sorcerer เคลือบอาวุธ', value='', inline=False)
            embed.add_field(
                name='๐ ตัวละคร Sorcerer',
                value='> Id : ```mildro02```' \t Password : ```Mild1234``` \t รหัส4ตัว : ``2535``,
                inline=False
            )

            # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)

            embed.add_field(name=':church: ไอดี Acolyte วาร์ป', value='', inline=False)
            embed.add_field(
                name='๐ ตัวละคร Acolyte',
                value='> Id : ```mildro03```' \t Password : ```Mild1234``` \t รหัส4ตัว : ``1423``,
                inline=False
            )

            # เว้นระยะห่างหนึ่งบรรทัด
            embed.add_field(name="\n", value="\n", inline=False)
            
            embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1291645672512290886/Ro_CT_copy.jpg?ex=6700da45&is=66ff88c5&hm=ade4994c2bdeb59d5e96f5b533112e396073e9055b9e840310ce174c6c76e1ed&=&format=webp')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/1173912177585963048/1291607292411641887/804-mets_alpha.png?ex=6700b687&is=66ff6507&hm=6535b644b35d4c28b98ecd425d5dfe3de79df341bd6218ff9dc8ad5eb6852e8b&=&format=webp&quality=lossless')

            await message.channel.send(embed=embed)
            
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
