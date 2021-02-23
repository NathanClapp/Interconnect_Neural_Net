#supporting functions for udp server

#normal python modules
import subprocess, multiprocessing, sys, os, json
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

#return a list of all the unique modules in the directory
def get_unique_modules(function_argc_list):
    unique_modules = []
    for i in function_argc_list:
        for j in unique_modules:
            if i != j:
                unique_modules.append(i)
            else:
                continue
    return unique_modules

def write_module_list(module_array, filename='/home/nathan/Documents/Code/Interconnect_Neural_Net/module_list.txt'):
    with open(filename, 'w') as file:
        json.dump(module_array, file)

def read_module_list(filename='/home/nathan/Documents/Code/Interconnect_Neural_Net/module_list.txt'):
    with open(filename, 'r') as file:
        return json.load(file)

#returns python list of ints, from tf tensor encoded as string
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

#Do: include typecasting between sys.argv and layer function - modify module array to include a list of dtypes
    #workarea: py_functions_from_modules

'''
-Do: custom type casting later (get type from function signature, include in module array)

working module format - update template:
import os, sys
sys.path.append('/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators')

from boolean_py import and_bool

with open('fifosomething.txt', 'w') as fifo:
    print(and_bool(int(sys.argv[1]),int(sys.argv[2]),), file=fifo)


'''

#make argv strings to accept fifos
def fifo_argv():
    base_string = 'sys.argv[{}]'
    return base_string.format(1)

#write a string reading in as many argv values as the relevant function's argc

def function_argv(argc):
    #argv[0] is the file being called - ignore 1st argument
    #shift up argc to allow fifo input
    argv_index = 2
    argc += 1
    base_string = 'int(sys.argv[{}]),'
    return_string = ''
    while argv_index <= argc:
        return_string += base_string.format(argv_index)
        argv_index += 1
    return return_string

def make_fifo(function_name, parallel_file_directory='/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Parallel_Files/'):
    fifo_name = function_name + '_fifo'
    fifo_folder = 'fifos/'
    os.popen('cd ' + parallel_file_directory + fifo_folder + ' && '
                    'mkfifo ' + fifo_name)
    return fifo_name

#Do: mark off decoded tensor values as function inputs are filled (keep 1-1 map)
    #right now the file writer assumes that there are exactly as many elements in the input tensor as there are parallel run files (same as function count)
#Do: make a function to assign FIFO files (see: man mkfifo)

#take a list of lists such as: [module_name, function_name, function_input_count]
#write files for each function, per the template file
def write_runner_files(modules_list,
    operator_root_dir = '\'/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Operators\'', #file writing removes 1 layer of quotes & 1 layer is needed for the parallel files
    parallel_file_directory='/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Parallel_Files/',
    in_filename= 'template.txt',
    out_filename='parallel_runfile_{}.py'):

    #function argv and file argv are mutually exclusive
    keywords_dict = {'operator_root_dir':'','module_name':'', 'function':'', 'argv':'', 'out_fifo':''}

    #read in template py file
    with open(parallel_file_directory + in_filename, 'r') as in_file:
        in_file = in_file.readlines()
    #iterate through all functions
    print(modules_list[1])
    for i in range(modules_list[1]):
        #map module/function/argc values from modules_list to dict
        #make this less manual/compatible with more key/value pairs
        keywords_dict['operator_root_dir'] = operator_root_dir
        keywords_dict['module_name'] = modules_list[0][i][0]
        keywords_dict['function'] = modules_list[0][i][1]
        #get argc
        argument_count = modules_list[0][i][2]
        keywords_dict['argv'] = function_argv(argument_count)
        #extra arguments for input and output files
        keywords_dict['out_fifo'] = fifo_argv()

        print(keywords_dict)

        #writing run files - assign function name to each runfile
        with open(parallel_file_directory + out_filename.format(keywords_dict['function']), 'w') as out_file:
            for line in in_file:
                for keyword in keywords_dict:
                    if keyword in line:
                        #replace generic keywords with strings from modules_list
                        line = line.replace(keyword, keywords_dict[keyword])
                out_file.write(line)
        
        #writing fifos
        fifo_name = make_fifo(function_name=keywords_dict['function'])
        print(fifo_name)

    return True

#take created run files and the parsed tensor
#generate fifos for each file (unique ids)
#
#def parallel_run(parallel_file_directory='/home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/Layer_Programs/Parallel_Files/'):



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

print(function_argv(5))

write_runner_files(modules_list=module_array,)
                    #decoded_tensor=[1,2,3,4,5,6])
