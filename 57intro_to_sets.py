#set data type
#unordered collection of unique itmes
from turtle import pen
import _tkinter

s = {1,2,3,4,4}
print(s)

l = [1,2,2,2,3,44,55,66,55,1]
print(l)
#remove duplicate
# new_l = set(l)        #type is set and no duplicates
new_list = list(set(l))      #type is list and no duplicates
#it will create a new list that doesn't contain duplicates
print(new_list)

#accesing set :
new_s = {1,2}
print(f"new set is {new_s}")
#adding unique item in set
new_s.add(3)
new_s.add(4)
new_s.add(3)     #won't repeat it
print(f"after adding new set is {new_s}")

# note imp: 1 = True and  0 = False, so we cannot add boolean if 1 and 2 both present and cannot add True if 1 present and false if 0 present 

#removing itmes from set
new_s.remove(1)
# new_s.remove(7)      #jo hain hi nahi agar use remove karege toh error ayega
new_s.discard(9)     #jo hain hi nahi agar use discard karege toh error nahi ayega just kuch nahi hoga
print("after removing items {}".format(new_s))

# to take copy of set
copy_s = new_s.copy()
copy_s.add(0)
print(copy_s)
print(new_s)

#we can store most of the items in set except for list and dictionary and set itself
new_set = {1,2,2.0, "string", None}
print(new_set)
# new_set_2 = {1,2,2.0, "string", None, ['darshan raval', 'arijit sing'], {'key1': 'value1'}}  #error


#in keyword in set 
def_set = {1,2,3,'a','b','c'}
if 'a' in def_set :
    print("present")
else :
    print("not present")

#for loop
for item in def_set :
    print(item)


#set maths
#union() method     ---> returns a new set containing all items from both set
def_set_2 = {2,3,'c','z','x'}
union_set = def_set | def_set_2     #all unique items from two or more sets
print(union_set)    

#intersection 
intersection_set = def_set & def_set_2    #all common items form two or more sets
print(intersection_set)

# intersection_update()
print("--------comman_items update set-------------")
def_set.intersection_update(def_set_2)          # updates the set 'def_set' to common elements
print(def_set)                  # will print only comman items from both sets
print(def_set_2)                # will print whole def_set_2. by syntax



print("----------not_comman_items update set-------------")
# symmetric _difference_update() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

print("-------------symetric difference------------")
# symmetric_difference() returns a new set 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

zz = x.symmetric_difference(y)    # (x | y) - (x & y)
print(zz)




 