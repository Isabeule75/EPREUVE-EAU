import sys

def are_digits(arguments):
    for arg in arguments:
        if not arg.isdigit():
            return False
    return True

def args_Valid(args):
    if len(args) == 2:
        return True
    else:
        return False

def is_prime(nb):
    i = 2
    if nb < 2:
        return -1
    while(i <= nb/i):
        if nb%i == 0:
            return False
        i=i+1
    return True

def next_prime(nb):
    if nb < 2:
        return 2
    i = nb
    while is_prime(i) == False:
        i=i+1
    return i

arguments = sys.argv[1]
print(next_prime(int(arguments))) if args_Valid(sys.argv) == True and are_digits(arguments) else sys.exit("Error")
