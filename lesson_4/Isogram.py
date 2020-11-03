# Isogram is a word with no repeating letters, in a row or not. Create a Python function to check is word isogram.
# Empty string - isogram. Case doesn't matter.


def is_isogram(string):
    if len(string) == 0:
        return True
    string = string.lower()
    uniq = ''
    for char in string:
        if char in uniq:
            return False
        uniq += char
    return True


print(is_isogram('helol'))
