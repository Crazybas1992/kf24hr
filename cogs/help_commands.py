import discord
from discord.ext import commands
from discord import Option
from kafra import GUILD_IDS

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=GUILD_IDS,
        name="ช่วยเหลือ",
        description="🛠 เลือกตัวเลือกที่คุณต้องการรับคำแนะนำ"
    )
    async def help_command(
        self, 
        ctx, 
        option: Option(str, "เลือกตัวเลือก", choices=["คำนวนสเตตัส", "แต่งตัว", "ดันเจี้ยน", "คำสั่งและการแก้ไขภายในเกม"], required=True)
    ):
        # ตัวเลือกและ Embed ที่ตรงกับตัวเลือก
        embed = discord.Embed(color=discord.Color.green())

        if option == "คำนวนสเตตัส":
            embed.title = "🧮 __**คำนวนสเตตัส**__"
            embed.description = "เครื่องมือคำนวณความเสียหายของทักษะในเกม Ragnarok Online ผู้เล่นสามารถปรับค่าสถานะ, อาวุธ, การ์ด, และอุปกรณ์ต่างๆ เพื่อดูผลลัพธ์ความเสียหายในแต่ละสถานการณ์ เหมาะสำหรับผู้ที่ต้องการวิเคราะห์และปรับปรุงการเล่นเกมให้มีประสิทธิภาพยิ่งขึ้น โดยเลือกใช้อุปกรณ์และทักษะที่เหมาะสมในการต่อสู้"
            embed.add_field(name="✨ Calculator", value="> ๐ [คลิกที่นี่](https://turugrura.github.io/tong-calc-ro-host/#/)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1286169799562362951/image_.png?ex=66ecee78&is=66eb9cf8&hm=58f1d74fe36c35c9a6ebe14afb13ed091b4ad3c025f2a8d394ff4ccac61f802e&=&format=webp&quality=lossless&width=1100&height=694')

        elif option == "แต่งตัว":
            embed.title = "🎎 __**แต่งตัว**__"
            embed.description = "เครื่องมือสำหรับเกม Ragnarok Online ที่ช่วยให้ผู้เล่นสามารถคำนวณและวางแผนการสวมใส่อุปกรณ์ของตัวละครได้อย่างมีประสิทธิภาพ"
            embed.add_field(name="✨ Costume", value="> ๐ [คลิกที่นี่](https://visual.runemidgarts.in.th)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1173912177585963048/1286167619061415936/image_.jpg?ex=66ecec70&is=66eb9af0&hm=d6f05ea4c4ee1cb3b7517d3962ada5bcac009641beb4d3231af04c4bc61aee9b&=&format=webp&width=1498&height=1136')

        elif option == "ดันเจี้ยน":
            embed.title = "⚔️ __**ดันเจี้ยน**__"
            embed.description = "รวบรวมเทคนิคในการลงดันเจี้ยนที่จำเป็น"
            embed.add_field(name="✨ Central Laboratory วิธีเปิดดันและวิธีลงดัน", value="> ๐ [วิธีเปิดดัน](https://www.youtube.com/watch?v=ah7S7s5EUwU&t=58s) & [วิธีลงดัน](https://www.whitebearz.com/simple-binary?fbclid=IwY2xjawEsVVRleHRuA2FlbQIxMAABHZN4gor8tWelBXPyLmBrE-SBOunsWi0UicDZ4f0Dy2Rnr0d-KIU_f3bPkQ_aem_QgokNXKsO2tOPRuhAVdmpg#google_vignette)", inline=False)
            embed.add_field(name="✨ ทำเควส 17.1 & 17.2", value="> ๐ [Patch 17.1 Illusion Part 1](https://www.youtube.com/watch?v=-ATOr0zNa7Q&t=161s)\n> ๐ [Patch 17.1 Illusion Part 2](https://www.youtube.com/watch?v=JlbFio3Zhjc)\n> ๐ [Patch 17.2 Legacy of the Wise One](https://www.youtube.com/watch?v=imnDhCpjaK0)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66e894a0&is=66e74320&hm=3f4adac5c6566b7f932b801e94eb50ce3290fc9f9412a412824846e056a024de&=&format=webp&quality=lossless&width=960&height=37')

        elif option == "คำสั่งและการแก้ไขภายในเกม":
            embed.title = "🎛 __**คำสั่งและการแก้ไขภายในเกม**__"
            embed.description = "รวบรวมเทคนิคคำสั่งภายในเกมที่เป็นประโยนช์ต่อผู้เล่น"
            embed.add_field(name="✨ __**คำสั่งภายในเกม**__", 
                            value="> ๐ `/mineffect`:\tลดหรือเปลี่ยน การแสดง Effect บางอย่าง เพื่อลดอาการกระตุกในการเล่น\n"
                            "> ๐ `/aura`:\tเปิด/ปิด การลดแสดงแสง Aura\n"
                            "> ๐ `/aura2`:\tเปิด/ปิด การแสดงแสง Aura\n"
                            "> ๐ `/fog`:\tเปิด/ปิด การแสดงหมอก\n"
                            "> ๐ `/quake`:\tเปิด/ปิด การแสดง Effect จอสั่น\n"
                            "> ๐ `/lightmap`:\tเปิด/ปิด การแสดง Effect เกียวกับแสงบนแผนที่\n"
                            "> ๐ `/zoom`:\tเปิด/ปิด ระดับการ Zoom เพิ่มเติมอีก 3 ช่อง\n"
                            "> ๐ `/skip`:\tถ้าค่าเป็น Off ตัวเกมจะพยายามแสดงทุก ๆ Frame ที่สามารถ Render ออกมาได้ ถ้าค่าเป็น On ตัวเกมจะข้ามบาง Frame ที่ Render ออกมา เพื่อจำกัด FPS ไว้"
                            , inline=False)
            embed.add_field(name="✨ __**วิธีแก้ไข Loading Screen จอดำค้างนาน**__", value="[ดูวิธีการแก้ไข](https://www.youtube.com/watch?v=07sHi-NsP18)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66e894a0&is=66e74320&hm=3f4adac5c6566b7f932b801e94eb50ce3290fc9f9412a412824846e056a024de&=&format=webp&quality=lossless&width=960&height=37')


        await ctx.respond(embed=embed, ephemeral=True)
        return

def setup(bot):
    bot.add_cog(HelpCommands(bot))
