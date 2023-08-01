import sys

def args_Valid(arguments):
    if len(arguments) == 2:
        return True
    return False
   
def are_letters(arg):
    for char in arg:
        if not char.isalpha():
            return False
        return True

def capitalize_first_letter(string):
    result = ""
    index = 1
    if ord('a') <= ord(string[0]) <= ord('z'):
        result += chr(ord(string[0]) - 32)
    while index < len(string): 
        if string[index - 1] == ' ' or string[index - 1] == '\t' or string[index - 1] == '\n':
            if ord('a') <= ord(string[index]) <= ord('z'):
                result = result + chr(ord(string[index]) - 32)
            else:
                result = result + string[index]
        else:
            if ord('A') <= ord(string[index]) <= ord('Z'):
                result = result + chr(ord(string[index]) + 32)
            else:
                result = result + string[index]
        index = index + 1
    return result

argument = sys.argv[1]
sortie = capitalize_first_letter(argument)
print(sortie) if args_Valid(sys.argv) and are_letters(argument) else sys.exit("Error")

