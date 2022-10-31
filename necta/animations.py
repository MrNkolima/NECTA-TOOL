# This is the animation file, all the animations,
# I have put them here!!!

import os
import sys
from time import sleep
from necta.globalv import *
#from errors import *


# These variables will be used regularly,
# So I decide to put them in the globalv.py
__TOOL__= "NECTA-TOOL"
__VERSION__= "1.0.0"
__YEAR__="©2022"
__DEVELOPER__= "Isack Nkolima"
__TWITTER__ = "https://twitter.com/isack_nkolima"
__GITHUB__= "https://github.com/MrNkolima"

__AVAILABLE__="Due to api dependance:: 2015 to 2022 ACSEE & CSEE results are available for this version"

#The colors used
__TOOL__= "NECTA-TOOL"
__BOLDRED__= "\033[01;31m"
__BOLDGREEN__= "\033[01;32m"
__BOLDBLUE__= "\033[01;34m"
__BOLDYELLOW__="\033[01;33m"
__BOLDCYAN__= "\033[01;36m"
__BOLDPURPLE__= "\033[01;35m"
__BACKBLUE__= "\033[44m"
__BACKPURPLE__= "\033[45m"
__BACKCYAN__= "\033[46m"
__RED__= "\033[0;31m"
__GREEN__= "\033[0;32m"
__BLUE__= "\033[0;34m"
__CYAN__= "\033[0;36m"
__YELLOW__= "\033[0;33m"
__PURPLE__= "\033[0;33m"
__RESET__="\033[00m"

# I love this piece of code very much!!,
# This helps me to diagnostically detect,
# And to assign the OS to variables so,
# That I can distinguish them in some,
# Critical situations.

if os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
  #This deals with TERMUX Environment.
  home=os.getenv("HOME")+"/"
  bd="/data/data/com.termux/files/usr/bin/"
  # bd=> bin directory.
  sd="/data/data/com.termux/files/usr/share/"
  # sd=> share directory.
  system="termux"
  # System is Termux Environment.

# This deals with non Termux Environments,
# Like Linux and Ubuntu (Desktops)
elif os.path.exists("/usr/bin/apt") or os.path.exists("/usr/bin/apt-get") or os.path.exists("/bin/apt") or os.path.exists("/bin/apt"):
  if os.path.exists("/usr/lib/sudo") or os.path.exists("/usr/bin/sudo") or os.path.exists("/usr/sbin/sudo"):
      home=os.getenv("HOME")+"/"
      pkg="sudo apt-get"
      bd="/usr/bin/"
      sd="/usr/share/"
      system="ubuntu"
  else:
      home=os.getenv("HOME")+"/"
      pkg="apt-get"
      bd="/usr/bin/"
      sd="/usr/share/"
      system="debian"


def version():
  print(__TOOL__+" version:  "+__BOLDCYAN__+__VERSION__+__RESET__)
  print(__YELLOW__+__AVAILABLE__+__RESET__+"!!")
  sys.exit()
 
 
def install():
   os.system("clear")
   print(__BOLDBLUE__+"     Installing "+__TOOL__+" ..."+__RESET__+__BOLDCYAN__)
   sleep(4)
   os.system("clear")
   print("\n\n\n\n     (1%)->")
   sleep(0.9)
   os.system("clear")
   print("\n\n\n\n     (7%)----->")
   sleep(0.7)
   os.system("clear")
   print("\n\n\n\n     (11%)------>")
   sleep(0.2)
   os.system("clear")
   print("\n\n\n\n     (23%)----------->")
   sleep(0.3)
   os.system("clear")
   print("\n\n\n\n     (33%)---------------->")
   sleep(0.1)
   os.system("clear")
   print("\n\n\n\n     (65%)------------------------->")
   sleep(0.2)
   os.system("clear")
   print("\n\n\n\n     (87%)---------------------------->")
   sleep(0.1)
   os.system("clear")
   print("\n\n\n\n     (100%)-----------------------------------|"+__RESET__)
   sleep(3)
   os.system("clear")
   print(__BOLDGREEN__+"\n\n\n\n     NECTA-TOOL is successfully installed!"+__RESET__)
   sleep(4)
   os.system("clear")
   print("\n\n")
   print("""       ╔═╗─╔╦═══╦═══╦════╦═══╗─╔════╦═══╦═══╦╗
       ║║╚╗║║╔══╣╔═╗║╔╗╔╗║╔═╗║─║╔╗╔╗║╔═╗║╔═╗║║
       ║╔╗╚╝║╚══╣║─╚╩╝║║╚╣║─║║─╚╝║║╚╣║─║║║─║║║
       ║║╚╗║║╔══╣║─╔╗─║║─║╚═╝╠══╗║║─║║─║║║─║║║─╔╗
       ║║─║║║╚══╣╚═╝║─║║─║╔═╗╠══╝║║─║╚═╝║╚═╝║╚═╝║
       ╚╝─╚═╩═══╩═══╝─╚╝─╚╝─╚╝───╚╝─╚═══╩═══╩═══╝""")
   print("\n"+__GREEN__+"    [+]"+__RESET__+"Type:"+__BOLDCYAN__+" necta --help"+__RESET__+ " to get to know how this tool \n       Works and see TERMS OF USE.")
   print(__GREEN__+"    [+]"+__RESET__+"By using this tool you agree to "+__CYAN__+"TERMS OF USE"+__RESET__+".\n\n")
  
  
        
   
   
def uninstall():
   askv=input(f"\n\n  Do you really want to uninstall NECTA-TOOL? {__BOLDYELLOW__}[y or n]\n\n              >>> ")
   if askv == "n" or askv == "N":
     exit()
   elif askv== "y" or askv == "Y":
     pass
   else:
     print(__BOLDRED__+"\n        Error:: Invalid chose!!\n"+__RESET__)
     sleep(3)
     sys.exit()
     

def update ():
   askv=input(f"\n\n  Do you really want to update NECTA-TOOL? {__BOLDYELLOW__}[y or n]\n\n              >>> ")
   if askv == "n" or askv == "N":
     exit()
   elif askv== "y" or askv == "Y":
     pass
   else:
     print(__BOLDRED__+"\n        Error:: Invalid chose!!\n"+__RESET__)
     sleep(3)
     sys.exit()    
  
  

def exit():
  print(__BOLDRED__+"    Exiting..."+__RESET__)
  sleep(2.5)
  sys.exit()
  
#Sat, Oct 30 2022. 03:45EAT
