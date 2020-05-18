import os
import sys
import random
import socket



def logo():
    print("""\033[33m
    Made by
                    \033[32m        
       /\  | |\ | \_/ 
      \033[31m/--\ | | \| / \ 
\033[37m
███╗   ███╗ █████╗ ██████╗ ████████╗
████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║███████║██████╔╝   ██║   \033[35m
██║╚██╔╝██║██╔══██║██╔══██╗   ██║   
██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
       \033[31mMyanmar Anonymous       \033[32m▇◤▔▔▔▔▔▔▔◥▇
       \033[31mRecovery Team           \033[32m▇▏\033[31m◥▇◣┊◢▇◤\033[32m▕▇
                               \033[32m▇▏\033[31m▃▆▅▎▅▆▃\033[32m▕▇
          \033[34mEverything           \033[32m▇▏\033[31m╱▔▕▎▔▔╲\033[32m▕▇
                               \033[32m▇◣◣\033[31m▃▅▎▅▃\033[32m◢◢▇
             \033[334mis                \033[32m▇▇◣\033[31m◥▅▅▅◤\033[32m◢▇▇
                               \033[32m▇▇▇◣\033[31m╲▇╱\033[32m◢▇▇▇
          \033[34mTemporary            \033[32m ▇▇▇◣\033[31m▇\033[32m◢▇▇▇

    """)
def menu():
    os.system("clear")
    logo()
    print(""" 
                    \033[32mHackcat Tool
            \033[31mMyanmar Anonymous Recovery Team
    \033[0;33m(1) Text editor
    \033[1;34m(2) Programming
    \033[0;35m(3) Scan
    \033[0;32m(4) Web Server
    \033[0;31m(5) Web Hacking
    \033[0;36m(6) Exploit and The best Hacking Tools
    \033[1;34m(7) Password Hash
    \033[1;37m(8) Exit""")
    try:
     a=eval(input("\033[31mMART\033[33m=\033[32m=\033[37m>"))
     if a==1:

      text()

     elif a==2:
       pro()
     elif a==3:
         scan()
     elif a==4:
        web()
     elif a==5:
        wh()
     elif a==6:
      dev()
     elif a==7:
       pwhash()
     elif a==8:
        os.system("clear")
        exit()
     else:
        os.system("clear")
        menu()
    except ValueError:
         print("Please Enter Number")

def text():
    os.system("clear")
    logo()
    print("""   \033[0;31m          Code editor 
         \033[0;31m(1) nano
         \033[0;32m(2) vim
         \033[0;33m(3) Webidle
         \033[0;34m(4) micro 
         \033[0;35m(5) neovim
         \033[0;36m(6) emacs
         \033[0;37m(7) jupp
         \033[0;33m(8) Main Menu
         \033[0;34m(00) Exit""")
    try:
      a = int(input("\033[31mMART\033[33m=\033[32m=\033[37m>"))
      if a == 1:
          nano()
      elif a == 2:
          vim()
      elif a == 3:
        webidle()
      elif a == 4:
        micro()
      elif a == 5:
        neovim()
      elif a == 6:
        emacs()
      elif a == 7:
        jupp()
      elif a == 8:
        os.system("clear")
        menu()
      elif a== 00:
        os.system("clear")
        exit()
      else:
        os.system("clear")
        text()
    except ValueError:
        print("Enter only number")
def nano():
            os.system("pkg install nano -y")
            os.system("clear")
            text()

def vim():
            os.system("pkg install vim -y")
            os.system("clear")
            text()

def webidle():
            os.system("pkg install git -y")
            os.system("git clone https://github.com/raynoppe/BLACKICEcoder.git -y")
            os.system("cd blackicecoder")
            os.system("chmod 775 backups/")
            os.system("cd BLACKICEcoder && vim lib/config__settings.php")
            os.system("clear")
            text()

def micro():
            os.system("pkg install micro -y")
            os.system("clear")
            text()

def neovim():
            os.system("pkg install neovime -y")
            os.system("clear")
            text()

def emacs():
            os.system("pkg install emacs -y")
            os.system("clear")
            text()

def jupp():
            os.system("pkg install jupp -y")
            os.system("clear")
            text()


