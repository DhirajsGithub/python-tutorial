from csv import writer
import csv
from os import write

with open('112file.csv', 'w', newline='') as rf:
    # newline='' will terminate the line which are there after every row 
    csv_writer = writer(rf)
    # methods - writerow, writerows 
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['harshit', 'India'])

    # writerows method
    # csv_writer.writerow
    csv_writer.writerows([['name', 'country'], ['mohit', 'India'], ['hrashit', 'India']])
