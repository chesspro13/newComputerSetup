import os

ip = ""

def basic():
    os.system("sudo apt install vim -y")
    os.system("sudo apt install net-tools -y")
    print("Basic utilities added (vim, net-tools)")

def docker():
    os.system("sudo snap install docker")
#    os.system("sudo apt install docker-compost -y")
    print("Docker components added (docker, docker-compose)")

def git():
    os.system("sudo apt install git -y")
    print("Git installed")

def networkData():
    os.system("ifconfig > ip.txt")
    f = open("ip.txt")
    os.remove("ip.txt")
    f.readline() 
    ip = f.readline().split()[1]

    print( "This computers IP address is " + ip )

def init():
    print("What kind of opperation are you planning?")
    print("\t1)Basic stuff(vim, net-tools)")
    print("\t2)Git")
    print("\t3)Basic docker(opt 1+ docker")

    result = input()

    if "1" in result:
        basic()
    if "2" in result:
        git()
    if "3" in result:
        docker()

    if ip != "":
        networkData()


init()

print('\a')
