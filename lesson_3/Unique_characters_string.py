# When given a string the code deletes all duplicates leaving only one of each character.

string1 = input(f"Enter a string: ")


def unique_characters_string(string):
    result = ''
    for char in string:
        if result.count(char) == 0:
            result += char
    # return ''.join(set(string))


result_variable = unique_characters_string(string1)
print(result_variable)
