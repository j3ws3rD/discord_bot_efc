from typing import Optional
import discord
from discord import client
from discord import message
from discord.embeds import EmptyEmbed
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands.cog import Cog

continent_list = ["Asia", "North_America", "South_America",
                  "Africa", "Europe", "Antarctica", "Australia"]

countries_list = [
    "U.S",
    "U.K",
    "Canada",
    "Germany",
    "Australia",
    "Russia",
    "France",
    "India",
    "China",
    "Greece",
    "Finland",
    "Romania",
    "Israel",
    "Netherlands",
    "South_Africa",
    "Switzerland",
    "Ukraine",
    "Spain",
    "Sweden",
    "Italy"
]


class Get_Role(Cog):
    def __init__(self, bot):
        self.bot = bot

        async def remove_another_roles_prog(member,main_role,guild):
            prog_list = [
                "Python",
                "C",
                "C++",
                "Java",
                "HTML",
                "CSS",
                "Sass",
                "Javascript",
                "Kotlin",
                "Go",
                "Bash",
                "PHP",
                "Ruby",
                "Perl",
                "Scala",
                "Swift",
                "R"
            ]
            prog_list.remove(main_role)
            return_value = True
            for member_role in member.roles:
                if member_role.name in prog_list:
                    if member_role.name != main_role:
                        await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                        return_value = False
            print("Returning value..")
            return return_value

        @bot.event
        async def on_raw_reaction_add(payload):
            message_id = payload.message_id
            if message_id == 869465306156908574:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                if payload.emoji.name == "Asia":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name="Asia")

                elif payload.emoji.name == "NorthAmerica":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(
                            guild.roles, name="North_America")

                elif payload.emoji.name == "SouthAmerica":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(
                            guild.roles, name="South_America")

                elif payload.emoji.name == "Africa":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(guild.roles, name="Africa")

                elif payload.emoji.name == "Europe":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(guild.roles, name="Europe")

                elif payload.emoji.name == "Australia":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(guild.roles, name="Australia")

                elif payload.emoji.name == "Antarctica":
                    for member_role in member.roles:
                        if member_role.name in continent_list:
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869465306156908574)
                            for continent_message_reaction in continent_message.reactions:
                                if continent_message_reaction.emoji.name == member_role.name:
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))
                    else:
                        role = discord.utils.get(
                            guild.roles, name="Antarctica")

                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        await member.add_roles(role)
                        print("Done")
                    else:
                        print("Member not found.")

            elif message_id == 869617258018775100:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                if payload.emoji.name == "🇺🇸":
                    emoji = "🇺🇸"
                    con = "U.S"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name="U.S")

                elif payload.emoji.name == "🇬🇧":
                    emoji = "🇬🇧"
                    con = "U.K"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, con)

                elif payload.emoji.name == "🇨🇦":
                    emoji = "🇨🇦"
                    con = "Canada"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇩🇪":
                    emoji = "🇩🇪"
                    con = "Germany"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇦🇺":
                    emoji = "🇦🇺"
                    con = "Australia"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇷🇺":
                    emoji = "🇷🇺"
                    con = "Russia"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇫🇷":
                    emoji = "🇫🇷"
                    con = "France"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇮🇳":
                    emoji = "🇮🇳"
                    con = "India"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇨🇳":
                    emoji = "🇨🇳"
                    con = "China"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇬🇷":
                    emoji = "🇬🇷"
                    con = "Greece"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇫🇮":
                    emoji = "🇫🇮"
                    con = "Finland"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇷🇴":
                    emoji = "🇷🇴"
                    con = "Romania"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇮🇱":
                    emoji = "🇮🇱"
                    con = "Israel"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇳🇱":
                    emoji = "🇳🇱"
                    con = "Russia"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇿🇦":
                    emoji = "🇿🇦"
                    con = "South_Africa"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇨🇭":
                    emoji = "🇨🇭"
                    con = "Switzerland"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇺🇦":
                    emoji = "🇺🇦"
                    con = "Ukraine"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇪🇸":
                    emoji = "🇪🇸"
                    con = "Spain"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇸🇪":
                    emoji = "🇸🇪"
                    con = "Sweden"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name="U.S")

                elif payload.emoji.name == "🇮🇹":
                    emoji = "🇮🇹"
                    con = "Italy"
                    for member_role in member.roles:
                        if member_role.name in countries_list:
                            if member_role.name == con:
                                role = discord.utils.get(guild.roles, name=con)
                            else:
                                member = guild.get_member(payload.user_id)
                                await member.remove_roles(discord.utils.get(guild.roles, name=member_role.name))
                                roles_channel = await bot.fetch_channel(852113132208914432)
                                country_message = await roles_channel.fetch_message(869617258018775100)
                                for country_message_reaction in country_message.reactions:
                                    if country_message_reaction.emoji != emoji:
                                        await country_message.remove_reaction(country_message_reaction, member)
                    else:
                        role = discord.utils.get(guild.roles, name=con)

                if role is not None:
                    print("Role in not None")
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("Done")
                else:
                    print("Member not found.")

            elif message_id == 869660757690818611:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                if payload.emoji.name == "Boy":
                    print("Beep")
                    for member_role in member.roles:
                        print(member_role.name)
                        if member_role.name == "Girl":
                            print("Beep3")
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            gender_message = await roles_channel.fetch_message(869660757690818611)
                            await member.remove_roles(discord.utils.get(guild.roles, name="Girl"))
                            for gender_message_reaction in gender_message.reactions:
                                if gender_message_reaction.emoji.name == "Girl":
                                    await gender_message.remove_reaction(
                                        gender_message_reaction, member)
                        else:
                            print("fdsf")
                            role = discord.utils.get(guild.roles, name="Boy")
                            
                elif payload.emoji.name == "Girl":
                    print("Beep")
                    for member_role in member.roles:
                        if member_role.name == "Boy":
                            print("Beep3")
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            gender_message = await roles_channel.fetch_message(869660757690818611)
                            await member.remove_roles(discord.utils.get(guild.roles, name="Boy"))
                            for gender_message_reaction in gender_message.reactions:
                                if gender_message_reaction.emoji.name == "Boy":
                                    await gender_message.remove_reaction(
                                        gender_message_reaction, member)
                        else:
                            role = discord.utils.get(guild.roles, name="Girl")

                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("Done")
                else:
                    print("Member not found.")
                    
            elif message_id == 869697904690999326:
                print("mr.x")
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                roles_channel = await bot.fetch_channel(852113132208914432)
                prog_message = await roles_channel.fetch_message(869697904690999326)
                print(payload.emoji.name)
                    # Check if user have that main_role if not 
                if payload.emoji.name == "C_":
                    role = discord.utils.get(guild.roles,name="C")
                
                elif payload.emoji.name == "Cpp":
                    role = discord.utils.get(guild.roles,name="C++")

                elif payload.emoji.name == "R_":
                    role = discord.utils.get(guild.roles,name="R")
                
                else:
                    role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                
                # elif payload.emoji.name == "C_":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role="C",guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != "C_":
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name="C")
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name="C")
                    
                # elif payload.emoji.name == "Cpp":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role="C++",guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != "Cpp":
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name="C++")
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name="C++")
                        
                # elif payload.emoji.name == "Java":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "HTML":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "CSS":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Sass":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Javascript":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Kotlin":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Go":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Bash":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "PHP":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Ruby":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Scala":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "Swift":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                # elif payload.emoji.name == "R":
                #     # Check if user have that main_role if not 
                #     a = False
                #     a = await remove_another_roles_prog(member=member,main_role=payload.emoji.name,guild=guild)
                #     if a == False:  
                #         for prog_message_reaction in prog_message.reactions:
                #             if prog_message_reaction.emoji.name != payload.emoji.name:
                #                 await prog_message.remove_reaction(
                #                             prog_message_reaction, member)
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                        
                #     elif a == True:
                #         role = discord.utils.get(guild.roles,name=payload.emoji.name)
                    
                
                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("Done")
                else:
                    print("Member not found.")

        @bot.event
        async def on_raw_reaction_remove(payload):
            message_id = payload.message_id
            if message_id == 869465306156908574:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                if payload.emoji.name == "Asia":
                    role = discord.utils.get(guild.roles, name="Asia")

                elif payload.emoji.name == "North_America":
                    role = discord.utils.get(guild.roles, name="North_America")

                elif payload.emoji.name == "South_America":
                    role = discord.utils.get(guild.roles, name="South_America")

                elif payload.emoji.name == "Africa":
                    role = discord.utils.get(guild.roles, name="Africa")

                elif payload.emoji.name == "Europe":
                    role = discord.utils.get(guild.roles, name="Europe")

                elif payload.emoji.name == "Australia":
                    role = discord.utils.get(guild.roles, name="Australia")

                elif payload.emoji.name == "Antarctica":
                    role = discord.utils.get(guild.roles, name="Antarctica")

                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        await member.remove_roles(role)
                        print("Done")
                    else:
                        print("Member not found.")
                else:
                    print("Role not found.")

            elif message_id == 869617258018775100:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                if payload.emoji.name == "🇺🇸":
                    con = "U.S"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇬🇧":
                    con = "U.K"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇨🇦":
                    con = "Canada"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇩🇪":
                    con = "Germany"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇦🇺":
                    con = "Australia"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)
                elif payload.emoji.name == "🇷🇺":
                    con = "Russia"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇫🇷":
                    print("U.S")
                    con = "France"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇮🇳":
                    con = "India"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇨🇳":
                    con = "China"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇬🇷":
                    con = "Greece"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇫🇮":
                    con = "Finland"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇷🇴":
                    con = "Romania"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇮🇱":
                    con = "Israel"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇳🇱":
                    con = "Netherlands"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇿🇦":
                    con = "South_Africa"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇨🇭":
                    con = "Switzerland"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇺🇦":
                    con = "Ukraine"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇪🇸":
                    con = "Spain"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇸🇪":
                    con = "Sweden"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)

                elif payload.emoji.name == "🇮🇹":
                    con = "Italy"
                    for member_role in member.roles:
                        print(1)
                        if member_role.name == con:
                            print(2)
                            print(member_role.name)
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                member = guild.get_member(payload.user_id)
                                await continent_message.remove_reaction(continent_message_reaction, member)
                                await member.remove_roles(discord.utils.get(guild.roles, name=con))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name=con)
                elif payload.emoji.name == "🇮🇹":
                    print("Italy")
                    for member_role in member.roles:
                        print("FDS")
                        if member_role.name in countries_list:
                            print("1")
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            continent_message = await roles_channel.fetch_message(869617258018775100)
                            for continent_message_reaction in continent_message.reactions:
                                print(2)
                                if continent_message_reaction.emoji.name == member_role.name:
                                    print(3)
                                    member = guild.get_member(payload.user_id)
                                    await continent_message.remove_reaction(continent_message_reaction, member)
                                    print(continent_message_reaction.emoji.name)
                                    await member.remove_roles(discord.utils.get(guild.roles, name=continent_message_reaction.emoji.name))

                    else:
                        print("It should not ")
                        role = discord.utils.get(guild.roles, name="Italy")

                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    print("removing role.")
                    await member.remove_roles(role)
                else:
                    print("Member not found.")

            elif message_id == 869660757690818611:
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                if payload.emoji.name == "Boy":
                    print("Beep")
                    for member_role in member.roles:
                        if member_role.name == "Girl":
                            print("Beep3")
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            gender_message = await roles_channel.fetch_message(869660757690818611)
                            await member.remove_roles(discord.utils.get(guild.roles, name="Girl"))
                            for gender_message_reaction in gender_message.reactions:
                                if gender_message_reaction.emoji.name == "Girl":
                                    await gender_message.remove_reaction(
                                        gender_message_reaction, member)
                        else:
                            role = discord.utils.get(guild.roles, name="Boy")
                            
                elif payload.emoji.name == "Girl":
                    print("Beep")
                    for member_role in member.roles:
                        if member_role.name == "Boy":
                            print("Beep3")
                            roles_channel = await bot.fetch_channel(852113132208914432)
                            gender_message = await roles_channel.fetch_message(869660757690818611)
                            await member.remove_roles(discord.utils.get(guild.roles, name="Boy"))
                            for gender_message_reaction in gender_message.reactions:
                                if gender_message_reaction.emoji.name == "Boy":
                                    await gender_message.remove_reaction(
                                        gender_message_reaction, member)
                        else:
                            role = discord.utils.get(guild.roles, name="Girl")

                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print("Done")
                else:
                    print("Member not found.")

            elif message_id == 869697904690999326:
                print("mr.x")
                guild_id = payload.guild_id
                guild = discord.utils.find(
                    lambda g: g.id == guild_id, bot.guilds)
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members
                )
                roles_channel = await bot.fetch_channel(852113132208914432)
                prog_message = await roles_channel.fetch_message(869697904690999326)
                print(payload.emoji.name)
                    # Check if user have that main_role if not 
                if payload.emoji.name == "C_":
                    role = discord.utils.get(guild.roles,name="C")
                
                elif payload.emoji.name == "Cpp":
                    role = discord.utils.get(guild.roles,name="C++")

                elif payload.emoji.name == "R_":
                    role = discord.utils.get(guild.roles,name="R")
                
                else:
                    role = discord.utils.get(guild.roles,name=payload.emoji.name)
                
                
                if role is not None:
                    member = discord.utils.find(
                        lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print("Done")
                else:
                    print("Member not found.")
                    
                    

def setup(bot):
    bot.add_cog(Get_Role(bot))
