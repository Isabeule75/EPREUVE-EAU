import sys
import re

def are_letters(arg):
    if re.search("\D+", arg):
        return True
    return False

def args_Valid(args):
    if len(args) == 2:
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
    print()

arguments = sys.argv[1]
majuscule_sur_2(arguments) if args_Valid(sys.argv) and are_letters(arguments) else sys.exit("Error")
