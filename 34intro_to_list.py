#data structures ---> list, tuple, set, dictionary
#list = ordered collection of items
#you can store anything in lists int, float, string
# list are flexible whereas arrays takes element of a single data type only


numbers = [1,2,3,4]
print(numbers)

mixed = [1,2,3,"five", "six", None, 2,3]
print(mixed[3])
mixed[3] = 5
print(mixed)
print(mixed[:2])
mixed[1:] = "harsh"      #it will print out each index of string harsh updating elements of mixed from index 1
print(mixed)
mixed[1:]  = "harsh", "rohit" 
print(mixed)


