# ==================== Import Statements ====================
import discord
from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1119100375681736878)  # เปลี่ยนเป็น ID ของช่องที่คุณต้องการ

        if channel is not None:
            embed = discord.Embed(
                title='📢 ยินดีต้อนรับ!',
                description=f"ยินดีต้อนรับคุณ {member.mention} เข้าสู่เซิร์ฟเวอร์!",
                color=0x66FFFF
            )
            embed.set_thumbnail(url='https://example.com/welcome_image.png')  # เปลี่ยน URL เป็นลิงก์ของภาพที่คุณต้องการ
            embed.add_field(name='💬 กฎของเซิร์ฟเวอร์', value='กรุณาอ่านกฎของเซิร์ฟเวอร์ในช่อง #rules', inline=False)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1119100375681736878)  # เปลี่ยนเป็น ID ของช่องที่คุณต้องการ

        if channel is not None:
            embed = discord.Embed(
                title='📢 ลาออกจากเซิร์ฟเวอร์',
                description=f"คุณ {member.mention} ได้ออกจากเซิร์ฟเวอร์แล้ว ขอให้โชคดีในอนาคต!",
                color=0xFF0000
            )
            embed.set_thumbnail(url='https://example.com/goodbye_image.png')  # เปลี่ยน URL เป็นลิงก์ของภาพที่คุณต้องการ
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Join(bot))