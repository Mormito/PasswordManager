from generate import *
from encrypt_decrypt import *


# def initpasswd():
#     adminpasswd = "x"
#     clear()
#     print()
#     print("First of all, write your password here.")
#     answer = input(">> ").strip()

#     if(adminpasswd != answer):
#         clear()
#         print("INCORRECT")
#         exit()
#     else:
#         clear()
#         mainMSG()

def mainMSG():
    clear()

    print('''[ OPTIONS !]
                            
1 - Generate a random password
2 - Check your password list

              
''')
    
    answer = int(input(">> ").strip())
    if answer == 1:
        password_system()
    elif answer == 2:
        decrypt()


        #show decrypt passwords


mainMSG()