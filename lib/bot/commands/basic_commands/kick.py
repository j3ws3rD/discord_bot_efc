import discord
from discord.embeds import Embed
from discord.errors import Forbidden
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands import has_role, has_permissions, bot_has_permissions
from datetime import datetime

from discord.ext.commands.errors import CommandInvokeError, MissingPermissions


class kick_m(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @has_permissions(kick_members=True)
    @command(name="kick", help="Kick the server member (This command requires some special permissions.)",aliases=["remove"])
    async def kick_(self,ctx, member: discord.Member = None, *, reason: str = "For no reason."):
        try:
            await member.kick()

        except MissingPermissions:
            await ctx.send("You do not have permission to kick any member of this server!")

        embed = Embed(
            title=f"{member.display_name} kicked by {ctx.author.display_name}", description=f"Reason: {reason}")
        embed.set_footer(text=datetime.utcnow())
        await ctx.send(embed=embed)

    @kick_.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to kick any member of this server!")

        elif CommandInvokeError:
            await ctx.send("Please specify the member tagname!")


def setup(bot):
    bot.add_cog(kick_m(bot))
