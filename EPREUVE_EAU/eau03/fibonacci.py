import sys
import re

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

def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(int(sys.argv[1]))) if args_Valid(sys.argv) == True else sys.exit("Too few or too many digit arguments")
