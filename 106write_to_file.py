# write to file
# to write to file we have three methods as 'w', 'a', 'r+'

# 1.) w method

# with open('106text.txt', 'w') as f:
#     f.write('hellow')

# with open('106text.txt') as f:
#     data = f.read()
#     print(data)

# 'w' method will override the existence file and hence our previous file content will be deleted 
# when to use 'w' method, when there is nothing in our file

# 2.) a method (append)
with open('106text.txt', 'a') as f:
    f.write("\ncontinue using append method")

# it will add the text at the end of cursor 
# if the given file doesn't exist then it will create that file and hence add that text

# 3.) r+ method
with open('106text.txt', 'r+') as f:
    # f.write('please do it')
    # it will overide the starting letter as per the length of the 'please do it' to avoid this we can move the position of the cursor
    f.seek(len(f.read()))
    f.write('please do it')


# how to copy text from one file to another
with open('105text.txt', 'r') as rf:
    with open('106text.txt', 'a') as wf:
        wf.write(rf.read())