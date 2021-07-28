from threading import Event
import discord
from discord.ext import commands
from discord.ext.commands import command

class Err_hnd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        @bot.event
        async def on_error(event,err):
            print(event)
            print(err)
            
        @bot.event
        async def on_command_error(ctx,error):
            await ctx.send(str(ctx.message.content[1:]) + " doesn't exist.")
            await ctx.send(error)
        


def setup(bot):
    bot.add_cog(Err_hnd(bot))