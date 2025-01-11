# read file 

# open function 
# read method
# seek method
# tell method 
# readline method
# readlines method
# close method


# to  read the file we have open functin 
# f = open('105text.txt', 'r')     # to read the file
# f = open('105text.txt' 'w')      # to write the file

# f = open('105text.txt')         # by default agar kuch nahi likha to 'r' consider kiya jata hain 

# print(f.read())              #--------(1)
# print(f.read())              #-------(2)
# f.close()                   # file should be closed, it's a good habit to close the file

# by (2) one may be thinking that the file read must be printed twice, 
# but that's not the case actually what happens is that the read function read our file according to the 
# moment of the cursor. When it completely read the file from (1) then the cursor is at end of the file 
# hence it can't read the file from (2)

# f = open('105text.txt')

# print(f'cursor position now : {f.tell()}')
# print(f.read())
# print(f'cursor position now : {f.tell()}')

# print("before seek method")
# f.seek(0)
# print("after seek method")
# print(f"cursor positrion after seeking cursor to 0 : {f.tell()}")
# print(f.read())
# f.close()

# f = open('105text.txt')
# print("---------readline method-------------")
# print(f.readline(), end='')         # end=''  will terminate the space between two line
# print(f.readline())
# print(f.readline())
# print(f.readline())         #won't print any line due to the cursor position 

# f = open('105text.txt')
# print('--------readlines method-------------')
# lines = f.readlines()
# print(lines)          # list of lines we have in our .txt file
# print(len(lines))          # number of lines

# # for loop
# for line in lines : 
#     print(line, end='')


# f = open('105text.txt')
# # data disrcripter
# print("-------data discripter-----------")
# # to know the name of file
# print(f.name)

# # to know whether our file is close or not 
# print(f.closed)         #False    #boolean
# f.close()
# print(f.closed)            # True

# note name and closed are not methods 

print("-----if our file is not in the same folder as of python file---------")
# f = open("/Users/dhiraj/Library/Mobile Documents/com~apple~CloudDocs/python_tutorials/for read txt/test_file.txt") 
# error for windows caz unka path \ se start hota hain aur python main \ se escape bhi hona hota hain 
# mac mai / se start hota hain file ka location

f = open("/Users/dhiraj/Library/Mobile Documents/com~apple~CloudDocs/python_tutorials/for read txt/test_file.txt") 

print(f.readline())

print(type(f))        # <class '_io.TextIOWrapper'>
# we can iterate the f object as 
# for line in f:
#     print(line)
for line in f.readlines()[:2]:              # slicing 
    print(line)



print("----------another method to read our file--------------")

# another method to read our txt file is with block method
# with block 
# context manager
# with open('105text.txt', 'r') as f:
with open('105text.txt') as f:
    # var = f.read()
    data = f.read()
    print(data)

# block method will automatically close the file
print(f.closed)