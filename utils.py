import os
import platform

def warning():
    i = 0
    while i <= 5:
        print("WARNING! Now you need to set a path for your key, if you lost the key you will lost the password!!!")
        i+=1


def pause():
    if(platform.system() == "Windows"):
        os.system('pause')
    else:
        os.system('sleep 6')