# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string,
# and words may be separated by several spaces). Make the string regular (delete all spaces at the beginning and
# end of the string, leave one space separating words).

string_1 = input(f"Enter a string: ")


def normalize(string):
    # option 1
    # return ' '.join(string.split())

    # option 2
    while string[0] == ' ':
        string = string[1:]
    while string[-1] == ' ':
        string = string[:-1]
    index = 0
    while index < len(string):
        if string[index] == ' ' and string[index + 1] == ' ':
            string = string[:index] + string[index + 1:]
        else:
            index += 1
    return string

print(normalize(string_1))
