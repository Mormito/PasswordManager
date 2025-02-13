import os
import platform

from cryptography.fernet import Fernet
from generate import *

path = None
filename = None

def definePath():
    clear()
    global path

    print("Set the path")
    path = input(">> ").strip() + "\\"

    print(path)

def defineFilename():
    global filename

    print()
    print("Set the name")
    filename = input(">> ").strip()


def show():
    clear()
    print("Path: " + path)
    print("Filename: " + filename)


def reader():
    fr = open(path + filename + ".txt", "r")
    print(fr.read())


def writer():
    print("file name is: " + filename)
    fw = open(path + filename + ".txt", "a")
    fw.write("newpassword" + "\n")


def encrypt():
    clear()

    print("Do you have any key?" )
    print("1 - YES")
    print("2 - NO")

    haveakey = int(input(">> " ))

    if haveakey != 1:
        clear()

        # here generate the key, and i created a var for key string, because a FW needs a string argument.
        key = Fernet.generate_key()
        key_str = key.decode()
        fernetKey = Fernet(key)

        # filereader
        with open(path + filename + ".txt", "r") as freader:
            content = freader.read()
            content_bytes = content.encode()

        # encrypt the content (passwords) and writes in a txt
        token = fernetKey.encrypt(content_bytes)
        print(token)

        token_str = token.decode()

        fw = open(path + filename + ".txt", "a")
        fw.write(token_str + "\n")

        clear()
        warning()
        pause()
        # key filewriter
        definePath()
        defineFilename()
        fw = open(path + filename + ".txt", "w")
        fw.write(key_str)

    else:     
        # ask to set path and filename for extract the key
        warning()
        pause()
        definePath()
        defineFilename()

        # reads the key
        fr = open(path + filename + ".txt", "r")
        key = fr.read()
        key_bytes = key.encode()
        fernetKey = Fernet(key_bytes)

        clear()
        print("Now you need to set the path and name of your passwords file")

        definePath()
        defineFilename()

        with open(path + filename + ".txt", "r") as freader:
            content = freader.read()
            content_bytes = content.encode()

        # token = f.encrypt(path + filename)
        token = fernetKey.encrypt(content_bytes)
        print(token)

        token_str = token.decode()

        f = open(path + filename + ".txt", "w")
        f.write(token_str)


def decrypt():
    print()


def clear():
    if(platform.system() == "Windows"):
        os.system('cls')
    else:
        os.system('clear')

def password_system(): 
        clear()
        newpassword = generatepasswd()
        print("Password: " + newpassword)

        print("Did you like this password?")
        print()
        print("1 - YES")
        print("2 - NO")
        

        answer2 = int(input(">> ").strip())

        if answer2 == 1:

            definePath()
            defineFilename()
            writer()
            encrypt()

            #Create a save system | with encrypting
            #decrypt the file  
            #add the password
            #encrypt
        else:
            password_system()

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