from aiohttp.client_exceptions import ServerDisconnectedError
from discord.ext.commands import command
from discord.ext import commands
from tc import tc
import discord
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import tasks
import asyncio
from apscheduler.triggers.cron import CronTrigger
import schedule

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class Bump(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()

        async def send_d_bump():
            print("I, I am running.")
            embed = Embed(title="E.F.C Interface",description=f"Send the `!d bump` command to bump the server.")
            await self.bot.get_channel(852112995563864085).send(embed=embed)

        self.scheduler.add_job(send_d_bump,"interval",seconds=10)
        self.scheduler.start()

def setup(bot):
    bot.add_cog(Bump(bot))