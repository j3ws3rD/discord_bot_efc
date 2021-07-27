import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import command,Greedy
from discord.ext.commands.core import has_permissions
from datetime import datetime
from discord.embeds import Embed

class Ban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
        @has_permissions(ban_members=True)
        @command(name="ban",help="Ban the discord member (This commmadn requires some special permissions.")
        async def ban_members(ctx, member: Greedy[discord.Member],*, reason: str = "For no reason."):
            for memberg in member:
                if ctx.author == memberg:
                    await ctx.send("You can't ban yourself.")
                else:
                    await member.ban()
                    embed = Embed(title="Ban report",colour=ctx.author.colour)
                    embed.add_field(name=f"{member.display_name} banned by {ctx.author.display_name}.",value=f"Reason: {reason}.")
                    embed.set_thumbnail(url=member.avatar_url)

            embed.set_footer(text=datetime.now())
            await ctx.send(embed=embed)
        self.bot.add_command(ban_members)
        # @ban_members.error
        # async def ban_members

        @command(name="flag")
        async def show_flag(ctx):
            # embed = discord.Embed(title="Gender",description="Choose your Gender and react on it.",color=4901375)
            # embed.add_field(name="\u200b", value="<:Boy:869295341160267846> Boy")
            # embed.add_field(name="\u200b", value="<:Girl:869295729095639090> Girl")
            # message = await ctx.send(embed=embed)
            # await message.add_reaction("<:Boy:869295341160267846>")
            # await message.add_reaction("<:Girl:869295729095639090>")
            embed = Embed(title="Programming Languages",description="Select your favourite programming langauge/languages.",colour=1587962)
            embed.add_field(name="\u200b", value="<:Python:869262242158362696> Python")
            embed.add_field(name="\u200b", value="<:C_:869262884629262336> C")
            embed.add_field(name="\u200b", value="<:Cpp:869261956631126178> C++")
            embed.add_field(name="\u200b", value="<:Java:869262510065352754> Java")
            embed.add_field(name="\u200b", value="<:HTML:869263114862997544> HTML")
            embed.add_field(name="\u200b", value="<:CSS:869263280605118494> CSS")
            embed.add_field(name="\u200b", value="<:Sass:869264118417326121> Sass")
            embed.add_field(name="\u200b", value="<:Javascript:869262706467819560> Javascript")
            embed.add_field(name="\u200b", value="<:Kotlin:869263981452353536> Kotlin")
            embed.add_field(name="\u200b", value="<:Go:869263839844241418> Go")
            embed.add_field(name="\u200b", value="<:Bash:869264427835351100> Bash")
            embed.add_field(name="\u200b", value="<:PHP:869680480646225990> PHP")
            embed.add_field(name="\u200b", value="<:Ruby:869680626473791559> Ruby")
            embed.add_field(name="\u200b", value="<:Perl:869680676163706920> Perl")
            embed.add_field(name="\u200b", value="<:Scala:869680521544859708> Scala")
            embed.add_field(name="\u200b", value="<:Swift:869680596220252222> Swift")
            embed.add_field(name="\u200b", value="<:R_:869680548338077746> R")
            message = await ctx.send(embed=embed)
            programming_languages = [
                "<:C_:869262884629262336>",
                "<:Cpp:869261956631126178>",
                "<:Java:869262510065352754>",
                "<:HTML:869263114862997544>",
                "<:CSS:869263280605118494>",
                "<:Sass:869264118417326121>",
                "<:Javascript:869262706467819560>",
                "<:Kotlin:869263981452353536>",
                "<:Go:869263839844241418>",
                "<:Bash:869264427835351100>",
                "<:PHP:869680480646225990>",
                "<:Ruby:869680626473791559>",
                "<:Perl:869680676163706920>",
                "<:Scala:869680521544859708>",
                "<:Swift:869680596220252222>",
                "<:R_:869680548338077746>"
            ]
            await message.add_reaction("<:Python:869262242158362696>")
            for programming_langauge in programming_languages:
                await message.add_reaction(programming_langauge)

            # embed=discord.Embed(title="Country", description="Choose your country and react on this message.", color=1552347)
            # embed.add_field(name="\u200b", value=":flag_us: United States(U.S)", inline=True)
            # embed.add_field(name="\u200b", value=":flag_gb: United Kindom", inline=True)
            # embed.add_field(name="\u200b", value=":flag_ca: Canada", inline=True)
            # embed.add_field(name="\u200b", value=":flag_de: Germany", inline=True)
            # embed.add_field(name="\u200b", value=":flag_au: Australia", inline=True)
            # embed.add_field(name="\u200b", value=":flag_ru: Russia", inline=True)
            # embed.add_field(name="\u200b", value=":flag_fr: France", inline=True)
            # embed.add_field(name="\u200b", value=":flag_in: India", inline=True)
            # embed.add_field(name="\u200b", value=":flag_cn: China", inline=True)
            # embed.add_field(name="\u200b", value=":flag_gr: Greece", inline=True)
            # embed.add_field(name="\u200b", value=":flag_fi: Finland", inline=True)
            # embed.add_field(name="\u200b", value=":flag_ro: Romania", inline=True)
            # embed.add_field(name="\u200b", value=":flag_il: Israel", inline=True)
            # embed.add_field(name="\u200b", value=":flag_nl: Netherlands", inline=True)
            # embed.add_field(name="\u200b", value=":flag_za: South Africa", inline=True)
            # embed.add_field(name="\u200b", value=":flag_ch: Switzerland", inline=True)
            # embed.add_field(name="\u200b", value=":flag_ua: Ukraine" , inline=True)
            # embed.add_field(name="\u200b", value=":flag_es: Spain" , inline=True)
            # embed.add_field(name="\u200b", value=":flag_se: Sweden" , inline=True)
            # embed.add_field(name="\u200b", value=":flag_it: Italy" , inline=True)
            # message = await ctx.send(embed=embed)
            # await message.add_reaction("🇺🇸")
            # await message.add_reaction("🇬🇧")
            # await message.add_reaction("🇨🇦")
            # await message.add_reaction("🇩🇪")
            # await message.add_reaction("🇦🇺")
            # await message.add_reaction("🇷🇺")
            # await message.add_reaction("🇫🇷")
            # await message.add_reaction("🇮🇳")
            # await message.add_reaction("🇨🇳")
            # await message.add_reaction("🇬🇷")
            # await message.add_reaction("🇫🇮")
            # await message.add_reaction("🇷🇴")
            # await message.add_reaction("🇮🇱")
            # await message.add_reaction("🇳🇱")
            # await message.add_reaction("🇿🇦")
            # await message.add_reaction("🇨🇭")
            # await message.add_reaction("🇺🇦")
            # await message.add_reaction("🇪🇸")
            # await message.add_reaction("🇸🇪")
            # await message.add_reaction("🇮🇹")
            
            # reactions = [""]
            # for reaction in reactions:
            # await message.add_reaction()
            # embed = discord.Embed(title="Region",description="Choose your region and react on it .",colour=15728639)
            # embed.add_field(name="\u200b", value="<:Asia:869448636055052298> Asia", inline=True)
            # embed.add_field(name="\u200b",value="<:Africa:869449191116660736> Africa")
            # embed.add_field(name="\u200b",value="<:Europe:869448837717172274> Europe")
            # embed.add_field(name="\u200b",value="<:Australia:869453694838665226> Australia")
            # embed.add_field(name="\u200b",value="<:NorthAmerica:869449485430980648> North America")
            # embed.add_field(name="\u200b",value="<:SouthAmerica:869450033307721759> South America")
            # embed.add_field(name="\u200b",value="<:Antarctica:869450400250613770> Antarctica")
            # message = await ctx.send(embed=embed)
            # reactions = ["<:Asia:869448636055052298>","<:Africa:869449191116660736>","<:Europe:869448837717172274>","<:Australia:869453694838665226>","<:NorthAmerica:869449485430980648>","<:SouthAmerica:869450033307721759>","<:Antarctica:869450400250613770>"]
            # for reaction in reactions:
            #     await message.add_reaction(reaction)
        self.bot.add_command(show_flag)
def setup(bot):
    bot.add_cog(Ban(bot))