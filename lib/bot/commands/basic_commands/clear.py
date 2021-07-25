from discord.ext.commands import command
from discord.ext import commands
from discord.ext.commands import has_permissions, bot_has_permissions
from tc import tc
import discord
from discord import Embed
from typing import Optional

class Clear(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @command(name="clear", aliases=["purge", "cls", "prg"],help="Clear the messages of a channel.")
    @bot_has_permissions(manage_messages=True)
    @has_permissions(manage_messages=True)
    async def clear_messages(self,ctx, limit: Optional[int] = 1):
        with ctx.channel.typing():
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=limit)
            if limit == 1:
                await ctx.send(f"Deleted {len(deleted):,} message.", delete_after=7)
            else:
                await ctx.send(f"Deleted {len(deleted):,} messages.", delete_after=7)
        
        
def setup(bot):
    bot.add_cog(Clear(bot))