import discord
import wavelink
from discord.ext import commands
from discord.ext.commands import bot, command
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class Player(wavelink.Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class Music(commands.Cog, wavelink.WavelinkMixin):
    def __init__(self, bot):
        self.bot = bot
        self.wavelink = loop.run_until_complete(wavelink.Client(bot=bot))
        self.bot.loop.create_task(self.start_nodes())
    
    
    # We need some listeners for lavalink.
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.bot and after.channel is None:
            if not [m for m in before.channel.members if not m.bot]:
                pass # Disconnect the bot from the channel.
    
    
    @wavelink.WavelinkMixin.listener()
    async def on_node_ready(self, node):
        # server has nodes and we need to connect to one of these nodes.
        print(f"Connected with node '{node.identifer}' ready.")

    async def cog_check(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Music commands are not available in DMs.")
            return False
        
        return True
    
    async def start_nodes(self):
        await self.bot.wait_until_ready()

        nodes = {
            "MAIN": {
                "host": "127.0.0.1",
                "port": 2333,
                "rest_uri": "http://127.0.0.1:2333",
                "password": "youshallnotpass",
                "identifier": "MAIN",
                "region": "us_central"
            }
        }
        
        for node in  nodes.values():
            await self.wavelink.initiate_node(**node)
        
    def get_player(self, obj):
        if isinstance(obj, commands.Context):
            return self.wavelink.get_player(obj.guild.id, cls=Player, context=obj)
        
        elif isinstance(obj, discord.Guild):
            return self.wavelink.get_player(obj.id, cls=Player)

    
def setup(bot):
    bot.add_cog(Music(bot))