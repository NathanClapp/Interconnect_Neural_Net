#miscellaneous supporting functions for udp server

import subprocess, multiprocessing

#returns python list of ints
def parse_tensor(decoded_tensor):
    #remove brackets and convert to list
    return [int(i) for i in decoded_tensor.replace('[','').replace(']','').split()]

#print(parse_tensor('[1 2 1 4]'))

#make as many named pipes as there are array elements (+1 default pipe on startup for exporting pipe count)
#send data to pipe
#use mkfifo
#subprocess.run()

# need unique pipe names
#instead of running 2 scripts for each data movement, pipe data straight to processing scripts
#make parallel evaluation processes, 1 for each data point
def run_container_modules(list_tensor):
    #make pool of processes

    #in each process, pipe data to a unique function, concatenate output, and return
    subprocess.run('/')
    return pipe_ids

