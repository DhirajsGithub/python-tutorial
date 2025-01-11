# can work with folders and files in put system using OS module
import os
# we need to impost os module 

# to know to current working directory(basically a folder) path
# os.getcwd() is a function for that
print(os.getcwd())

# os.mkdir("dumy_folder")    # will create a folfer in the directory of a path
# os.mkdir("dumy_folder")    # file exist error will be raised 
# to avoid this error 
if os.path.exists("dumy_folder"):      # when dealing with cwd else need to add path+foldername
    print("already presetnt")
else :
    os.mkdir("dumy_folder")

# NOTE os.path.exists("full path must be here otherwise it will consider cwd path and execute")

# to create a file in our path so many method but we use
open('115dumyfile.txt', 'a').close()   
open('115dumyfile.txt', 'a').close()     # it also don't create a duplicate one and also not shows any error

# copying the path where new directory is to be made
# os.mkdir('/Users/dhiraj/Library/Mobile Documents/com~apple~CloudDocs/python_tutorials/osmodules/dumy_folder_2')

# to change the current directory we can do 
# os.chdir('any_path')
# then we can use that path referecnce and now without providing full path we can make mkdir and stuffs

# print(os.listdir()) # will print all the files in list format of current directory
print(os.listdir('/Users/dhiraj/Music'))  # for other than current directoy
# to print the path of the list items we can do
# 1. 
# for item in os.listdir('/Users/dhiraj/Music'):
#     print('/Users/dhiraj/Music'+'/'+item)   # it's a forward slash so no need of escape sequence

# 2. # it will work for current directory items
for item in os.listdir():
    path = os.path.join(os.getcwd(), item)
    print(path)
