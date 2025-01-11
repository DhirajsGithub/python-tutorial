#adding items to our list

#adding elements from last position :
from typing import Collection


fruits = ["mango", "grapes"]
fruits.append("apple")                  #this will add apple from last to list
print(fruits)             

fruits = []
fruits.append("mango")
print(fruits)
#yek bar main yek hi item add kar sakte hain


#adding elements to desire position :
fruits1 = ['mango', "orange"]
fruits1.insert(1,"apple")
print(fruits1)
fruits1.insert(20, "apple")
print(fruits1)

#list concatenation :
fruits2 = ["banana", "papaya"]
fruits_coll = fruits1 + fruits2           #order will be same pahale fruits1 ke elements then fruits2 ke element     
print(fruits_coll)

#extendig list by adding other list elements:
#adding elements of fruits1 to fruits2
fruits2.extend(fruits1)
print(fruits2)
# NOTE: any iterable can be extend with list or any mutable data type (4 built in data type)

fruits2.append(fruits1)
print(fruits2)                        #append will directly insert puri list inside list
 


print("----------------------------")
fruits2 = ["banana", "papaya"]
fruit1 = ["apple", "watermaleion"]
l = fruit1 + fruits2
print(l)
