import discord
from discord.ext import commands
from discord import Option
from kafra_beta import GUILD_IDS

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=GUILD_IDS,
        name="ช่วยเหลือ",
        description="🔍 เลือกตัวเลือกที่คุณต้องการรับคำแนะนำ"
    )
    async def help_command(
        self, 
        ctx, 
        option: Option(str, "เลือกตัวเลือก", choices=["คำนวนสเตตัส", "แต่งตัว", "ดันเจี้ยน"], required=True)
    ):
        # ตัวเลือกและ Embed ที่ตรงกับตัวเลือก
        embed = discord.Embed(color=discord.Color.green())

        if option == "คำนวนสเตตัส":
            embed.title = "คำนวนสเตตัส"
            embed.description = "เครื่องมือคำนวณความเสียหายของทักษะในเกม Ragnarok Online ผู้เล่นสามารถปรับค่าสถานะ, อาวุธ, การ์ด, และอุปกรณ์ต่างๆ เพื่อดูผลลัพธ์ความเสียหายในแต่ละสถานการณ์ เหมาะสำหรับผู้ที่ต้องการวิเคราะห์และปรับปรุงการเล่นเกมให้มีประสิทธิภาพยิ่งขึ้น โดยเลือกใช้อุปกรณ์และทักษะที่เหมาะสมในการต่อสู้"
            embed.add_field(name="Calculator", value="[คลิกที่นี่](https://turugrura.github.io/tong-calc-ro-host/#/)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66e894a0&is=66e74320&hm=3f4adac5c6566b7f932b801e94eb50ce3290fc9f9412a412824846e056a024de&=&format=webp&quality=lossless&width=960&height=37')

        elif option == "แต่งตัว":
            embed.title = "แต่งตัว"
            embed.description = "เครื่องมือสำหรับเกม Ragnarok Online ที่ช่วยให้ผู้เล่นสามารถคำนวณและวางแผนการสวมใส่อุปกรณ์ของตัวละครได้อย่างมีประสิทธิภาพ"
            embed.add_field(name="Costume", value="[คลิกที่นี่](https://visual.runemidgarts.in.th)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66e894a0&is=66e74320&hm=3f4adac5c6566b7f932b801e94eb50ce3290fc9f9412a412824846e056a024de&=&format=webp&quality=lossless&width=960&height=37')

        elif option == "ดันเจี้ยน":
            embed.title = "ดันเจี้ยน"
            embed.description = "รวบรวมเทคนิคในการลงดันเจี้ยนที่จำเป็น"
            embed.add_field(name="Central Laboratory วิธีเปิดดันและวิธีลงดัน", value="[วิธีเปิดดัน](https://www.youtube.com/watch?v=ah7S7s5EUwU&t=58s) & [วิธีลงดัน](https://www.whitebearz.com/simple-binary?fbclid=IwY2xjawEsVVRleHRuA2FlbQIxMAABHZN4gor8tWelBXPyLmBrE-SBOunsWi0UicDZ4f0Dy2Rnr0d-KIU_f3bPkQ_aem_QgokNXKsO2tOPRuhAVdmpg#google_vignette)", inline=False)
            embed.add_field(name="ทำเควส 17.1 & 17.2", value="[Patch 17.1 Illusion Part 1](https://www.youtube.com/watch?v=-ATOr0zNa7Q&t=161s)\n[Patch 17.1 Illusion Part 2](https://www.youtube.com/watch?v=JlbFio3Zhjc)\n[Patch 17.2 Legacy of the Wise One](https://www.youtube.com/watch?v=imnDhCpjaK0)", inline=False)
            embed.set_image(url='https://media.discordapp.net/attachments/1119100375681736878/1276457703765708861/Screenshot_2567-08-23_at_15.26.39.png?ex=66e894a0&is=66e74320&hm=3f4adac5c6566b7f932b801e94eb50ce3290fc9f9412a412824846e056a024de&=&format=webp&quality=lossless&width=960&height=37')

        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(HelpCommands(bot))
