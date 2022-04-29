import pyautogui as pag
import time, os, sys, random
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import autoclicker
import pyfiglet
from pyfiglet import Figlet
import colorama
from colorama import Fore
import socket
import portscanner
import concurrent.futures
import hashlib
import hashcrack
import ssl
import smtplib
import gmailbrute
import json
import requests
import iptracker
import discord
from discord.ext import commands, tasks
from itertools import cycle
import discordnuke
import argparse
import smtplib
import XXSdetector
colorama.init()

print(Fore.LIGHTRED_EX)
print('''                                                                                                                                                                                    
                                                                                                                                                                                      
                    MMMMMMMM               MMMMMMMM  iiii  kkkkkkkk                                      OOOOOOOOO                         lllllll                                                        
                    M:::::::M             M:::::::M i::::i k::::::k                                    OO:::::::::OO                       l:::::l                                                        
                    M::::::::M           M::::::::M  iiii  k::::::k                                  OO:::::::::::::OO                     l:::::l                                                        
                    M:::::::::M         M:::::::::M        k::::::k                                 O:::::::OOO:::::::O                    l:::::l                                                        
                    M::::::::::M       M::::::::::Miiiiiii  k:::::k    kkkkkkk eeeeeeeeeeee         O::::::O   O::::::Oxxxxxxx      xxxxxxx l::::l    ooooooooooo   nnnn  nnnnnnnn       ggggggggg   ggggg
                    M:::::::::::M     M:::::::::::Mi:::::i  k:::::k   k:::::kee:::::ab:::::::ee       O:::::O     O:::::O x:::::x    x:::::x  l::::l  oo:::::::::::oo n:::nn::::::::nn    g:::::::::ggg::::g
                    M:::::::M::::M   M::::M:::::::M i::::i  k:::::k  k:::::ke::::::eeeee:::::ee     O:::::O     O:::::O  x:::::x  x:::::x   l::::l o:::::::::::::::on::::::::::::::nn  g:::::::::::::::::g
                    M::::::M M::::M M::::M M::::::M i::::i  k:::::k k:::::ke::::::e     e:::::e     O:::::O     O:::::O   x:::::xx:::::x    l::::l o:::::ooooo:::::onn:::::::::::::::ng::::::ggggg::::::gg
                    M::::::M  M::::M::::M  M::::::M i::::i  k::::::k:::::k e:::::::eeeee::::::e     O:::::O     O:::::O    x::::::::::x     l::::l o::::o     o::::o  n:::::nnnn:::::ng:::::g     g:::::g 
                    M::::::M   M:::::::M   M::::::M i::::i  k:::::::::::k  e:::::::::::::::::e      O:::::O     O:::::O     x::::::::x      l::::l o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g 
                    M::::::M    M:::::M    M::::::M i::::i  k:::::::::::k  e::::::eeeeeeeeeee       O:::::O     O:::::O     x::::::::x      l::::l o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g 
                    M::::::M     MMMMM     M::::::M i::::i  k::::::k:::::k e:::::::e                O::::::O   O::::::O    x::::::::::x     l::::l o::::o     o::::o  n::::n    n::::ng::::::g    g:::::g 
                    M::::::M               M::::::Mi::::::ik::::::k k:::::ke::::::::e               O:::::::OOO:::::::O   x:::::xx:::::x   l::::::lo:::::ooooo:::::o  n::::n    n::::ng:::::::ggggg:::::g 
                    M::::::M               M::::::Mi::::::ik::::::k  k:::::ke::::::::eeeeeeee        OO:::::::::::::OO   x:::::x  x:::::x  l::::::lo:::::::::::::::o  n::::n    n::::n g::::::::::::::::g 
                    M::::::M               M::::::Mi::::::ik::::::k   k:::::kee:::::::::::::e          OO:::::::::OO    x:::::x    x:::::x l::::::l oo:::::::::::oo   n::::n    n::::n  gg::::::::::::::g 
                    MMMMMMMM               MMMMMMMMiiiiiiiikkkkkkkk    kkkkkkk eeeeeeeeeeeeee            OOOOOOOOO     xxxxxxx      xxxxxxxllllllll   ooooooooooo     nnnnnn    nnnnnn    gggggggg::::::g 
                                                                                                                                                                                                  g:::::g 
                                                                                                                                                                                       gggggg      g:::::g 
                                                                                                                                                                                      g:::::gg   gg:::::g 
                                                                                                                                                                                       g::::::ggg:::::::g 
                                                                                                                                                                                       gg:::::::::::::g  
                                                                                                                                                                                          ggg::::::ggg    
                                                                                                                                                                                             gggggg       ''')


print(Fore.LIGHTRED_EX)
print('                  -------------------------------------------------------------------------------------SESSION STARTED----------------------------------------------------------------------------------------- by Feciouss')

