# TODO: Write a function for decompressing string “a4b3c2d”

def decompress_string(string):
    result = ''
    char = ''
    count = ''

    for current_char in string:
        if current_char.isalpha():
            if count != '':
                result += char * (int(count) - 1)
                count = ''
            char = current_char
            result += char
        else:
            count += current_char
    else:
        if count != '':
            result += char * (int(count) - 1)
    return result


print(decompress_string('a5b4c3d4'))