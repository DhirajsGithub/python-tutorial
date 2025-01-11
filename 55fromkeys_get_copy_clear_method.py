#fromkeys

# d = {'name': 'unknown', 'age': 'unknown'}
# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
d = dict.fromkeys(('name','age', 'height'), 'unknown')        #we can also make tuples
d_tuple = tuple(d)
print(d_tuple)
# d = dict.fromkeys(('abcd'), 'unknown')        #all indexing will act as key and their value will be unknown
# d = dict.fromkeys((range(1,11)), 'unknown')      #all numbers from 1 to 10 act as key and their value will be unknown
print(d)


d = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])
# {'age': ['unknown', 'unknown'], 'name': ['unknown', 'unknown']}
print(d)


#get method()
d = {'name': 'Harshit', 'age': 'unknown'}
# print(d['names'])      # error    
print(d['name'])        #-----(1)

print(d.get('names'))     #no error only print none
print(d.get('name'))       #better to acces any value for key than (1)
print(d.get('names', "not found"))       #is names not exist as  key in d then it will not print none it will print not found

dic = {'name': 'Harshit', 'age': 22, 'age' : 34}
print(dic.get('age'))   #last wali key value will overide 


# if 'name' in d :
#     print("present")
# else: 
#     print("not present")

if d.get('names') :
    print("present")
else: 
    print("not present")
#note: if None implies false therefore next loop chalega i.e. else wala chalega


#clear method()
d.clear()
print(d)


#copy method()
# d1 = d.copy()
# print(d1)
# print(d1.popitem())
# print(d)

# dict () function to copy the dictionary
d2 = dict(d)
print(d2)

d1 = d 
#not a relevent method to copy, it just make d1=d not a copy of it
print(d1.popitem())
print(d)