def and_bool(a,b):
    return int(a and b)

def nand_bool(a,b):
    return int(not (a and b))

def nor_bool(a,b):
    return int(not (a or b))

def not_bool(a):
    return int(not a)

def or_bool(a,b):
    return int(a or b)

def xor_bool(a,b):
    return int(a ^ b)
