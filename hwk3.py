#Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD C

# string1 = "cvcbbvbbbbduhuhudjdnjdbcccjcbauiuibbjjiodubbciia"
# string2 = 'i'
#
# def sub_count(str1,str2):
#
#     counter = 0
#     for x in str1:
#         if x == str2:
#             counter += 1
#
#     return f'The Character {str2} is {counter} times in a string'
#
# print(sub_count(string1,string2))


#Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE
#
# string3 =input("Please enter a string to edit")
# string4 =input("Please enter a substring to be replaced")
# string5 =input("Please enter a replacement substring")
#
#
#
# def replace_string(str3,str4,str5):
#     holder_string = ""
#     for x in str3:
#         if x or x[range(0,len(str4))] == str4:
#            holder_string = str3.split(str4)
#            final_string = str5.join(holder_string)
#
#
#
#            return final_string
#
#
#
# print(replace_string(string3,string4,string5))


#* TODO: Write a function for decompressing string “a4b3c2d”
#
# string6= "a4b3c2d"
#
# def decompressing(str6):
#     index = -1
#     q = ""
#
#
#     for x in str6:
#         index += 1
#         if x.isdigit():
#             z = int(x)
#             h_string = str6[index-1] * z
#             f_string = q+h_string
#             q = f_string

#     return f_string+str6[len(str6)-1]

# print(decompressing(string6))





#Recursion for Fib, factorial, digital root

#n = int(input('Input a number'))

# def rec_factorial(number):
#     result = 1
#
#     if number < 0:
#         print("Error")
#
#     elif number == 0:
#         return 1
#     elif number > 0:
#
#          result1 = 0
#          result = rec_factorial(number-1)*number
#
#
#     return result
#
# print(rec_factorial(n))

#
# def rec_digital_root(y):
#     sum_of_all_1 = 0
#     k=str(y)
#     for x in k:
#         if x.isdigit():
#             single_int = int(x)
#             sum_of_all_1 = sum_of_all_1 + single_int
#
#     if len(str(sum_of_all_1)) > 1:
#         sum_of_all_1 = rec_digital_root(sum_of_all_1)
#
#     return (sum_of_all_1)
#
# print(rec_digital_root(7))
#

