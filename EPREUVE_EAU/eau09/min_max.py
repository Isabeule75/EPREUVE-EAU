import re
import sys

def are_digits(nb_min, nb_max):
    if re.search("\D+", nb_min):
        return False
    elif re.search("\D+", nb_max):
        return False
    elif re.search("\d+", nb_min):
        return True
    elif re.search("\d+", nb_max):
        return True

def args_Valid(args):
    if len(args) == 3:
        return True
    else:
        return False

def entre_min_max(nb_min, nb_max):
    for i in range(nb_min, nb_max):
        print(i, end=" ")
        i+1

entre_min_max(int(sys.argv[1]), int(sys.argv[2])) if args_Valid(sys.argv) == True and are_digits(sys.argv[1], sys.argv[2]) == True else sys.exit("Error")
