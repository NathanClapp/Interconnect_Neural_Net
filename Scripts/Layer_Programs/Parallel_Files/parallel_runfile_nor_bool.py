import os, sys
sys.path.append('/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators')

from boolean_py import nor_bool

with open('fifosomething.txt', 'w') as fifo:
    print(nor_bool(int(sys.argv[1]),int(sys.argv[2]),), file=fifo)
