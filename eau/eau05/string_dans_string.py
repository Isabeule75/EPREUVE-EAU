import sys

def are_only_letters(arguments):
    for arg in arguments:
        if not arg.isalpha():
            return False
    return True

def args_Valid(args):
    if len(args) == 3:
        return True
    else:
        return False

def str_in_str(string, substring):
    i = 0
    j = 0
    len_sub = len(substring)
    len_str = len(string)
# Parcourir la chaîne principale
    while i < len_str:
# Comparer les caractères entre les deux chaînes
        if string[i] == substring[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
# Vérifier si on a trouvé la sous-chaîne dans la chaîne principale
        if j == len_sub:
            print("True")
            return

    print("False")

arguments = sys.argv[1::]
str_in_str(sys.argv[1], sys.argv[2]) if are_only_letters(arguments) and args_Valid(sys.argv) else sys.exit("Error")
