import os
import sys
from tabulate import tabulate
from time import sleep
from nectaapi.student import *
#from necta.globalv import *


# These variables will be used regularly,
# So I decide to put them in the var.py
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


# Converting the user inputs to variables,
# That works with Api
schoolNumber=sys.argv[1]
studentNumber=sys.argv[2]
year=sys.argv[3]
examType=sys.argv[4]


os.system("clear")
#logo
print("\n\n")
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year}  {__RESET__} ")
print("Loading.")
sleep(2)
os.system("clear")
   
#logo
print("\n\n")
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year} {__RESET__}")
print("Loading..")
sleep(1.5)
os.system("clear")
   
#logo   
print("\n\n") 
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year} {__RESET__}")
print("Loading...")
sleep(4)
os.system("clear")
   #END OF ANIMATION

# Get data from api.
results = student(year, examType, schoolNumber, studentNumber)


# To check if the inserted school number,
# Is valid if not Terminate process
def check():
   os.system("clear")
   if (schoolNumber[0]=="s" or schoolNumber[0]=="S") and len(schoolNumber)== 5:
       rst()
   else:
        print(__RED__+"\n  Error:: Invalid school number Format!!!!!"+__RESET__)
        print("  See how to use this tool::  "+__BACKCYAN__+"necta help"+__RESET__)
        print("")
        sys.exit()
    
   
def rst():
    #LOGO HERE
    #The results are printed here!!
    os.system("clear")
    sleep(0.5)
    division=results.get("division")
    point=results.get("points")
    school_name=results.get("school_name")
    gender=results.get("gender","")
    examination_number=results.get("examination_number","This cannot happen!")
    print("""      ╭━╮╱╭┳━━━┳━━━┳━━━━┳━━━╮╱╭━━━━┳━━━┳━━━┳╮
      ┃┃╰╮┃┃╭━━┫╭━╮┃╭╮╭╮┃╭━╮┃╱┃╭╮╭╮┃╭━╮┃╭━╮┃┃
      ┃╭╮╰╯┃╰━━┫┃╱╰┻╯┃┃╰┫┃╱┃┃╱╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
      ┃┃╰╮┃┃╭━━┫┃╱╭╮╱┃┃╱┃╰━╯┣━━╮┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
      ┃┃╱┃┃┃╰━━┫╰━╯┃╱┃┃╱┃╭━╮┣━━╯┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
      ╰╯╱╰━┻━━━┻━━━╯╱╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰━━━┻━━━┻━━━╯""")
    print("     Candidate: "+__BOLDCYAN__+examination_number+__RESET__)
    print("     Gender:    "+__BOLDCYAN__+gender+__RESET__)
    if examType=="acsee" or examType=="ACSEE":
        print("     School (A-Level): "+__BOLDCYAN__+school_name+__RESET__)
    elif examType=="csee" or exam_type=="CSEE":
        print("     School (O-Level): "+__BOLDCYAN__+school_name+__RESET__)
    else:
         print(__BOLDRED__+"\n\n          How can you reach here?"+__RESET__)
         print("Here")
         sys.exit()
         
    # Thanks to w3 schools I nearly spend,  # A whole night to these Two variables.
    print("\n\n")
    rslts=list(results["subjects"].keys())
    grds=list(results["subjects"].values())    
    table={"RESULTS": rslts,
                "GRADES": grds
     }
    print(tabulate(table,headers="keys"))
    print("\n")
    print("          DIVISION: "+__BOLDCYAN__+division+__RESET__)
    print("          POINT:  "+__BOLDCYAN__+point+__RESET__)
    
    print("\n\n\n\n\n")
    print("                 "+__TOOL__+__YEAR__)
    print("            Developer: "+__BOLDBLUE__+__DEVELOPER__+__RESET__)
    print("")
    sys.exit()
     
check()

#Sun, Oct 30 2022.