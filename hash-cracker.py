from hashlib import md5, sha1, sha256, sha384
import sys
from time import sleep
import os




print("""

 _   _           _        ____                _    
| | | | __ _ ___| |__    / ___|_ __ __ _  ___| | __
| |_| |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ /
|  _  | (_| \__ \ | | | | |___| | | (_| | (__|   < 
|_| |_|\__,_|___/_| |_|  \____|_|  \__,_|\___|_|\_\a
                                                   

""")




def get_hash():
    Hash = str(input("Enter a valid hash\n#> "))
    return Hash


def Hash_function(password, hashed_pass):
    global Found
    if md5(password.encode()).hexdigest() == hashed_pass:
        Found = True
        print("Hashed password {0} Found#> {1}".format(hashed_pass, password))
    elif sha1(password.encode()).hexdigest() == hashed_pass:
        Found = True
        print("Hashed password {0} Found#> {1}".format(hashed_pass, password))
    elif sha256(password.encode()).hexdigest() == hashed_pass:
        Found = True
        print("Hashed password {0} Found#> {1}".format(hashed_pass, password))
    elif sha384(password.encode()).hexdigest() == hashed_pass:
        Found = True
        print("Hashed password {0} Found#> {1}".format(hashed_pass, password))



def Read_Passwordfile():
        try:
            y = input("Enter Your Wordlist path\n#> ")
            with open(y, "r") as File:
                password = [x.strip() for x in File.readlines() ]
            File.close()
            return password 
        except:
            with open('Wordlist/10-million-password-list-top-1000000.txt', "r") as File:
                password = [x.strip() for x in File.readlines()]
            File.close()
            return password

Found = False
List = Read_Passwordfile()
while True:
    print("Hash or Exit?")
    cmd = str(input("#> "))
    if cmd == "Hash" or cmd == "hash" or cmd == "":
        Hash = get_hash()
        for password in List:
            Hash_function(password, Hash)
            
            if Found:
                break
            if Found == False:
                print(password + " Tested")
    elif cmd == "Exit" or cmd == "exit":
        sys.exit()
    else:
        print("Command Unknown")
        sleep(2)
        sys.exit()