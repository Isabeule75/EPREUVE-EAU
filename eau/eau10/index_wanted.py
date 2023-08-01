import sys

def args_Valid(args):
    if len(args) < 2:
        return False
    else:
        return True

def index_wanted(args, last_arg):
    arg_to_find_index = ""
    arg_to_find_index = [index for (index, element) in enumerate(args) if element == last_arg]
    print(arg_to_find_index)

index_wanted(sys.argv[1:-1], sys.argv[-1]) if args_Valid(sys.argv) == True else sys.exit("Error")



"""print(sys.argv[-1])
print(sys.argv[-2])
print(sys.argv[1:-1])"""

