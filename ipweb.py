#!/bin/python

import socket
import os,sys,time

os.system("clear")
os.system("pyfiglet -f slant GLoriusHeLL666 | lolcat")

print ("====================================") 
print ("| https://github.com/GloriusHELL |")
print ("	  --------------		")
print ("   	      CillL             ")
print ("====================================")

hostname = input('Masukkan URL: ')
ip_addres = socket.gethostbyname(hostname)


print(f'URL: {hostname}')
print(f'IP Address: {ip_addres}')


