# User enters a string from a keyboard. Write a Python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

from lesson_3.Reverse_string import reversed_string

string = input(f"Enter a string: ")


def palindrome_check(given_string):
    reversed_string_value = reversed_string(given_string)
    return reversed_string_value == given_string


print(palindrome_check(string))
