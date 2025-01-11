#string 
#collection of characters inside single quotes or double quotes

first_name = "Harshit"
last_name = "vashishtha"
full_name = first_name +" "+last_name
# print(full_name)
# print(full_name + 3)    # erroe kyunki apn string ko number ke sath nahi jod sakte
print(full_name, 3)    # chalta hain
# print(full_name + "3")   # no error
# print(full_name + str(3))   # no error
print((full_name +" " )* 3)    # no error it will print full_name three times in a line
print((full_name +" "+"\n" )* 3)    #now in a vertical line


# Some of the mutable data types in Python are list, dictionary, set and user-defined classes. 
# On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.