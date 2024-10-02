import discord
from discord.ext import commands
import asyncio

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_poll = False  # Flag สำหรับตรวจสอบว่าโพลมีอยู่หรือไม่

    @commands.command(name="poll")
    async def create_poll(self, ctx, duration: int, question: str, *, options: str):
        # เช็คว่าโพลกำลังดำเนินการอยู่หรือไม่
        if self.active_poll:
            return  # ออกจากฟังก์ชันโดยไม่แสดงข้อความใด ๆ

        options_list = options.split(';')

        if len(options_list) < 2:
            await ctx.send("คุณต้องใส่ตัวเลือกอย่างน้อย 2 ตัวเลือก")
            return
        if len(options_list) > 10:
            await ctx.send("คุณสามารถเพิ่มตัวเลือกได้สูงสุด 10 ตัวเลือก")
            return

        # แยก emoji และตัวเลือก
        emojis = []
        for option in options_list:
            parts = option.split('[')  # แบ่งตัวเลือกออกเป็นส่วนๆ
            if len(parts) == 2:
                emoji = parts[1].strip().rstrip(']')  # แยกเอา emoji ออก
                option_text = parts[0].strip()  # ข้อความตัวเลือก
                emojis.append(emoji)
                options_list[options_list.index(option)] = option_text  # อัปเดตตัวเลือก
            else:
                await ctx.send("กรุณาใช้รูปแบบ: ตัวเลือก [emoji] เช่น 'ตัวเลือก 1 [👍]; ตัวเลือก 2 [❤️]'")
                return

        # เช็คว่า emoji ที่กำหนดมีจำนวนมากกว่าตัวเลือกหรือไม่
        if len(emojis) < len(options_list):
            await ctx.send("คุณมีตัวเลือกมากกว่า emoji ที่สามารถใช้ได้")
            return

        # ตั้งค่า flag ว่ามีโพลอยู่
        self.active_poll = True

        # สร้าง embed สำหรับโพล
        embed = discord.Embed(
            title=f"📊 {question} 📊",
            description=f"เลือกตัวเลือกของคุณโดยคลิกที่ reaction ด้านล่าง!\n\nเวลานับถอยหลัง: {duration} วินาที",
            color=discord.Color.blue()
        )

        # เพิ่มตัวเลือกลงใน embed โดยใช้ emoji ที่กำหนด
        for i, option in enumerate(options_list):
            embed.add_field(name=f"{emojis[i]}", value=f"{option.strip()}", inline=True)

        # เพิ่มข้อมูลผู้สร้างโพล
        embed.set_footer(text=f"สร้างโดย {ctx.author.display_name}")

        # ส่งข้อความ @everyone พร้อม embed
        poll_message = await ctx.send(content="@everyone", embed=embed)

        # เพิ่ม reaction สำหรับตัวเลือกที่ใช้ emoji
        for emoji in emojis:
            await poll_message.add_reaction(emoji)

        # นับถอยหลัง
        await asyncio.sleep(duration)

        # ดึงข้อมูลการโหวตหลังจากหมดเวลา
        poll_message = await ctx.channel.fetch_message(poll_message.id)
        reaction_counts = {emoji: 0 for emoji in emojis}

        for reaction in poll_message.reactions:
            if reaction.emoji in reaction_counts:
                reaction_counts[reaction.emoji] = reaction.count - 1

        # สร้าง embed สำหรับผลโหวต
        result_embed = discord.Embed(
            title=f"📊 ผลลัพธ์โพล: {question} 📊",
            description=f"นี่คือผลลัพธ์จากการโหวตของคุณ",
            color=discord.Color.green()
        )

        for i, option in enumerate(options_list):
            result_embed.add_field(
                name=f"{emojis[i]} {option.strip()}",
                value=f"ผลโหวต: {reaction_counts[emojis[i]]} ครั้ง",
                inline=False
            )

        await ctx.send(embed=result_embed)

        # รีเซ็ต flag เพื่อให้สามารถสร้างโพลใหม่ได้
        self.active_poll = False

    @create_poll.error
    async def create_poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("กรุณาระบุคำถาม, ตัวเลือก และระยะเวลาในการสร้างโพลของคุณในรูปแบบ: `!poll <ระยะเวลา (วินาที)> <คำถาม> <ตัวเลือก 1 [emoji]; ตัวเลือก 2 [emoji]>`")
        else:
            await ctx.send(f"เกิดข้อผิดพลาด: {str(error)}")

def setup(bot):
    bot.add_cog(Poll(bot))