def pro():
    os.system("clear")
    logo()
    print(""" \033[0;31mChoose Programming
    \033[0;33m(1) php
    \033[0;37m(2) python2
    \033[0;32m(3) python
    \033[0;35m(4) nodejs 
    \033[0;36m(5) c
    \033[0;34m(6) c++
    \033[0;31m(7) java
    \033[0;34m(8) ruby
    \033[0;37m(9)  Main Menu
    \033[0;36m(00) exit""")
    try:
      a = int(input(" \033[31mMART\033[33m=\033[32m=\033[37m>"))
      if a == 1:
        php()
      elif a == 2:
        python2()
      elif a == 3:
        python()
      elif a == 4:
        nodejs()
      elif a == 5:
        c()
      elif a == 6:
        cdouble()
      elif a == 7:
        java()
      elif a == 8:
        ruby()
      elif a == 9:
        os.system("clear")
        menu()
      elif a==00:
        os.system("clear")
        exit()
      else:
        print("NO include")
        os.system("clear")
        pro()
    except ValueError:
        print("Please Enter Number")
def php():
 os.system("pkg install php -y")
 os.system("clear")
 pro()
def python2():
    os.system("pkg install python2 -y")
    os.system("clear")
    pro()
def python():
    os.system("pkg install python -y")
    os.system("clear")
    pro()
def nodejs():
    os.system("pkg install nodejs -y")
    os.system("clear")
    pro()
def c():
    os.system("pkg install clang -y")
    os.system("clear")
    pro()
def cdouble():
    os.system("pkg install g++")
    os.system("clear")
    pro()
def java():
    os.system("pkg install wget && wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava && installjava")
    os.system("clear")
    pro()
def ruby():
    os.system("pkg install ruby -y ")
    os.system("clear")
    pro()
def scan():
    os.system("clear")
    logo()
    print("""           \033[0;37m Scaning Tools
    \033[0;34m (1) Nmap
    \033[0;37m (2) TM-Scanner
    \033[0;32m (3) Cyber SCan
    \033[0;31m (4) WhatWeb
    \033[0;35m (5) Nikto
    \033[0;33m (6) Main Menu
    \033[0;36m (7) Exit""")
    try:
      b=int(input("\033[31mMART\033[33m=\033[32m=\033[37m> "))
      if b==1:
        nmap()
      elif b==2:
        tm()
      elif b==3:
        cs()
      elif b==4:
        ww()
      elif b==5:
        file()
      elif b==6:
        os.system("clear")
        menu()
      elif b==7:
        os.system("clear")
        exit()
      else:
        print("No include")
        os.system("clear")
        scan()
    except ValueError:
        print("Please Enter Number")
def nmap():
    os.system("pkg install nmap -y")
    os.system("clear")
    scan()
def tm():
    os.system("pkg install ")
    os.system("git clone https://github.com/TechnicalMujeeb/TM-scanner.git")
    os.system("chmod +x *")
    os.system("clear")
    scan()
def cs():
    os.system("git clone https://github.com/medbenali/CyberScan.git")
    os.system("clear")
    scan()
def ww():
    os.system("git clone https://github.com/urbanadventurer/WhatWeb")
    os.system("clear")
    scan()
def file():
    os.system("git clone https://github.com/sullo/nikto.git")
    os.system("clear")
    scan()
def web():
    os.system("clear")
    logo()
    print("""
           \033[0;37m Web Server
        \033[0;31m (1) ssh
        \033[0;36m (2) apache2
        \033[0;34m (3) mysql
        \033[0;33m (4) menu
        \033[0;35m (5) exit
        """)
    try:
      c=int(input("\033[31mMART\033[33m=\033[32m=\033[37m> "))
      if c==1:
        ssh()
      elif c==2:
        apache()
      elif c==3:
        mysql()
      elif c==4:
        menu()
      elif c==5:
        os.system("clear")
        exit()
      else:
        print("No exit")
        os.system("clear")
        web()
    except ValueError:
        print("Please Enter Number")
def ssh():
    os.system("pkg install openssh")
    os.system("clear")
    web()
def apache():
    os.system("pkg install apache2")
    os.system("clear")
    web()
def mysql():
    os.system("pkg install mariadb")
    os.system("clear")
    web()
