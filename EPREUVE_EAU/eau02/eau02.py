import sys

def args_Valid(args):

    if len(args) < 2:
        return False
    else:
        return True

def print_reverse_args(args):
    for arg in args[:0:-1]:
        print(arg)


print_reverse_args(sys.argv) if args_Valid(sys.argv) == True else sys.exit("Too few arguments")
