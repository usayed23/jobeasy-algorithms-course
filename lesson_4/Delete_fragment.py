# Given a string. Character “h” is included as minimal two times.
# Delete from given string first and last h - characters and all characters between them.


def delete_fragment(string, char):
    first = 0
    last = 0
    index = 0
    while index < len(string):
        if string[index] == char:
            first = index
            break
        index += 1

    index = len(string) - 1
    while index >= 0:
        if string[index] == char:
            last = index
            break
        index -= 1

    return f'{string[:first]}{string[last + 1:]}'

print(delete_fragment('qwertyhuhasdfghzxcvrbnhm', 'r'))
