from discord.ext.commands import command
from discord.ext import commands
import discord
from discord import Embed

class joinLeave(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        @bot.event
        async def on_ready():
            # print(tc.bright_green,"Bot is ready.",tc.reset)
            print("Bot is ready.")
        
        @bot.event
        async def on_member_join(member):
            embed = Embed(title=f"{member.display_name} joined.",description=f"Hello,{member.mention} welcome to trinity.Enjoy your stay.",colour=discord.Colour.light_grey())
            embed.set_thumbnail(url=member.avatar_url)
            await self.bot.get_channel(853506951774076938).send(embed=embed)
            
        @bot.event
        async def on_member_remove(member):
            embed = Embed(title=f"{member.display_name} got scared and leaved us.",colour=discord.Colour.orange())
            embed.set_thumbnail(url=member.avatar_url)
            await self.bot.get_channel(853506986737401876).send(embed=embed)
            
        
        
def setup(bot):
    bot.add_cog(joinLeave(bot))