#!/usr/bin/python3

#This is the main file of execution,
#All the operations are done here,

import os 
import sys
from necta.animations import *
#from necta.globalv import *
from necta.errors import *


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



## My favorite piece of code.
if os.getuid() == 0 or system=="termux":
  pass
else:
    print("\nerror: Please, Run This programm as Root!\n")
    sys.exit()
if len(sys.argv)>1:
  pass
else:
  print ("error : invalid arguments !!")
  print ("use : necta --help  for more information")
  sys.exit()

if sys.argv[1]=="results":
  if system=="ubuntu":
      os.system("sudo python3 results.py ")
  else:
      os.system("python3 results.py ")
      
elif sys.argv[1]=="version" or sys.argv[1]=="--version":
  version()
  
elif sys.argv[1]=="--help" or sys.argv[1]=="help":
  os.system("python3 necta/help.py")
  
  
elif sys.argv[1]=="update":
  if system=="ubuntu":
    os.system("cd "+home+" && sudo git clone https://github.com/MrNkolima/NECTA-TOOL.git")
  else:
    os.system("cd "+home+" && git clone https://github.com/MrNkolima/NECTA-TOOL.git")
  if os.path.exists(home+"NECTA-TOOL"):
    os.system("cd "+home+"NECTA-TOOL && sh install")
    os.system("clear")
    update()
    sys.exit()
  else:
    print(__YELLOW__+"       [+]"+__RESET__+" Can't update "+__TOOL__+".")
    print(__YELLOW__+"       [+]"+__RESET__+" Please check your internet connection.")
    print(__YELLOW__+"       [+]"+__RESET__+" Remember UPDATES comes with new features!!.")
    print("\n")
    sys.exit()
  
elif sys.argv[1]=="uninstall":
 uninstall ()
 if system=="ubuntu":
   os.system("cd "+sd+" && sudo rmdir NECTA"+" && cd "+bd+" &&  rm -rf necta")
   print("Uninstall NECTA-TOOL successful!!")
 else:
   os.system("cd "+sd+" && rm -rf NECTA && cd "+bd+" && rm -rf necta")
   print("Uninstallation successful")
 sys.exit()
 
elif len(sys.argv) == 5:
 if system=="ubuntu":
     os.system("sudo exec python3 attach.py "+ sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
 else:
     os.system("exec python3 attach.py "+ sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4])
else:
  invalidWrite()
  
# 25 Oct, 2022 -> Final day