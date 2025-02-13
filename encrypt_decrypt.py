from cryptography.fernet import Fernet
from generate import *
from utils import *
path = None
filename = None
newpassword = "failed for some reason"

def definePath():
    clear()
    global path

    print("Set the path [add / or \ at the end of path]")
    path = input(">> ").strip()

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
    fw.write(newpassword)


def encrypt():
    clear()

    print("Do you have any key?" )
    print("1 - YES")
    print("2 - NO")

    haveakey = int(input(">> " ))

    if haveakey == 1:
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

        #set password path and filename
        clear()
        print("Now you need to set the path and name of your passwords file")

        definePath()
        defineFilename()

        #read the encrypted password

        with open(path + filename + ".txt", "r") as freader:
            content = freader.read()
            content_bytes = content.encode()

        # token = f.encrypt(path + filename)
        token = fernetKey.encrypt(content_bytes)

        token_str = token.decode()

        f = open(path + filename + ".txt", "w")
        f.write(token_str)

    else:     
        clear()

        # here generate the key, and i created a var for key string, because a FW needs a string argument.
        key = Fernet.generate_key()
        key_str = key.decode()
        fernetKey = Fernet(key)

        # password filereader
        with open(path + filename + ".txt", "r") as freader:
            content = freader.read()
            content_bytes = content.encode()

        # encrypt the content (passwords) and writes in a txt
        token = fernetKey.encrypt(content_bytes)

        token_str = token.decode()

        fw = open(path + filename + ".txt", "w")
        fw.write(token_str)

        clear()
        warning()
        pause()

        # key filewriter
        definePath()
        defineFilename()
        fw = open(path + filename + ".txt", "w")
        fw.write(key_str)


def decrypt():
    clear()

    print("Set the key path!")

    pause()

    definePath()
    defineFilename()

    fr = open(path + filename + ".txt", "r")
    key = fr.read()
    key_bytes = key.encode()
    fernetKey = Fernet(key)

    print("Set the file path!")
    pause()

    definePath()
    defineFilename()

    fr = open(path + filename + ".txt", "r")
    token = fr.read()
    token_bytes = token.encode()

    content_bytes = fernetKey.decrypt(token_bytes)
    content = content_bytes.decode()
    clear()
    print("Password of " + filename + ": " + content)
    
    


    


def clear():
    if(platform.system() == "Windows"):
        os.system('cls')
    else:
        os.system('clear')

def password_system(): 
        global newpassword

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
        else:
            password_system()

# utils

