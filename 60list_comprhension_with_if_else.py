# list comprehesion with if else statement 
nums = list(range(0,11))

new_list = []
for i in nums :
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)

print(new_list)

new_list_short = [i*2 if (i%2==0) else -i for i in nums]
print(new_list_short)
#syntax dhyan se dekho bhai