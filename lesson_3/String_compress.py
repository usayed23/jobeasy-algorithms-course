# When given a string the the code checks if there are repetitive characters and deletes all repetitions,
# leaving the first number in place followed by the number of repetitions.

string1 = input(f"Enter a string: ")


def str_compress(string):
    counter = 1
    result = string[0]
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
                counter = 1
            result += string[index + 1]
    else:
        if counter > 1:
            result += str(counter)
    return result





print(str_compress(string1))

# TODO: Write a function for decompressing string “a4b3c2d” => "aaaabbbccd"
