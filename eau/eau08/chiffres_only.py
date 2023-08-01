import re
import sys

def args_Valid(args):
    if len(args) > 2:
        return True
    else:
        return False

def are_digits(args):
    if re.search("\D+", args):
        return False
    else:
        return True

print(are_digits(sys.argv[1::])) if args_Valid(sys.argv) == True else sys.exit("Error")
