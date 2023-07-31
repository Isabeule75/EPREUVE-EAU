import re
import sys

def are_letters(args):
    if re.search("\d+", args[1]):
        return False
    elif re.search("\d+", args[2]):
        return False
    else:
        return True

def args_Valid(args):
    if len(args) == 3 and are_letters(args):
        return True
    else:
        return False

def str_in_str(my_string, string_to_find):
    i=0
    while my_string[i]:
        j=0
        while string_to_find[j] == my_string[i + j]:
            if string_to_find[j + 1]:
                return True
            j=j+1
        i=i+1
        while string_to_find[j] != my_string[i + j]:
            return False

print(str_in_str(sys.argv[1], sys.argv[2])) if args_Valid(sys.argv) == True else sys.exit("Error")
