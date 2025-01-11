#compare list 
#is vs ==
fruits1 = ['orange', 'apple', 'pear']
fruits3 = ['orange', 'apple', 'pear']
fruits2 = ['banana', 'kiwi', 'apple', 'banana']

print(fruits1 == fruits2) 
print(fruits1 == fruits3)            #values are same
print(fruits1 is fruits3)             #false it will see ki fuits1 and fruits3 ek hi heap memeory main store hain ki nahi or unki address at heap same hain ki nahi 