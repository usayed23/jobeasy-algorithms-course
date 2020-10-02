# When a user enters a year, the code detects if it is a leap year or not.

# Leap years have the following characteristics:
# Their number is multiple by 400 or their number is multiple by 4.
# If the year number id multiple by 100, it is not a leap year.

year = int(input('Input a year: '))

if year % 4 != 0:
    print('Not a leap year!')
else:
    if year % 100 != 0:
        print('Is a leap year')
    else:
        if year % 400 == 0:
            print('Is a leap year')
        else:
            print('Not a leap year!')



