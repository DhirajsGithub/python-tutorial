#min and max function:
numbers = [2,20,2,0]
min_num = min(numbers)
print(min_num)
print(max(numbers))

#define a function which will give a greatest difference:
def greatest_diff(list):
    return max(list)-min(list)

print(greatest_diff([1,2,3,4,5,6]))

#define a function which takes list inside list and return how many list inside our list:
def sublist_counter (elements):
    total = 0
    for element in elements:
        if type(element)==list:
            total = total + 1
            # total += 1
    return total
print(sublist_counter([1,[2],3,[34],[5,67]]))