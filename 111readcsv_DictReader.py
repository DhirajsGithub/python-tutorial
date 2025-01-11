from csv import DictReader
# ordered dict
with open('110file.csv', 'r') as rf:
    csv_reader = DictReader(rf)
    # print(csv_reader)
    # print(next(csv_reader))
    # print(next(csv_reader))
    # print(next(csv_reader))
    for row in csv_reader:
        print(row)
        # print(row.get('name'))
    # it will take first row as key(headers) and rest rows as vaulues 


# with open('110file.csv', 'r') as rf :
# note if we are using '|' instead of ',' we have to determine delimiter 
#     csv_reader = DictReader(rf, delimiter = '|')
#     for row in csv_reader:
#         print(row)