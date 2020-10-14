
# Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.


def areYouPlayingBanjo(name):
    name_list = list(name)
    name_first_string = str(name_list[0])

    if "r"  == name_list[0]:

        return name + " plays banjo"

    if "R" == name_list[0]:

        return name + " plays banjo"
    else:

        return name + " does not play banjo"



#*********************************************************************************

#You Can't Code Under Pressure #1
#Code as fast as you can! You need to double the integer and return it.


def double_integer(i):
    z = i * 2

    return z


