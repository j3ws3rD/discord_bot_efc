import discord
from discord.embeds import Embed
from discord.ext import commands
import time
import datetime
from discord.ext.commands import command



class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(anme="ping", help="Ping command latency of discord api websocket.")
    async def ping(self,ctx):
        before = time.monotonic()
        message = await ctx.send("Ping message please ignore.", delete_after=2)
        ping = (time.monotonic() - before) * 1000
        embed = Embed(
            title="Ping", description=f"{ping:.0f}ms", colour=ctx.author.colour)
        await ctx.send(embed=embed)
    
    # self.bot.add_command(ping)
        
def setup(bot):
    bot.add_cog(Ping(bot))
