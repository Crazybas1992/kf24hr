import discord
import requests
import csv
import io
from discord import Option
from discord.ext import commands
from kafra import GUILD_IDS  # นำเข้า GUILD_IDS จากไฟล์หลัก

# ฟังก์ชันดึงข้อมูลจาก Google Sheets
async def fetch_google_sheet_data():
    sheet_url = (
        "https://docs.google.com/spreadsheets/d/1PQkLSV5H98zaMp2qU6isgBbfNYjEIHwop6fWX0MVZC4/export?format=csv&id=1PQkLSV5H98zaMp2qU6isgBbfNYjEIHwop6fWX0MVZC4&gid=0"
    )
    try:
        response = requests.get(sheet_url)
        response.raise_for_status()
        data = response.content.decode("utf-8")
        csv_reader = csv.reader(io.StringIO(data))
        return list(csv_reader)  # คืนค่าข้อมูลในรูปแบบ list
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

class Vip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=GUILD_IDS,
                             name="vip-check",
                             description="💳 ตรวจสอบข้อมูล VIP จากกลุ่มซื้อขายโดยระบุ `VIP-00` ตามที่คุณต้องการ")
    async def vip_check(self, ctx, vip_id: str):
        # ดึงข้อมูลจาก Google Sheets
        data = await fetch_google_sheet_data()
        if data is None:
            await ctx.respond("ไม่สามารถดึงข้อมูลจาก Google Sheets ได้.", ephemeral=True)
            return

        # ค้นหาข้อมูลตามรหัสที่ระบุในคำสั่ง
        found = False
        for row in data[1:]:  # เริ่มจากแถวที่ 1 เพราะแถวที่ 0 คือหัวข้อ
            if row[0].strip() == vip_id.strip():  # เปรียบเทียบโดยไม่สนใจช่องว่าง
                embed = discord.Embed(
                    title="VIP - Credit : 💳",
                    color=discord.Color.blue()
                )
                embed.add_field(name="รหัส", value=row[0], inline=True)
                embed.add_field(name="ชื่อ - นามสกุล", value=row[1], inline=True)
                embed.add_field(name="Facebook", value=f"```{row[2]}```", inline=False)
                embed.add_field(name="Link", value=row[3], inline=False)

                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1173912177585963048/1281122311210139668/credit-card.png?ex=66da91a1&is=66d94021&hm=c456d7b22790817d665a766c7ef57ab09fa5dfbb573a139f81cb6ba298f16b3f&=&format=webp&quality=lossless")
                embed.set_image(url="https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66c99960&is=66c847e0&hm=32267fa1884cb28fd910c4f7ca5994452c657e9f5f65e399a5a4d826c185adc4&=&format=webp&quality=lossless&width=2160&height=82")

                await ctx.respond(embed=embed, ephemeral=True)
                found = True
                break

        if not found:
            await ctx.respond(f"ไม่พบข้อมูลสำหรับรหัส VIP: {vip_id}", ephemeral=True)

def setup(bot):
    bot.add_cog(Vip(bot))
