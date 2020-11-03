# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE


# string = input(f"Input string: ")
# old_substr = input(f"Input substring which you want to change: ")
# new_substr = input(f"Input new substring for changing: ")


def replace(string_1, old_substr_1, new_substr_1):
    len_old_string = len(old_substr_1)
    index = string_1.find(old_substr_1)
    while string_1.find(old_substr_1, index) > -1:
        string_1 = f'{string_1[:index]}{new_substr_1}{string_1[index + len_old_string:]}'
        index = string_1.find(old_substr_1, index + 1)
    return string_1



print('aaaabbaaabbaaaa'.replace('aa', 'a'))
print(replace('aaaabbaaabbaaaa', 'aa', 'a'))


# print('hello world'.find('o', 6, 8))
# 'hello world'[6:8].find('o')