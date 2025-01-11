# zip function
user_id = ['usser1', 'user2', 'user3']
names = ['Harshit', 'Mohit', 'Rhoit', 'Harshal']
last_name = ['vashishtha','vashishtha','sharma']

# ('user1', 'Harshit'), ('user2', 'Mohit'), ('user3', 'Rohit')

# print(zip(user_id, names))
print(tuple(zip(user_id, names)))
print(list(zip(user_id, names)))

example = [('a', 1), ('b', 2)]
print(dict(example))

print(dict(zip(user_id, names)))
print(list(zip(user_id,names, last_name)))

# print(dict(zip(user_id,names, last_name)))    #error can't take more than key value


l1 = [1,3,5,7]
l2 = [2,4,6,8]  


# * operator with zip 
l = list(zip(l1,l2))
print(l)
# [(1, 2), (3, 4), (5, 6), (7, 8)]    #---(1)

# with (1) convert it into lists like l1 and l2  i.e zip unpacking
l1, l2 = list(zip(*l))
print(l1)
print(l2)
print(list(l1)) 
# print(dict(l1))    # error

#make a list which store the max of the pair in l
new_list = []
for pair in zip(l1, l2):
    new_list.append(max(pair))

print(new_list)