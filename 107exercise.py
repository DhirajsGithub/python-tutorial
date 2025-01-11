with open('107salary.txt', 'r') as rf:
    with open('107output.txt', 'w') as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f'{name}\'s salary is {salary}')