from csv import DictReader, DictWriter
with open('113file.csv', 'w', newline='') as wf:
    csv_writer = DictWriter(wf, fieldnames=['firstname', 'lastname', 'age'])
    csv_writer.writeheader()
    # all that shitty headers man !

    # csv_writer.writerow({
    #     'firstname': 'Harshith',
    #     'lastname' : 'vashishtha',
    #     'age' : 30
    # })
    # csv_writer.writerow({
    #     'firstname' : "harshith",
    #     'lastname' : 'vashishtha',
    #     'age' : 30
    # })

    # writerows
    csv_writer.writerows([
        {'firstname': "harshith", 'lastname': 'vashishtha', 'age': 30},
        {'firstname': "mohit", 'lastname': 'borse', 'age': 20},
        {'firstname': "rajesh", 'lastname': 'mehata', 'age': 10}
    ]
    )
