import os
import sys
import subprocess

ip = ""
global needReboot
global changesMade

needReboot = False
changesMade = "Stuff added to the system:"


def vim():

    global changesMade

    os.system("sudo apt install vim -y")
    changesMade += "\n\tVim installed"

def matrix():
    global changesMade
    os.system("sudo apt install cmatrix -y")
    changesMade += "\n\tCMatrix installed"

def netTools():
    global changesMade
    os.system("sudo apt install net-tools -y")
    changesMade += "\n\tNet-tools installed"

def docker():
    global changesMade
    os.system("sudo snap install docker")
    os.system("sudo usermod -aG docker $USER")
    changesMade += "\n\tDocker components added (docker, docker-compose)"

def awesome():
    global changesMade
    os.system("sudo apt-get install awesome -y")
    changesMade += "\n\tInstalled Awesome Window Manager"

def htop():
    global changesMade
    os.system("sudo apt-get install htop -y")
    changesMade += "\n\tHtop installed"

def gnome():
    global changesMade
    os.system("sudo apt-get install tasksel -y")
    os.system("sudo tasksel tsall ubuntu-desktop -y")
    changesMade += "\n\tGnome installed"

def git():
    global changesMade
    os.system("sudo apt install git -y")
    os.system('git config --global user.email "chesspro13@gmail.com"')
    os.system('git config --global user.name "Brandon"')
    changesMade += "\n\tGit installed"

def pip():
    global changesMade
    os.system("sudo apt install python3-pip")
    changesMade += "\n\tPip installed"

def networkData():
    os.system("ifconfig > ip.txt")
    f = open("ip.txt")
    os.remove("ip.txt")
    f.readline() 
    ip = f.readline().split()[1]
    print( "This computers IP address is " + ip )

def keybindings():

    # defining keys & strings to be used
    key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
    subkey1 = key.replace(" ", ".")[:-1]+":"
    item_s = "/"+key.replace(" ", "/").replace(".", "/")+"/"
    firstname = "custom"
    # get the current list of custom shortcuts
    get  = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    array_str = get("gsettings get "+key)
    # in case the array was empty, remove the annotation hints
    command_result = array_str.lstrip("@as")
    current = eval(command_result)
    # make sure the additional keybinding mention is no duplicate
    n = 1
    while True:
        new = item_s+firstname+str(n)+"/"
        if new in current:
            n = n+1
        else:
            break
    # add the new keybinding to the list
    current.append(new)

    setKeyBinding(key, current, subkey1, new, "Open a terminal", "gnome-terminal")

def setKeyBinding(key, current, subkey1, new, a, b, c):
    # create the shortcut, set the name, command and shortcut key
    cmd0 = 'gsettings set '+key+' "'+str(current)+'"'
    cmd1 = 'gsettings set '+subkey1+new+" name '"+sys.argv[1]+"'"
    cmd2 = 'gsettings set '+subkey1+new+" command '"+sys.argv[2]+"'"
    cmd3 = 'gsettings set '+subkey1+new+" binding '"+sys.argv[3]+"'"

    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        subprocess.call(["/bin/bash", "-c", cmd])

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
    global changesMade
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
        changesMade += "\n\tStatic IP address set to [192.168.0." + str(addr) + "/24]"
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
    print("\t5)Pip")
    print("\t6)CMatrix")
    print("\t7)Gnome")
    print("\t8)Htop")
    print("\t9)Awesome wm")

    result = input()

    if "1" in result:
        vim()
    if "2" in result:
        netTools()
    if "3" in result:
        git()
    if "4" in result:
        docker()
    if "5" in result:
        pip()
    if "6" in result:
        matrix()
    if "7" in result:
        gnome()
    if "8" in result:
        htop()
    if "9" in result:
        awesome()

    if ip != "":
        networkData()

    

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
    global changesMade
    sudoTest()
    print("\n\n")
    print("1) Computer initial setup")
    print("2) Git clone")

    result = input()

    if result == "1":
        setup()
    if result == "2":
        gitClone()

    print("\n\n\n" + changesMade)

    if needReboot:
        print("\n\n==There have been changes to your system that require a reboot to take effect. Do you wish to reboot? [y/n]")
        rb = input()

        if "y" in rb.lower() or "yes" in rb.lower():
            os.system("sudo reboot")

init()

print('\a')
