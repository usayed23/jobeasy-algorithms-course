#Number 1:
#Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need.
#
# Example:
# paperwork(5, 5) == 25
# Note: if n < 0 or m < 0 return 0!
#
# Waiting for translations and Feedback! Thanks!


def paperwork(n, m):

    if n* m <= 0:
        return 0
    elif m <= 0:
        return 0
    elif n <= 0:
        return 0
    elif n * m > 0:
        BP = n * m
        return BP


#Number 2:
# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
#
# For example:
#
# cockroach_speed(1.08) == 30
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

import math


def cockroach_speed(s):
    cm = s * 27.77778

    return math.floor(cm)



#Number 3:
# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!
#
# Examples
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2


def get_sum(a,b):
    if a == b:
        return a
    s = 0
    for n in range(min(a,b), max(a,b)+1):
        s += n
    return s
