# Enter a string of words separated by spaces. Find the longest word. (split / join methods)

def longest_word(words):
    longest_word = ''
    longest_size = 0
    word_list = words.split(" ")

    for word in word_list:
         if (len(word) > longest_size):
             longest_word = word
             longest_size = len(word)

    return longest_word



print(longest_word("my name is umair and i am from NewYork" ))

#***********************************************************************************************************************
#Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string,  and words may be separated by several spaces).
#Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

def empty_spaces(str):

    strip_spaces_list = str.strip().split()

    final_string = " "

    final_string = final_string.join(strip_spaces_list)

    return final_string

print(empty_spaces("      my   name  is  umair   "))

#***********************************************************************************************************************
#CodeWar Problems:

# Name = 7 kyu, Codewars Leaderboard Climber
#
# We all want to climb the leaderboard. Even given some of the massive scores on there, it's nice to know how close you are...
#
# In this kata you will be given a username and their score, your score (not your real score) and you need to calculate how many kata you need to complete to beat their score, by 1 point exactly.
#
# As this is the easy version (harder one to folow at some point in the future), let's assume only Beta kata and 8kyu kata are available. Worth 3 and 1 point respectively.
#
# Return a string in this format: "To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata."
#
# If the total number of kata you need to complete >1000, add "Dammit!" to the end of the string, like so: "To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata. Dammit!"
#
# If your score is higher than the user's already, return "Winning!" and if they are equal, return "Only need one!"
#
# Note: You are looking to complete as few kata as possible to get to your target.

def leader_b(user, user_score, your_score):
    y = user_score - your_score
    z = y % 3
    x = y // 3
    if user_score == your_score:
        return 'Only need one!'
    if user_score < your_score:
        return 'Winning!'
    if user_score > your_score and x + z > 1000:
        return f"To beat {user}'s score, I must complete {x} Beta kata and {z} 8kyu kata. Dammit!"
    if user_score > your_score:
        return f"To beat {user}'s score, I must complete {x} Beta kata and {z} 8kyu kata."


#***********************************************************************************************************************
# name= 7 kyu ,Responsible Drinking
#
# Welcome to the Codewars Bar!
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
#
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.
#
# Examples
# "1 beer"  =>  "1 glass of water"
# "1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"
# Notes
# To keep the things simple, we'll consider that anything with a number in front of it is a drink: "1 bear" => "1 glass of water" or "1 chainsaw and 2 pools" => "3 glasses of water"
# The number in front of each drink lies in range [1; 9]

def hydrate(drink_string):
    y = 0
    z = 0

    for x in drink_string:
        if x.isdigit():
            y = int(x)

            z = z + y

    if z == 1:
        return f'{z} glass of water'

    else:
        return f'{z} glasses of water'


#************************************************************************************************************************
# Name: 7 kyu, Consecutive items
# You are given a list of unique integers arr, and two integers a and b.
# Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.


def consecutive(arr, a, b):
    index = -1

    list_string = map(str, arr)
    l = len(arr)

    if b == arr[l - 1] and a != arr[l - 2]:
        return False

    if a == arr[l - 1] and b != arr[l - 2]:
        return False

    if a == arr[0] and b != arr[1]:
        return False

    if b == arr[0] and a != arr[1]:
        return False

    for x in list_string:
        index += 1

        q = abs(index - 1)

        if x == str(a) and arr[index + 1] == b:
            return True

        elif x == str(b) and arr[index + 1] == a:
            return True


    else:
        return False
