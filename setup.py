import os

ip = ""
needReboot = False


def vim():
    os.system("sudo apt install vim -y")
    print("Vim installed.")

def netTools():
    os.system("sudo apt install net-tools -y")
    print("Net-tools installed")

def docker():
    os.system("sudo snap install docker")
    os.system("sudo usermod -aG docker $USER")
    print("Docker components added (docker, docker-compose)")

def git():
    os.system("sudo apt install git -y")
    os.system('git config --global user.email "chesspro13@gmail.com"')
    os.system('git config --global user.name "Brandon"')
    print("Git installed")

def networkData():
    os.system("ifconfig > ip.txt")
    f = open("ip.txt")
    os.remove("ip.txt")
    f.readline() 
    ip = f.readline().split()[1]
    print( "This computers IP address is " + ip )

def setIP():
    print("\nWhat do you want to set your IP address as? 192.168.0.XXX")
    addr = input()
    
    try:
        addr = int(addr)
    except:
        if type(addr) == str:
            if "quit" in addr.lower():
                print("Skipping static IP")
                return
            else:
                print( "Command not understood: " + addr )
                setIP()

    if type( addr) == int:
        if int(addr) < 1:
            print( str(addr) + " is too low. Please choose an integer between 1-255.")
            setIP()
        elif int(addr) > 255:
            print( str(addr) + " is too high. Please choose an integer between 1-255.")
            setIP()
        else:
            print("Setting IP address at [192.168.0." + str(addr) + "]")
            editIP( addr )


def editIP(addr):
    try:

        f = open("/etc/dhcpcd.conf", "a")
        f.write("\n")
        f.write("\n# Static IP Address")
        f.write("\nstatic interface wlan0")
        f.write("\nstatic ip_address=192.168.0." + str(addr) + "/24")
        f.write("\nstatic routers=192.168.0.1")
        f.write("\nstatic domain_name_servers=192.168.0.1 8.8.8.8")
        
        nc = "\n\n# Static IP Address\ninterface wlan0\nip_address=192.168.0." + str(addr) + "/24\nstatic routers=192.168.0.1\nstatic domain_name_servers=192.168.0.1 8.8.8.8"
#        os.system("sudo " + nc + " >> /etc/dhcpcd.conf")
        needReboot = True
        print("Static IP address set to [192.168.0." + str(addr) + "/24]")
    except:
        print("Something went wrong setting a static IP address!")


    

def setup():
    print("\nDo you want to set up a static IP? [y/n]")

    result = input()

    if "y" in  result.lower() or "yes" in result.lower():
        setIP()

    print("\nWhat kind of opperation are you planning?")
    print("\t1)vim")
    print("\t2)net-tools")
    print("\t3)Git")
    print("\t4)Basic docker")

    result = input()

    if "1" in result:
        vim()
    if "2" in result:
        netTools()
    if "3" in result:
        git()
    if "4" in result:
        docker()

    if ip != "":
        networkData()

    if needReboot:
        print("\n\n==There have been changes to your system that require a reboot to take effect. Do you wish to reboot? [y/n]")
        rb = input()

        if "y" in rb.lower() or "yes" in rb.lower():
            os.system("sudo reboot")

def gitClone():
    print("1) Docker project")

    result = input()

    if "1" in result:
        os.system('git clone https://github.com/chesspro13/serverStuff.git')
        print("Server stuff downloaded")

def sudoTest():
    try:
        f = open("/etc/testing.conf","w")
        f.write("Testing")
        f.close()
        os.system("sudo rm /etc/testing.conf")
    except:
        print("This program must be ran with as super user to work properly!")
        quit()

def init():
    sudoTest()
    print("\n\n")
    print("1) Computer initial setup")
    print("2) Git clone")

    result = input()

    if result == "1":
        setup()
    if result == "2":
        gitClone()

init()

print('\a')
