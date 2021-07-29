import discord
from discord.ext import commands
from discord.ext.commands import command
import random


class Loli(commands.Cog):
    def __init(self, bot):
        self.bot = bot
        self.loliLi = ["20210613_211228.jpg"
                "20210707_182541.jpg"
                "20210713_184922.jpg"
                "20210713_234616.jpg"
                "Buddah-the-Cat-MAIN.jpg"
                "C5ovUWkVMAAMhc0.jpg"
                "CAwtgxeM2Sc_d6eb54d9c0f873134bd4b51956834f39.jpg"
                "Dneb27e7b3.jpg"
                "E2xqwLxXMAIMvxL.jpg"
                "E3wf9gFVUAQN0yA.jpg"
                "Hcdrhve24ubf4.jpg"
                "Hvrgjbd57he2.jpg"
                "IMG_20210402_130922_201.jpg"
                "IMG_20210525_080040_262.jpg"
                "IMG_20210603_202239_883.jpg"
                "Meow-Mix_cat-food-dry.png"
                "Tdee35bbyjcwd.jpg"
                "Ugfecgbf44h.jpg"
                "Wu3g37rvej27egrn.jpg"
                "bhjedvuy.jpg"
                "c6b849184ec191c59bb75ee2468f1d0a.webp"
                "cat.jpg"
                "cat_gif.0.gif"
                "cats_tail_giphy_3dwiggle.gif"
                "cutest-kitten-gifs-massage.gif"
                "diona__klee__qiqi_by_urgentcoffee_dea9dcr-fullview.jpg"
                "e8e7fcf46f1e2fb9368e099da0c5b5d9.gif"
                "funny-cat-gifs-162-02.gif"
                "funny-cat.jpeg"
                "iiiiiii.jpg"
                "ilya-kuvshinov-img-5458.jpg"
                "im-a-nigger.jpg"
                "jodbehvu3.jpg"
                "seriouscatcover.jpg"
                "uwu.jpg"
                "uwuwuuwu.jpg"
                "wp6554107.jpg"]

    @command(name="loli", help="Random Loli's")
    async def loli(self,ctx):
        loli_one = random.choice(self.loliLi)
        await ctx.send("https://media.koolkidzklub.net/images/api/{}".format(loli_one))


def setup(bot):
    bot.add_cog(Loli(bot))
