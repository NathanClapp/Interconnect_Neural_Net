#supporting functions for udp server

#normal python modules
import subprocess, multiprocessing, sys, os

#get this path automatically later
root_dir = '/home/nathan/Documents/Code/Interconnect_Neural_Net'
sys.path.append(root_dir + '/Scripts/Layer_Programs/Operators')

from Boolean_Py import buffer,and_bool,or_bool,nand_bool,nor_bool,not_bool,or_bool,xor_bool

#returns python list of ints
def parse_tensor(decoded_tensor):
    #remove brackets and convert to list
    return [int(i) for i in decoded_tensor.replace('[','').replace(']','').split()]

#print(parse_tensor('[1 2 1 4]'))

#make as many named pipes as there are array elements (+1 default pipe on startup for exporting pipe count)
#send data to pipe
#use mkfifo
#subprocess.run()


#make parallel evaluation processes, 1 for each data point
def run_container_modules(arg_count, list_tensor):
    #make 1 process for each function/file in the module directory
#    if arg_count == len(list_tensor):
#        continue

    #in each process, pipe data to a unique function, concatenate output, and return
    #subprocess.run('/')
#    else:
#        print("Error: data/operator mismatch")
    return pipe_ids

#def collect_data


