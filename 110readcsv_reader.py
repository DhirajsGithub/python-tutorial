from csv import reader
import csv

with open('110file.csv', 'r') as rf:
    csv_reader = reader(rf)
    print(type(csv_reader))
    # iterator
    print(next(csv_reader))
    for row in csv_reader:
        print(row)
    # since it's a iterator so we can apply only one time for loop hence we can convert iterator to list as 
    # li = list(csv_reader)
    
    