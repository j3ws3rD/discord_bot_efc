import discord
from discord.ext import commands
from discord.embeds import Embed
from discord.ext.commands import command
from discord.ext.commands.cog import Cog
from discord.ext.menus import ListPageSource, Menu, MenuPages
from discord.utils import get
from typing import Optional, ValuesView

def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key,value in command.params.items():
        if key not in ("self","ctx",):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")
    params = " ".join(params)
    return f"```{cmd_and_aliases} {params}```"

class HelpMenu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx
        
        super().__init__(data,per_page=5)
    
    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)
        
        embed = Embed(title="Help",
                      description="This is help command for Helping You <3.",
                      colour=self.ctx.author.colour
                      )
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, commands):
        fields = []

        for command in commands:
            fields.append((syntax(command),command.help or "No description."))
        
        return await self.write_page(menu, fields)

class Help(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.remove_command("help")

    
    async def cmd_help(self, ctx, command):
        embed = Embed(title=f"Help with `{command}`",
                        description=syntax(command),
                        colour=ctx.author.colour
                      )
        embed.add_field(name="Command description", value=command.help)
        await ctx.send(embed=embed)
    
    @command(name="help",help="Show this help menu",case_insensitive=True)
    async def show_help(self,ctx, cmd: Optional[str]):
        if cmd is None:
            menu = MenuPages(source=HelpMenu(ctx,list(self.bot.commands)),
                                clear_reactions_after=True,
                                delete_message_after=True,
                                timeout=60.0
                             )
            await menu.start(ctx,)
        
        else:
            if (command := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)
            else:
                await ctx.send(embed=Embed(title="Command doesn't exist.",colour=ctx.author.colour))

def setup(bot):
    bot.add_cog(Help(bot))