# Enter a string of words separated by spaces. Find the longest word.

string = input(f"Enter a string: ")


def longest_word(string_1):
    substring = ''
    result = ''
    counter = 0
    maximum = 0
    for char in string + ' ':
        if char == ' ':
            if counter > maximum:
                maximum = counter
                result = substring
            counter = 0
            substring = ''
        else:
            counter += 1
            substring += char
    return result

print(longest_word(string))
