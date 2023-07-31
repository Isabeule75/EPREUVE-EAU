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

def majuscule_letter_1(arg):
    s=arg
    new_s = ""
    code = ord(s[i])
    new_s = chr(code - 32) + s[1:]
    while s[i]:
        i=1
        if s[i-1] < '0' and s[i-1] > '9' or s[i-1] < 'a' and s[i-1] > 'z' or s[i-1] < 'A' and s[i-1] > 'Z':
            if s[i] >= 'a' and s[i] <= 'z':
                code = ord(s[i])
                new_s = chr(code - 32) + s[i1:]
    print(new_s)

majuscule_letter_1(sys.argv[1]) if args_Valid(sys.argv) == True else sys.exit("Error")
