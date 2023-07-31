import re
import sys

def are_letters(args):
    if re.search("\d+", args[1]):
        return False
    else:
        return True

def args_Valid(args):
    if len(args) == 2 and are_letters(args):
        return True
    else:
        return False

def majuscule_sur_2(arg):
    s=arg
    new_s=""
    for i in range(len(s)):
        if i%2==0:
            new_s=s[i].upper()
        else:
            new_s=s[i]
        print(new_s, end="")

majuscule_sur_2(sys.argv[1]) if args_Valid(sys.argv) == True else sys.exit("Error")