def wh():
     os.system("clear")
     logo()
     print("""
                    \033[0;32mWeb Hacking Tools
     \033[0;37m (1)Sql injection
     \033[0;35m (2)wpscan
     \033[0;33m (3)Xattacker
     \033[0;32m (4)joomla vunlerability
     \033[0;31m (5) Admin Finder
     \033[0;36m (6) XSStrike  
     \033[0;37m (7)Hammer DDOS
     \033[0;34m (8) Menu
     \033[0;36m (9) Exit""")
     try:
       mart=int(input("mart==>"))
       if mart==1:
         sql()
       elif mart==2:
         wpscan()
       elif mart==3:
         xatt()
       elif mart==4:
          jomla()
       elif mart==5:
        admin()
       elif mart==6:
         xss()
       elif mart==7:
         hammer()
       elif mart==8:
         menu()
       elif mar==9:
         os.system("clear")
         exit()
       else:
         print("no exit")
         os.system("clear")
         wh()
     except ValueError:
         print("Enter Number")
def sql():
    os.system("git clone https://github.com/sqlmapproject/ssqlmap.git")
    os.system("clear")
    wh()
def wpscan():
    os.system("git clone https://github.com/swisskyrepo/Wordpresscan.git")
    os.system("clear")
    wh()
def xatt():
    os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git")
    os.system("clear")
    wh()
def jomla():
    os.system("git clone https://github.com/sachin75638/jdash")
    os.system("clear")
    wh()
def admin():
    os.system("git clone https://github.com/fnkOc/cangibrina.git")
    os.system("clear")
    wh()
def xss():
    os.system("git clone https://github.com/sOmd3v/XSStrike.git")
    os.system("clear")
    wh()
def hammer():
    os.system("git clone https://github.com/Pavithran-R/Hammer")
    os.system("clear")
    wh()
def dev():
    os.system("clear")
    logo()
    print("""   
               \033[0;35m  Exploit and The best Tools
            \033[0;37m (1) Metasploit
            \033[0;34m (2) Routersplit
            \033[0;33m (3) Phonesploit
            \033[0;32m (4) Tool-x
            \033[0;35m (5) Hacktroian 
            \033[0;31m (6) termux-adb
            \033[0;32m (7) menu
            \033[0;36m (8) exit""")
    try:
      c=int(input("\033[31mMART\033[33m=\033[32m=\033[37m> "))
      if c==1:
        msf()
      elif c==2:
        rou()
      elif c==3:
        phone()
      elif c==4:
        tool()
      elif c==5:
        hack()
      elif c==6:
        hack()
      elif c==7:
        os.system("clear")

        menu()
      elif c==8:
        os.system("clear")
        exit()
      else:
        print("No exit")
        os.system("clear")
        wh()
    except ValueError:
        print("Enter Number")
def msf():
    os.system("pkg install curl")
    os.system("curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz")
    os.system("gunzip metasploit_5.0.65-1_all.deb.gz")
    os.system("dpkg -i metasploit_5.0.65-1_all.deb")
    os.system("apt 0-f install")
    os.system("clear")
    dev()
def rou():
    os.system("https://github.com/threat9/routersploit")
    os.system("clear")
    dev()
def phone():
    os.system("git clone https://github.com/metachar/PhoneSploit")
    os.system("clear")
    dev()
def tool():
    os.system("https://github.com/rajkumardusad/Tool-X")
    os.system("clear")
    dev()
def hack():
    os.system("git clone https://github.com/thehackingsage/hacktronian.git")
    os.system("clear")
    dev()
def adb():
    os.system("apt update && apt install wget && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh")
    os.system("clear")
    dev()
def pwhash():
    logo()
    print("""
                       \033[35mPassword Hash Tools
            \033[34m(1)hasher
            \033[36m(2)Hash-Buster
            \033[32m(3)Main Menu
            \033[32m(4)Exit""")
    try:
     a=int(input("\033[31mMART\033[33m=\033[32m=\033[37m> "))
     if a==1:
        hash()
     elif a==2:
        hbuster()
     elif a==3:
        os.system("clear")
        menu()
     else:
        os.system("clear")
        exit()
    except ValueError:
        print("Enter Number")
def hash():
    os.system("git clone https://github.com/ciku370/hasher")
    os.system("clear")
    pwhash()

def hbuster():
    os.system("git cloen https://github.com/UltimateHackers/Hash-Buster")
    os.system("clear")
    pwhash()
menu()
