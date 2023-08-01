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

def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

argument = sys.argv[1]
print(fibonacci(int(argument))) if args_Valid(sys.argv) == True and are_digits(argument) == True else sys.exit("Error")