print(Fore.LIGHTMAGENTA_EX + '                                                                                      [!]---------Please wait while we start your toolbox Version 1.0.0 ---------')
print(Fore.LIGHTMAGENTA_EX)
print('                                                            [!]Join the M.O Discord Server for support, the latest updates and newest versions here ---> https://discord.gg/hMrJtWUZab')
time.sleep(3.65)
print('                                                                                     [$]<------Please Select An Application------>')
time.sleep(0.3)
print(Fore.MAGENTA)
print('''                                                                                     =================================================================
                                                                                     | 1)Autoclicker          10)Mail Brute Force                    |
                                                                                     | 2)DDoS Tool                                                   |
                                                                                     | 3)Port Scanner                                                |
                                                                                     | 4)MD5 Hash Cracker                                            |
                                                                                     | 5)Gmail brute Force                                           |
                                                                                     | 6)Creator Credits                                             |
                                                                                     | 7)IP Tracker                                                  |
                                                                                     | 8)Discord Server Nuker                                        |
                                                                                     | 9)XXS Detector                                                |
                                                                                     =================================================================''')                                       
print(Fore.GREEN)
program = input('                                                                              [$]What program would you like to use: ')
if program == '1':
    try:
      print('[!]---LOADING---')
      time.sleep(0.45)
      print('[1]<-----Autoclicker Started----->')
      print('[!]Press "z" key to start/stop the Autoclicker and press "x" to close/exit the program. if you need support join the M.O Discord Server --> https://discord.gg/hMrJtWUZab')
      autoclicker.autoclick()
    except:
      print('[!]<------Autoclicker Failed to start, Aborting------>')
      time.sleep(5)
      sys.exit
elif program == '2':
  try:
    print('[!]---LOADING---')
    time.sleep(0.783)
    print('Open the "Mike Oxlong Terminal" folder then open the "DDoS" folder and right click in empty space and press "Open in terminal" then run this command "python DDoS.py <IP> <THREADS> <TIME>" join the M.O Discord Server if you have any questions or need support here --> https://discord.gg/hMrJtWUZab')
    time.sleep(3.854)
    print('[!]-----CLOSING IN 1 MINUTE-----')
    time.sleep(60)
    sys.exit
  except:
    print('[!]DDoS Failed to start, Aborting')
    time.sleep(5)
    sys.exit
elif program == '3':
  try:
    print('[!]---LOADING---')
    time.sleep(1.34812)
    print('[!]Port Scanner Program Started')
    portscanner.portscan()
  except:
    print('[!]Failed to start Port Scanner Program, Closing')
    time.sleep(5)
    sys.exit
elif program == '4':
  print('[!]---LOADING---')
  time.sleep(2.5454)
  print('[!]MD5 Hash cracker started')
  hashcrack.crackhash()
elif program == '5':
  print('[!]---LOADING---')
  time.sleep(3.23435)
  print('[!]Gmail Brute Force program started')
  gmailbrute.gmailbrute()
elif program == '6':
  print('[!]---LOADING---')
  time.sleep(0.24564)
  print(Fore.GREEN + '[!]Program Made by ' + Fore.RED + 'F' + Fore.BLUE + 'e' + Fore.GREEN + 'c' + Fore.CYAN + 'i' + Fore.LIGHTMAGENTA_EX + 'o' + Fore.YELLOW + 'u' + Fore.LIGHTRED_EX + 's' + Fore.LIGHTGREEN_EX + 's' + Fore.BLUE + '#' + Fore.GREEN + '5' + Fore.YELLOW + '3' + Fore.LIGHTWHITE_EX + '1' + Fore.MAGENTA + '0')
  time.sleep(1.5)
  print('Project Started on ' + Fore.LIGHTBLUE_EX + '22/04/2022')
  time.sleep(1.5)
  print(Fore.LIGHTMAGENTA_EX + 'Join the M.O Discord Server if you have questions or need support https://discord.gg/hMrJtWUZab')
  time.sleep(1.5)
  print(Fore.RED + 'This program was made for and only for ETHICAL Hacking!')
  time.sleep(1.5)
  print('---WE ARE NOT HELD RESPONSIBLE FOR ANY DAMAGES CAUSED BY THIS PRODUCT---')
  time.sleep(1.5)
  print(Fore.GREEN + '-----RULES AND NOTICE-----')
  print(Fore.MAGENTA + 'This program was not made for attacking, it was made for ethical hacking and penetration testing.')
  print('We are not responsible for any damages caused with this product.')
  time.sleep(30)
  sys.exit
elif program == '7':
  print('[!]---LOADING---')
  time.sleep(2.5676853276)
  print('[!]Program Started')
  iptracker.iptrack()
elif program == '8':
  print('[!]---LOADING---')
  time.sleep(3.4156747574)
  print('[!]Program Started')
  discordnuke.nukeserver()
elif program == '9':
  print('[!]---LOADING---')
  time.sleep(1.234)
  print('[!]Program Started')
  XXSdetector.xxsdetect()
elif program == '10':
  print('[!]---LOADING---')
  time.sleep(0.6364)
  print('[!]To use the mailbrute open a cmd and change directory to the Mike Oxlong Terminal the run the cmd py mailbrute.py -h (Shows help on how to use)')




else:
  print('[!]<------Unrecognised Program Number, Aborting------>')
  time.sleep(5)
  sys.exit



