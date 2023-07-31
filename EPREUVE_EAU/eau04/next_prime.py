import re
import sys

def is_digit(args):
    if re.search("\d+", args[1]):
        return True
    else:
        return False

def args_Valid(args):
    if len(args) == 2 and is_digit(args):
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

print(next_prime(int(sys.argv[1]))) if args_Valid(sys.argv) == True else sys.exit("Error")
