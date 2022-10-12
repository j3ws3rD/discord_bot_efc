from logging import basicConfig
from os import path
from discord.ext import commands
from discord.ext.commands import command, Bot as BotBase
from glob import glob
from discord.ext.commands.converter import TextChannelConverter
from discord.ext.commands.errors import BadInviteArgument
from path import Path
import threading
from ..logger.loggers import takelogger
import discord

import os
# print("path")
# print(os.listdir())

class Bot(BotBase):
    def __init__(self):
        super().__init__(command_prefix="!",case_insensitive=True,intents=discord.Intents.all())
        self.remove_command("help")
        
        
        def load_basic_cogs(self):
            # basic cogs
            basic_cogs = [path.split("/")[4][:-3] for path in glob("lib/bot/events/basic_events/*")]
            print(basic_cogs)
            for cog in basic_cogs:
                if not cog.startswith("__"):
                    self.load_extension(f"lib.bot.events.basic_events.{cog}")
                    cog_log = takelogger("efc","basic_cog_thread",threading.get_ident())
                    cog_log.info(f"BASIC EVENTS {cog} LOADED.")
                    print("BASIC EVENTS %s loaded." % (cog))
        def load_debug_events(self):
            debug_events = [path.split("/")[4][:-3] for path in glob("lib/bot/events/debug_events/*")]
            print(debug_events)
            for debug_event in debug_events:
                if not debug_event.startswith("__"):
                    self.load_extension(f"lib.bot.events.debug_events.{debug_event}")
                    print("DEBUG EVENT %s LOADED." % debug_event)
        
        def load_user_events(self):
            user_events = [path.split("/")[4][:-3] for path in glob("lib/bot/events/user_events/*")]
            for user_event in user_events:
                if not user_event.startswith("__"):
                    self.load_extension(f"lib.bot.events.user_events.{user_event}")
                    print("USER EVENT %s LOADED." % user_event)

        def load_basic_commands(self):
            # basic cogs
            basic_commands = [path.split("/")[4][:-3] for path in glob("lib/bot/commands/basic_commands/*")]
            print(basic_commands)
            for commands in basic_commands:
                if not commands.startswith("__"):
                    self.load_extension(f"lib.bot.commands.basic_commands.{commands}")
                    general_log = takelogger("general","basic_commands_thread",threading.get_ident())
                    general_log.info(f"BASIC commands {commands} LOADED.")
                    print("BASIC COMMANDS %s loaded." % (commands))
                    
        def load_reddit_commands(self):
            reddit_commands = [path.split("/")[4][:-3] for path in glob("lib/bot/commands/reddit_commands/*")]
            print(reddit_commands)
            for reddit_command in reddit_commands:
                if not reddit_command.startswith("__"):
                    self.load_extension(f"lib.bot.commands.reddit_commands.{reddit_command}")
                    print("REDDIT COMMAND %s LOADED." %reddit_command)
    
        def load_music_commands(self):
            music_commands = [path.split("/")[4][:-3] for path in glob("lib/bot/commands/music_commands/*")]
            print(music_commands)
            for music_command in music_commands:
                if not music_command.startswith("__"):
                    self.load_extension(f"lib.bot.commands.music_commands.{music_command}")
                    print("MUSIC COMMAND %s LOADED." %music_command)

        def load_basic_tasks(self):
            basic_tasks = [path.split("/")[4][:-3] for path in glob("lib/bot/tasks/basic_tasks/*")]
            print(basic_tasks)
            for task in basic_tasks:
                if not task.startswith("__"):
                    self.load_extension(f"lib.bot.tasks.basic_tasks.{task}")
                    task_log = takelogger("task","basic_task_thread",threading.get_ident())
                    task_log.info("BASIC TASK {task} LOADED.")
                    
        basic_cog_thread = threading.Thread(target=load_basic_cogs,args=(self,),name="basicCog")
        basic_cog_thread.start()
        print("BAISIC COG THREAD created successfuly.")

        debug_event_thread = threading.Thread(target=load_debug_events,args=(self,), name="debug_event_thread")
        debug_event_thread.start()
        print("DEBUG EVENT THREAD created successfuly.")

        user_event_thread = threading.Thread(target=load_user_events,args=(self,),name="user_event_thread")
        user_event_thread.start()
        print("USER EVENT THREAD created successfuly.")

        basic_commands_thread = threading.Thread(target=load_basic_commands,args=(self,),name="basic_commands_thread")
        basic_commands_thread.start()
        print("BASIC COMMANDS THREAD created successfuly.")

        reddit_commands_thread = threading.Thread(target=load_reddit_commands,args=(self,),name="reddit_commands_thread")
        reddit_commands_thread.start()
        print("REDDIT COMMANDS THREAD created successfuly.")

        music_commands_thread = threading.Thread(target=load_music_commands,args=(self,),name="musice_command_thread")
        music_commands_thread.start()
        print('MUSIC COMMAND THREAD created successfuly.')
        
        basic_tasks_thread = threading.Thread(target=load_basic_tasks,args=(self,),name="basic_tasks_thread")
        basic_tasks_thread.start()
        print("BASIC TASKS THREAD created successfuly.")

    
    # music events
    

BOT = Bot()
