#supporting functions for udp server

#normal python modules
import subprocess, multiprocessing, sys, os, json, types
from inspect import signature, getmembers

#get this path automatically later
operator_root_dir = '/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators'

#import files in the given directory as modules
#return list of modules
def py_modules_from_directory(operator_dir):
    newline = '\n'
    file_suffix = '.py'
    exec_path_append = 'sys.path.append(operator_dir)' + newline
    modules_list = []
    #import modules in directory
    for file in os.listdir(operator_dir):
        if file.endswith(file_suffix):
            #remove '.py' suffix and import
            module_name = file.replace(file_suffix, '')
            exec(exec_path_append + 'import ' + module_name)
            modules_list.append(sys.modules[module_name])
    return modules_list

#get every function and the number of inputs for each, for all modules in modules list
#return a structured json array of module_name(function_name(input_count))
#ignore builtin methods by default
def py_functions_from_modules(modules_list, ignore_substring='__'):
    function_cumulative_argc = 0
    functionc = 0
    function_argc_list = []
    #open json and prepare for writing
    for module_object in modules_list:
        for function in dir(module_object):
            #ignore functions beginning or ending in '__', such as __init__
            if not (function.startswith(ignore_substring) or function.endswith(ignore_substring)):
                #find number of parameters each function takes
                function_argc = len(signature(getattr(module_object, function)).parameters)

                #parameter and function counts
                function_cumulative_argc += function_argc
                functionc += 1

                function_argc_list.append([module_object.__name__, function, function_argc])

            #list of lists: each sub-array is formatted as:
            #[module_name, function_name, function_input_count]
    return [function_argc_list,
            #number of functions
            functionc,
            #sum of inputs for all functions all modules in the modules_list
            function_cumulative_argc]

def write_module_list(module_array, filename='module_list.txt'):
    with open(filename, 'w') as file:
        json.dump(module_array, file)

def read_module_list(filename='module_list.txt'):
    with open(filename, 'r') as file:
        return json.load(file)

#returns python list of ints
def parse_tensor(decoded_tensor):
    #remove brackets and convert to list
    return [int(i) for i in decoded_tensor.replace('[','').replace(']','').split()]

#for arbitrary language implementation
# {
#make as many named pipes as there are array elements (+1 default pipe on startup for exporting pipe count)
#send data to dynamically created pipes
#use mkfifo
#subprocess.run()


#def run_general_modules(arg_count, list_tensor):
    #make 1 process for each function/file in the module directory

    #in each process, pipe data to a unique function, concatenate output, and return
    #subprocess.run('/')
    #else:
        #return 
#    return output_list
# }

#take a list of lists such as: [module_name, function_name, function_input_count]
#mark off decoded tensor values as function inputs are filled (keep 1-1 map)
#run as many parallel processes as there are functions
def write_runner_files(modules_list, filename='parallel_runfile{}.py'):
    #may be better to just run multiple udp servers after parsing tensor client-side
    if modules_list[2] == len(decoded_tensor):
        for i in range(len(modules_list[1])):
            with open(filename.format(i)) as file:
                file.write('import os\n')
                file.write('')




#    return 0;


operator_modules = py_modules_from_directory(operator_dir=operator_root_dir)
print(operator_modules)


print(dir(operator_modules[0]))

module_array = py_functions_from_modules(operator_modules)
print(module_array)

print('\n')

print(type(read_module_list()))

#list of lists: each sub-array is formatted as:
#[module_name, function_name, function_input_count]
print(module_array[0])
#number of functions
print(module_array[1])
#sum of inputs for all functions all modules in the modules_list
print(module_array[2])

print(parse_tensor('[1 2 1 4]'))
