import sys
import re

def are_digits(array):
    pattern = re.compile("\d+")
    res=""
    for arg in array:
        match = pattern.search(arg)
        if match is not None:
            res.append(int(match.group()))
            return True
        else:
            return False

def args_Valid(args):
    if len(args) > 2:
        return True
    else:
        return False

def tri_a_bulle(array, n):
    tab = array
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

def main():
    i = 0
    tab = array
    n = len(array)
    tri_a_bulle(array)
    while i < n:
        print(int(tab[i]))
        i=i+1

array = sys.argv[1::]
int_array = [int(i) for i in array]
print(tri_a_bulle(array, len(array))) if args_Valid(sys.argv) == True and are_digits(array) == True else sys.exit("Error")
