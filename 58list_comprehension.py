#list comprehension
#with the help of list comprehension we can make list in one line

#make a list of squares of numbers from 1 to 10
# squ_num = []
# for i in range(1,11):
#     squ_num.append(i**2)

# print(squ_num)

squ_num_short = [i**2 for i in range(1,11)]
print(squ_num_short)

#negative numbers
negative_num = []
for i in range (1,11):
    negative_num.append(-i)
print(negative_num)

negative_num_short = [-i for i in range(1,11)]
print(negative_num_short)

#first char
names = ['harshal', 'rohit', 'mohit', 'chetan']
first_char = []
for name in names :
    first_char.append(name[0])
print(first_char)

first_char_short = [name[0] for name in names]