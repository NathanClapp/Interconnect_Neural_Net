#supporting functions for udp server

#normal python modules
import subprocess, multiprocessing, sys, os, json, types
from inspect import signature, getmembers

#get this path automatically later
operator_root_dir = '/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators'
#json_module_dir = 

#
def py_modules(module_name_string):
    modules_list = []
    modules_list.append(sys.modules[module_name])

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

operator_modules = py_modules_from_directory(operator_dir=operator_root_dir)
print(operator_modules)

#workspot
#def module_object_to_string(module_name):

def nested_data_template(module_name_string, function, function_argc):
    return [ module_name_string, [function,  function_argc] ]

print(nested_data_template(operator_modules[0], 'testfuncstr', 5))
print(dir(operator_modules[0]))

#get every function and the number of inputs for each, for all modules in modules list
#return a structured json array of module_name(function_name(input_count))
#ignore builtin methods by default
def py_functions_from_modules(modules_list, ignore_substring='__'):
    function_cumulative_argc = 0
    function_argc_dict = {}
    #open json and prepare for writing
    for module_name in modules_list:
        for function in dir(module_name):
            #ignore functions beginning or ending in '__', such as __init__
            if not (function.startswith(ignore_substring) or function.endswith(ignore_substring)):
                #find number of parameters each function takes
                function_argc = len(signature(getattr(module_name, function)).parameters)
                #total parameter count
                function_cumulative_argc += function_argc
                function_argc_dict.update({function : function_argc})
    return [function_argc_dict, function_cumulative_argc]

print(py_functions_from_modules(operator_modules))



#returns python list of ints
def parse_tensor(decoded_tensor):
    #remove brackets and convert to list
    return [int(i) for i in decoded_tensor.replace('[','').replace(']','').split()]

#print(parse_tensor('[1 2 1 4]'))

#make as many named pipes as there are array elements (+1 default pipe on startup for exporting pipe count)
#send data to pipe
#use mkfifo
#subprocess.run()

#known arg count for boolean py module
arg_count = 14
inputs_functions = [()]

def run_general_modules(arg_count, list_tensor):
    #make 1 process for each function/file in the module directory
    #for i in 


    #in each process, pipe data to a unique function, concatenate output, and return
    #subprocess.run('/')
    #else:
        #return 
    return pipe_ids



#def collect_data

#print(boolean_py.and_bool(1,1))
