# Write a Python program to check if a given string is an anagram of another given string.
# According to Wikipedia an anagram is direct word switch or word play, the result of rearranging the
# letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once;
# for example, the word anagram can be rearranged into nag-a-ram.
# Example: 'heart' and 'earth'

str1 = input(f"Enter first string: ")
str2 = input(f"Enter second string: ")


def anagram_check(string_1, string_2):
    if string_1 == string_2 or len(string_1) != len(string_2):
        return False
    for char in string_1:
        if string_1.count(char) != string_2.count(char):
            return False
    return True


print(anagram_check(str1, str2))
