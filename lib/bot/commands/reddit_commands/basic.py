from discord.errors import HTTPException, NotFound
from discord.ext import commands
from discord.ext.commands.core import command
import praw
import aiohttp
import discord
from discord.ext.commands import Cog,command
import random
from discord.ext import commands

REDDIT_APP_ID = "A_pvXoSDWS2pSRHnj2JE6w"
REDDIT_APP_SECRET = "BBvkuqxXtDvuDGKSu1S7-kS2OYjJpA"
REDDIT_ENABLED_MEME_SUBREDDITS = [
    "funny",
    "memes",
    "wtf"
]

class Images(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID,client_secret=REDDIT_APP_SECRET,user_agent="efc_redit:%s:1.0" % REDDIT_APP_ID)
        
    @command()
    async def random(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit(subreddit).hot()
                post_to_pick = random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                    await ctx.send(submission.url)

                    

            else:
                await ctx.send("This is not working contact administrator.")
                
        # await ctx.send(",".join(args))
    @random.error
    async def random_error(self,ctx,error):
        await ctx.send(error.original)


def setup(bot):
    bot.add_cog(Images(bot))
    