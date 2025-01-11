import os
# first we need to import shutil module to delete the non empty directory
import shutil

# to walk through each folder and file in the current 
os.chdir('/Users/dhiraj/Downloads')
print(os.listdir())
all_stuff = os.walk('/Users/dhiraj/Documents')
# os.walk() function will give three things i.e. is current path, folder names, file names with same sequence as written
for current_path,folder_names, file_names in all_stuff:
    print(f'current path: {current_path}')
    print(f'folder names are {folder_names}')
    print(f'file name is {file_names}')
# us path main jitte bhi folder and files hain phir agle path main jitte bhi folders and files hain and so on 

# it will roam to each folder and then come to again where it was started and continue looping unless no any folder remins

# how to delete any directory
# note our current directory is /Users/dhiraj/Downloads
# os.rmdir('untitled folder')    # NOTE it will only delete if directory is fully empty 

# How we can create directory inside directory
# os.makedirs('dumy_floder/movies/shit')     # NOTE agar directory already ban chuki hain toh agar usi naam se dusri directory banyi jaye to woh error dega Make sure of it

# NOTE shutil.rmtree('path')  will delete your directory entirely it won't make it to recycle bin 
# shutil.rmtree('dumy_floder')

# # How to copy the directory to any other directory
# shutil.copytree('dump', 'untitled folder/can_rename folder')

# How to copy any file to any directory 
# shutil.copy('file.txt', 'dump/renamed_file')            # inner text will be same but format will differ
# shutil.copy('file.txt', 'dump/renamed_file.txt')

# How to move a directory to another
# shutil.move('untitled folder', 'untitiled folder 2/move_renamed')

# How to move a file to any directory
# shutil.move('file.txt', 'untitiled folder 2/ file_renamed.txt')

