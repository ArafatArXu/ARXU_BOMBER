import time
import requests
import sys
import os
import shutil
import json

#Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# Check Python Version, as Python < 3.11 Does not support 3.11 encryption
def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 11):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not Supported!")
        print("[\033[92m*\033[37m] Update Your Python Using the Command Below:\n\n    pkg reinstall python\n")
        sys.exit()

# Show New Message from Author
def showAuthorMsg(msg):
    print()
    print("\033[94m-"*columns, end="")
    print("\033[92mMessage From Author".center(columns+4))
    print("\033[95m-"*columns, end="")
    psb("\n\033[37m    " + msg + "\n")
    print("\033[94m-"*columns, end="", flush=1)
    print()
    open("./more/.msg", "w").write(msg)
    time.sleep(1)
    input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
    logo()

# Check Update
def update():
    try:
        toolVersion = json.loads(open("./more/.version", "r").read())["version"]
    except:
        toolVersion = "ARXU"
    
    try:
        authorMsg = open("./more/.msg", "r").read().replace("\n", "")
    except:
        authorMsg = "None"
    
    try:
        parsedData = requests.get("https://raw.githubusercontent.com/ArafatArXu/ARXU_BOMBER/main/more/.versions").json()
    except:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Connect To The Internet!")
        time.sleep(1)
        l = input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
        update()
    
    mainVersion = parsedData["version"]
    newMsg = parsedData["message"]
    
    # If Tool Version Is not Same, Update Tool
    if (toolVersion != mainVersion):
        psb("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
        time.sleep(0.5)
        psb("    \033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")
        
        os.system("cd .. && rm -rf ARXU_BOMBER && git clone https://github.com/Arxuishere/ARXU_BOMBER/ > /dev/null 2>&1")
        
        print("\033[37mDone")
        psb("\n    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
        time.sleep(0.8)
        
        os.system("cd .. && cd ARXU_BOMBER && python Abomb.py")
    
    else:
        if (authorMsg != newMsg) and (newMsg != "blank"):
            showAuthorMsg(newMsg)

# ASCII art representing your name
def arxuArt():
    print("\n\x1b[94m██╗   ██╗██████╗ ███████╗ ██████╗██╗   ██╗██████╗    ██████╗ ██╗  ██╗".center(columns+15))
    print("\x1b[94m██║   ██║██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗   ██╔══██╗██║ ██╔╝".center(columns+15))
    print("\x1b[94m██║   ██║██████╔╝███████╗██║     ██║   ██║██████╔╝   ██████╔╝█████╔╝ ".center(columns+15))
    print("\x1b[94m██║   ██║██╔══██╗╚════██║██║     ██║   ██║██╔══██╗   ██╔══██╗██╔═██╗ ".center(columns+15))
    print("\x1b[94m╚██████╔╝██████╔╝███████║╚██████╗╚██████╔╝██║  ██║   ██████╔╝██║  ██╗".center(columns+15))
    print("\x1b[94m ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═════╝ ╚═╝  ╚═╝".center(columns+15))

# Options Banner
def banner():
    arxuArt()
    amount = str(main.amount)
    # 21 - 1(lenOfAmount) = 20....
    amount = amount + (" " * (21-len(amount)))
    
    print("\033[95m-" * (columns), end="")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * (columns), end="")
    print("\n")

# Start Running Tool
if (__name__ == "__main__"):
    checkPy()
    from more.data import *
    arxuArt()
    update()
    main()
