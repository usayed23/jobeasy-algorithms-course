# Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.
# Shortest Word

def find_short(s):
    i = 0

    list_string = s.split()

    return min(map(len, list_string))


# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
#
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:
#
# setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) -> false setAlarm(true, false) -> true
#
# setalarm(true, true) -> false
# setalarm(false, true) -> false
# setalarm(false, false) -> false
# setalarm(true, false) -> true


def set_alarm(employed, vacation):
    if employed and vacation == 1:
        return False

    if employed == True and vacation == 0:

        return True

    else:

        return False





# Here we have a function that help us spam our hearty laughter. But is not working! I need you to find out why...
#
# Expected results:
#
# spam(1)  ==> "hue"
# spam(6)  ==> "huehuehuehuehuehue"
# spam(14) ==> "huehuehuehuehuehuehuehuehuehuehuehuehuehue"


def spam(number):
    return 'hue'* number