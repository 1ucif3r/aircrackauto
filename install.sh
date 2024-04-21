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

echo -e "${RED} "
echo ""                                                                         
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
echo -e "${RED}                                                      [!] This Tool Must Run As ROOT [!]${NC}\n"
echo ""
echo -e "${CYAN}[>] Press ENTER to Install AIRCRACKAUTO, CTRL+C to Abort.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/aircrackauto"
    BIN_DIR="$PREFIX/usr/bin/"
   # pkg install -y git python2
else
    INSTALL_DIR="/usr/share/doc/aircrackauto"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A Directory aircrackauto Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/1ucif3r/aircrackauto.git "$INSTALL_DIR";
echo "#!/bin/bash
python3 $INSTALL_DIR/aircrackauto.py" '${1+"$@"}' > aircrackauto;
chmod +x aircrackauto;
sudo cp aircrackauto /usr/bin/;
rm aircrackauto;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
        echo "[✔] Successfuly Installed !!! \n\n";
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]     ✔✔✔ Now Just Type In Terminal (aircrackauto) ✔✔✔         [+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
else
    echo "[✘] Installation Failed Do Properly Again NIGGA !!! [✘]";
    exit
fi
