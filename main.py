import os
import socket

os.system("pip install os")
os.system("pip install socket")
os.system("clear")

def system():
    print ("")
    addr=str(input("\033[1;31m[*] \033[1;33mEnter Your ip address \033[1;34m:"))
    try:
       socket.inet_aton(addr)
       print ("")
       print ("\033[1;35m[*] \033[1;32mvalid Ip")
    except socket.error:
       print ("")
       print ("\033[1;35m[*] \033[1;31mInvalid Ip")

def main():
    print ("\033[1;31m")
    print ("██ ██████")
    print ("██ ██   ██")
    print ("██ ██████")
    print ("██ ██")
    print ("██ ██")
    print ("\033[1;33m")
    print (" █████  ██   ██ ███████  █████  ██   ██")
    print ("██   ██ ██   ██ ██      ██   ██ ██  ██")
    print ("██      ███████ █████   ██      █████")
    print ("██   ██ ██   ██ ██      ██   ██ ██  ██")
    print (" █████  ██   ██ ███████  █████  ██   ██")
    print ("\033[1;37m_______________________________")
    print ("\033[1;31m              Tool by -:           ")
    print ("\033[1;36m            Termux hacking        ")
    print ("\033[1;37m_______________________________")
    print ("\033[1;31m[1] \033[1;32mstart")
    print ("\033[1;31m[2] \033[1;32mupdate")
    print ("\033[1;31m[3] \033[1;32mhelp")
    print ("\033[1;31m[4] \033[1;32mexit")
    print ("")
    x=int(input("\033[1;31m[*] \033[1;33mEnter Your choice \033[1;31m:\033[1;34m:"))
    if x==1:
       system()
    elif x==2:
         os.system("pkg update && pkg upgrade")
    elif x==3:
         os.system("pkg")
    elif x==4:
         os.system("clear")
    else:
        print ("not fund ...!")
main()
