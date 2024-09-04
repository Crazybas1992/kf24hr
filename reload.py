# ==================== Import Statements ====================
import os
from discord.ext import commands
from discord.commands import slash_command
from kafra import GUILD_IDS  # นำเข้าตัวแปร GUILD_IDS จาก kafra.py

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_IDS,
        description="🔄 Reload คำสั่งทั้งหมด"
    )
    @commands.has_permissions(administrator=True)  # อนุญาตเฉพาะผู้ดูแลระบบ
    async def reload(self, ctx):
        await ctx.defer(ephemeral=True)  # ซ่อนการตอบสนองในแชท
        try:
            for file in os.listdir('./cogs'):
                if file.endswith('.py'):
                    self.bot.reload_extension(f'cogs.{file[:-3]}')
            await ctx.respond("รีโหลดคำสั่งทั้งหมดเสร็จสิ้น!", ephemeral=True)
        except Exception as e:
            await ctx.respond(f"เกิดข้อผิดพลาด: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Reload(bot))
