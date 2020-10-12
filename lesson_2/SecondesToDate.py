# Write a Python program to convert seconds to hour, minutes and seconds.


def sec_to_hms(seconds):
    pass
# **********************************
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f"{hours}:{minutes}:{seconds}")

# **********************************
#     h = (seconds // 3600)
#     print(h)
# **************************************
#     hours = seconds // 3600
#     mins = (seconds - (3600 * hours)) // 60
#     secs = seconds - (3600 * hours) - (mins * 60)
#     print(f'{hours}:{mins}:{secs}')
# ********************************************
#     hours = seconds // 3600
#     seconds = seconds - hours * 3600
#     minutes = seconds // 60
#     seconds = seconds - minutes * 60
#     print(f"{hours}:{minutes}:{seconds}")


# print(sec_to_hms(10121))

# '222:59:59'
#
# import datetime
# sec = 10121
# res = datetime.timedelta(seconds=sec)
# print(res)
