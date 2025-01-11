# A date in Python is not a data type of its own, but we can import a module
# named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)             # year, month, day, hour, minute, second, and microsecond.

# the datetime module has many method to return information check on google or W3 school
print(x.strftime("%A"))         # Day full version like monday of the present date

print(x.strftime("%a"))         # Day short version like mon of the present date
print(x.strftime("%w"))         # 0 is sunday and 1 is monday and so on



# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
y = datetime.datetime(2022, 1, 31)

print(y.strftime("%A"))




