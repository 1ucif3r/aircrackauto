#!/bin/bash

set -e

clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[96m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'

clear

counter=0
(

while :
do
cat <<EOF
XXX
$counter
Loading AIRCRACKAUTO INSTALLER ....( $counter%):
XXX
EOF

(( counter+=20 ))
[ $counter -eq 100 ] && break

sleep 1
done
) |
whiptail --title " AIRCRACKAUTO " --gauge "Please wait" 7 70 0



clear

echo -e "${RED}                                                                "                                                                                  
echo "                                                                                                              ";
echo "  █████  ██ ██████   ██████ ██████   █████   ██████ ██   ██  █████  ██    ██ ████████  ██████           ";  
echo " ██   ██ ██ ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ██   ██ ██    ██    ██    ██    ██          ";
echo " ███████ ██ ██████  ██      ██████  ███████ ██      █████   ███████ ██    ██    ██    ██    ██          ";  
echo " ██   ██ ██ ██   ██ ██      ██   ██ ██   ██ ██      ██  ██  ██   ██ ██    ██    ██    ██    ██          ";
echo " ██   ██ ██ ██   ██  ██████ ██   ██ ██   ██  ██████ ██   ██ ██   ██  ██████     ██     ██████   V2.0    "; 
echo "                                                                                 ";
echo "                                                             Welcome To AIRCRACKAUTO Installer          ";
echo -e "${GREEN}==============================================================================================${NC} "                                                                                                                                                                                                                          
echo -e "${BLUE}           www.dark4rmy.in | Instagram.com/0x1ucif3r | Github.com/aircrackauto ${NC}"
echo -e "${GREEN}==============================================================================================${NC}          "
echo -e "${RED}                                                            [!] This Tool Must Run As ROOT [!]${NC}\n"
echo -e ${CYAN}                 "Choose an Option : \n"
echo -e "${ORANGE}              [1] Kali Linux "
echo -e "${ORANGE}              [0] Exit "
echo "                                                 "
echo -n -e " ${GREEN}Aircrackauto >> ${NC}"
read choice
INSTALL_DIR="/usr/share/doc/aircrackauto"
BIN_DIR="/usr/bin/"
if [ $choice == 1 ] || [ $choice == 2 ]; then
	echo "[*] Checking Your Internet Connection .."
	wget -q --tries=10 --timeout=20 --spider https://google.com
	if [[ $? == 0 ]]; then
        echo -e ${BLUE}"[✔] Loading ... "
        if [ $choice == 1 ]; then
            #sudo apt-get update -y && apt-get upgrade -y
            #sudo apt-get install python3-pip -y
        
        fi

	    echo "[✔] Checking directories..."
	    if [ -d "$INSTALL_DIR" ]; then
	        echo "[!] A Directory aircrackauto Was Found.. Do You Want To Replace It ? [y/n]:" ;
	        read input
	        if [ "$input" = "y" ]; then
	            sudo rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi

        echo "[✔] Installing ...\n";
        sudo git clone https://github.com/1ucif3r/aircrackauto.git "$INSTALL_DIR";
        echo "#!/bin/bash
        python3 $INSTALL_DIR/aircrackauto.py" '${1+"$@"}' > aircrackauto;
        sudo chmod +x aircrackauto;
        sudo cp aircrackauto /usr/bin/ && rm aircrackauto;

        echo "\n[✔] Trying to installing Requirements ..."
        if [ $choice == 1 ]; then
            sudo sudo pip3 install pystyle
            sudo apt-get install -y aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite 
        
        fi

	else
		  echo -e $RED "Please Check Your Internet Connection and try again ..!!"
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "[✔] Successfuly Installed !!! \n\n";
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]     ✔✔✔ Now Just Type In Terminal (aircrackauto) ✔✔✔       [+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo -e $RED "[✘] Installation Failed Do Properly Again NIGGA !!! [✘]"
        exit
    fi
elif [ $choice == 0 ] && [ $choice != 1 ] && [ $choice != 2 ]; then 
    echo -e $RED "[✘] THank Y0u for Using Aircrackauto !! [✘] "
    exit
else
    echo -e $RED "[!] Select a Valid Option and Try Again [!]"
fi
