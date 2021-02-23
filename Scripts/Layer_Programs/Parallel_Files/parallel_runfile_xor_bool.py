import os, sys
sys.path.append('/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators')

from boolean_py import xor_bool

with open(sys.argv[1], 'w') as fifo:
    print(xor_bool(int(sys.argv[2]),int(sys.argv[3]),), file=fifo)
