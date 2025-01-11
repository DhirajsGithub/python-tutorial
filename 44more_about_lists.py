#generate lists with range functions:
numbers = [1,2,3,4,5,6,7,8,9,10,1,5,7,8,1]
print(numbers)
# numbers.pop()
# print(numbers) 
# print(numbers.pop())           #jo pop kiya huae element hai woh store bhi hota hain

print(numbers.index(1))            #numbers.index(what_to_find, where to start, where to end)

# print(numbers.index(1,1))
print(numbers.index(1, 10, 149))      # 1 ko find karo from indexing 11 se lekar 14 tak
# first_1 = (numbers.index(1))
# print(numbers.index(1,first_1+1,len(numbers)))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))

