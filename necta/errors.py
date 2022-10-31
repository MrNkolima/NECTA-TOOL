#All the Errors, I have put them here,
#I found very boring to each time writing,
#Errors so I think this will help

import os
import sys
from time import sleep
#from necta.globalv import *
#from animations import *


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


def invalidChose():
  print(__BOLDRED__+"    Error::: You chose an invalid choice!!!"+__RESET__)
  print(__BOLDRED__+"    Check again your entry!"+__RESET__)
  os.system("exit")
  
def invalidWrite():
  print(__BOLDRED__+"     Error: "+ __RESET__+"  You wrote invalid format!! ")
  print(__BOLDRED__+"     Try like this::"+__RESET__+__BOLDCYAN__+"  necta s3140 0180 2018 csee"+__RESET__)
  print("     Type::"+__YELLOW__+" necta --help"+__RESET__+" To get more information")
  os.system("exit")
  
#Frid, Oct 28 2022. 22:10EAT