import os, sys
sys.path.append('/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators')

from boolean_py import not_bool

with open('fifosomething.txt', 'w') as fifo:
    print(not_bool(int(sys.argv[1]),), file=fifo)
