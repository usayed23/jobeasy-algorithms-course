# Write a Python function, which will count how many times a character (substring)
# is included in a string. DON’T USE METHOD COUNT

# string = input(f"Enter a string ")
# substring = input(f"Enter a substring ")


def count(given_string, given_substring):
    counter = 0
    if len(given_string) < len(given_substring):
        return counter

    index = given_string.find(given_substring)
    while index > -1:
        given_string = given_string[index + len(given_substring):]
        index = given_string.find(given_substring)
        counter += 1
    return counter

print(count('hello world of heroes', 'he'))
print('hello world of heroes'.count('he'))
