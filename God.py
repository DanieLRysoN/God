#python 2.7.15
import os
os.system("pip install colored")
os.system("pip install colorama")
os.system("pip install datetime")
#importing
import time                                                     
import sys                                                      
import colored                                                  
import colorama                                                 
import datetime
from colored import fg, bg, attr
from colorama import Fore, Back, Style                          
# rang
red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'
os.system("clear")
print(f"{blue} ")
print (Fore.BLUE + "")
x = """


                                                 . ...'..'','''.......
                                           ........',:;;,c::ldlcccc:cc,,
                                          .......',',:,;c:ccc:ocdllloo:;.
                                          ......'.',,',l:::;lolocllllcco.
                                             .....,:;;;;':;,:c::llll;col;.
                                          ........';....',;:;;dcc:codcklc;
                                         ......'.. ...'''.... ....':cloc::
                                          ............        .... . .ccl:.
                                            .......        ..,';;::o:;,cc:.
                                          ........      ..,,;llloco:olllc:'
                                            ...,........,:col:cdl:loolc::,
                                              ..,;...,.''..........lcc:::o
                                               .,;','..            ....:::.
                                               .,.;.'.. . .....','.:lxccc:
                                               .c;::;;,;;:,;cc;cc:ol;ooc:;
                                               .:;':';',::::ol:::;c:;lld;'
                                               .';;;;:;;';:,::,;;:,:ldoc:,
                                               .,;:;::c::clcc;;::clocoocc.
                                               .;,;;,,:;,':c:::::c;oocc;;.
                                              ..',,;;;;:;,,,''':;:cc:l:c;
                                               .',.....,;c:;;:'.. ...:oc'
                                                   .c,;;lclll,.. ';..cl:
                                                    ..,,,:,;.   ;c'',llc
                                              ...             'lo;.;l:;.
                                             ....      ....,::cl,.':lo.
                                               . .....';:''cll;'.;cll'
                                               ..'...;,,:;c::,'';:lc.
                                                   .,;;;ol;;:;::cc;.
                                                  .':oc,:l:;:lc::'
                                                  .'ccl:;;::;;c'
                                                   ,:c;:,;:c,'
                                                   ;;:':cc;'.
                                                  .:,:c;c.
                                                  'c:l,.
                                                  ..."""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.00001)
os.system("clear")