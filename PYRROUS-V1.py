print ('\033[1;33m _____  __    __  _____    _____    _____   _   _   _____')
print ('\033[4;34m|  _  \ \ \  / / |  _  \  |  _  \  /  _  \ | | | | /  ___/')
print ('\033[4;34m| |_| |  \ \/ /  | |_| |  | |_| |  | | | | | | | | | |___')
print ('\033[1;33m|  ___/   \  /   |  _  /  |  _  /  | | | | | | | | \___  \ ')
print ('\033[4;34m| |       / /    | | \ \  | | \ \  | |_| | | |_| |  ___| |')
print ('\033[4;34m|_|      /_/     |_|  \_\ |_|  \_\ \_____/ \_____/ /_____/')
import socket
import sys
print ('Enter Your DNS Or Target: ')
hostname = input()
ip=socket.gethostbyname(hostname)
print ('Host Name Is:',hostname,'\n' ' Target Ip Is: ',ip)
