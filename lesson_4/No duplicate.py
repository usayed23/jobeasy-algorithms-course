# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Input
# 'alpha beta beta gamma   gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output
# 'alpha beta gamma delta'


def no_duplicate(string):
    uniq = []
    list_of_words = string.split(' ')
    for word in list_of_words:
        if word not in uniq:
            uniq.append(word)
    return ' '.join(uniq)


print(no_duplicate('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
