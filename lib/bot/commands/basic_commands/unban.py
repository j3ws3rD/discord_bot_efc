import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import command
from datetime import datetime
from discord.ext.commands import Greedy
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import MissingPermissions


class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @has_permissions(ban_members=True)
        @command(name="unban", help="Ban the discord member.(This command requires some special permissions.)")
        async def unban_members(ctx, *, members: str, reason: str = "For no reason."):
            ack_emb = False
            if members == None:
                await ctx.send(embed=Embed(title="Please specify user."))
            else:

                embed = Embed(title="Unban Report", colour=ctx.author.colour)
                print(await ctx.guild.bans())
                for ban_entry in await ctx.guild.bans():
                    user = ban_entry.user
                    print(members)
                    print(user.name) 
                    if (user.name == members):
                        ack_emb = True
                        await ctx.guild.unban(user)
                        embed.add_field(
                            name=f"{user} unbanned by user {ctx.author.display_name}.",value=f"{reason}.")
                        embed.set_thumbnail(url=user.avatar_url)
                        embed.set_footer(text=datetime.utcnow())
                if ack_emb:
                    await ctx.send(embed=embed)
                else:
                    embed = Embed(
                        title="Unban Report", description="User not found in ban entries.", colour=ctx.author.colour)
                    await ctx.send(embed=embed)
        self.bot.add_command(unban_members)
        
        @unban_members.error
        async def unban_members_error(ctx,error):
            if isinstance(error,MissingPermissions):
                await ctx.send("You do not have permission to unban any member of this server.")
            

def setup(bot):
    bot.add_cog(Unban(bot))
