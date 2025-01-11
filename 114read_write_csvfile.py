# writer DictWriter

from csv import DictReader, DictWriter
import csv

with open('113file.csv', 'r') as rf:
    with open('114file.csv', 'w') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['first_name', 'last_name', 'age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname, lname, age = row.get('firstname'), row.get('lastname'), row.get('age')
            csv_writer.writerow({
                'first_name' : fname,
                'last_name' : lname,
                'age' : age
            })