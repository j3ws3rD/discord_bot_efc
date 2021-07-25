import discord
from discord.ext import commands
from discord.ext.commands import command,Greedy
from discord.ext.commands.core import has_permissions
from datetime import datetime
from discord.embeds import Embed

class Ban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
        @has_permissions(ban_members=True)
        @command(name="ban",help="Ban the discord member (This commmadn requires some special permissions.")
        async def ban_members(ctx, member: Greedy[discord.Member],*, reason: str = "For no reason."):
            for memberg in member:
                if ctx.author == memberg:
                    await ctx.send("You can't ban yourself.")
                else:
                    await member.ban()
                    embed = Embed(title="Ban report",colour=ctx.author.colour)
                    embed.add_field(name=f"{member.display_name} banned by {ctx.author.display_name}.",value=f"Reason: {reason}.")
                    embed.set_thumbnail(url=member.avatar_url)

            embed.set_footer(text=datetime.now())
            await ctx.send(embed=embed)
        self.bot.add_command(ban_members)
        # @ban_members.error
        # async def ban_members

def setup(bot):
    bot.add_cog(Ban(bot))