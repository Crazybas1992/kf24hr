import discord
from discord.ext import commands
from discord import Option, slash_command
from kafra import GUILD_IDS  # นำเข้าตัวแปร GUILD_IDS จาก kafra.py


class ItemSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_IDS,  # ใช้ GUILD_IDS ที่กำหนดใน kafra.py
        description="🔍 ค้นหาไอเท็มจากชื่อ"
    )
    async def search_item(self, ctx: discord.ApplicationContext, item_name: Option(str, "กรุณาใส่ชื่อไอเท็ม")):
        search_url = f"https://www.divine-pride.net/database/search?q={item_name.replace(' ', '+')}"
        
        embed = discord.Embed(
            title=f"ผลการค้นหา: {item_name}",
            description=f"คลิก [ที่นี่]({search_url}) เพื่อดูรายละเอียดเพิ่มเติม",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1173912177585963048/1280073658483609700/search.png?ex=66d6c0fe&is=66d56f7e&hm=a0e142f02e5f1ff1a6ffab66ab239969ce71788a24a2eec38e145012bc05b45b&=&format=webp&quality=lossless")  # เปลี่ยน URL เป็น URL ของภาพที่คุณต้องการ
        embed.set_footer(text='ข้อมูลอ้างอิงจาก www.divine-pride.net')

        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(ItemSearch(bot))