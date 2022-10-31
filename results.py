# It's work is to display student data(results).

import os
import sys
#from necta.globalv import *
from necta.errors import *
from nectaapi.student import *
from necta.animations import *
from tabulate import tabulate
from time import sleep
#from necta.globalv import *


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




# Taking the datas from the user by,
# Typing.

os.system("clear")
schoolNumber= input("\n   School number eg s3140: "+ __YELLOW__)
os.system("clear")
   
   #LOGO HERE
print(__RESET__+"\n   School Number: "+__BOLDCYAN__+schoolNumber)
studentNumber=input(__RESET__+"   Candidate number eg 0180: "+__YELLOW__)
os.system("clear")
   
   #LOGO HERE
print(__RESET__+"\n   School Number: "+__BOLDCYAN__+schoolNumber)
print(__RESET__+"   Candidate Number: "+__BOLDCYAN__+studentNumber)
year= input(__RESET__+"   The examination year eg 2019: "+__YELLOW__)
os.system("clear")
   
   #LOGO HERE
print(__RESET__+"\n   School Number: "+__BOLDCYAN__+schoolNumber)
print(__RESET__+"   Candidate Number: "+__BOLDCYAN__+studentNumber)
print(__RESET__+"   Exam Year: "+__BOLDCYAN__+year+__RESET__)
examType=input("   acsee or csee? :: "+__YELLOW__)
print(__RESET__+"")
os.system("clear")
# E N D   O F  A S K I N G


      #LOGO HERE
#Displaying the data user have entered.
print(__RESET__+"\n   School Number: "+__BOLDCYAN__+schoolNumber)
print(__RESET__+"   Candidate Number: "+__BOLDCYAN__+studentNumber)
print(__RESET__+"   Exam Year: "+__BOLDCYAN__+year+__RESET__)
print(__RESET__+"   Exam Type :: "+__BOLDCYAN__+examType+__RESET__)


# Starting a new screen.
sleep(4)
os.system("clear")

   
   
   #ANOTHER LOGO2
# T H E  
# L O A D I N G
# A N I M A T I O N

print("\n\n\n")
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year}  {__RESET__} ")
print("Loading.")
sleep(2)
os.system("clear")
   
   #ANOTHER LOGO2
print("\n\n\n")
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year} {__RESET__}")
print("Loading..")
sleep(1.5)
os.system("clear")
   
   #ANOTHER LOGO2
print("\n\n\n")
print(f"             Candidate:: {__BOLDCYAN__} {schoolNumber}/{studentNumber}/{year} {__RESET__}")
print("Loading...")
sleep(4)
os.system("clear")
   #END OF ANIMATION

# Taking data from Api source.
results = student(year, examType, schoolNumber, studentNumber)

# To check if the inserted data are,
# Accepted format.
def check():
   os.system("clear")
   if (schoolNumber[0]=="s" or schoolNumber[0]=="S" or schoolNumber[0]=="P" or schoolNumber[0]=="p") and len(schoolNumber)== 5:
       rst()
   else:
        print(__RED__+"Invalid School Number"+__RESET__)
        print("See how to use this tool::  "+__BACKCYAN__+"necta help"+__RESET__+" or"+__BACKCYAN__+"necta --help"+__RESET__)
        sys.exit()
    
 
   
#The results are printed here!!  
def rst():
    os.system("clear")
    sleep(0.5)
    division=results.get("division")
    point=results.get("points")
    school_name=results.get("school_name","")
    gender=results.get("gender","")
    examination_number=results.get("examination_number","This is impossible!")
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
         
    # Thanks to w3 schools I nearly spend,      # A night to these Two variables.
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


# Sun, Oct 30 2022. 21:37EAT