import os, sys
sys.path.append('/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators')

from boolean_py import not_bool

with open(sys.argv[1], 'w') as fifo:
    print(not_bool(int(sys.argv[2]),), file=fifo)
