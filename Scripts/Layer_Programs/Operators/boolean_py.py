def and_bool(a,b):
    return a and b

def nand_bool(a,b):
    return not (a and b)

def nor_bool(a,b):
    return not (a or b)

def not_bool(a):
    return int(not a)

def or_bool(a,b):
    return a or b

def xor_bool(a,b):
    return a ^ b

print(and_bool(0,1))