import os, shutil

# NOTE : tuples are used to not change the data inside and they give better performance than list 
dict_extensions = {
    'audio_extension' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extension' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extension' : ('.txt', '.pdf', '.yaml', '.doc')
}
# can modified as many files as you want in the dictionary and can take any extension

folderpath = input("enter the path name: ")        # need to enter the path where you have mess of your files
def file_finder(folder_path, file_extensions):
    files = [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension) ] 
    return files

for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split("_")[0] + "Files"
    folder_exist_path = os.path.join(folderpath, folder_name)
    if os.path.exists(folder_exist_path):
        for item in file_finder(folderpath, extension_tuple):
            item_path = os.path.join(folderpath, item)         # need to work with paths coz we are not in current directory hence can't deal with item directly
            item_new_path = os.path.join(folder_exist_path, item)
            shutil.move(item_path, item_new_path)
        
        
    else:
        folder_path = os.path.join(folderpath, folder_name)
        os.mkdir(folder_path)   # creates a folder by the above path
        for item in file_finder(folderpath, extension_tuple):
            item_path = os.path.join(folderpath, item)
            item_new_path = os.path.join(folder_path, item)
            shutil.move(item_path, item_new_path)

print("\nfiles moved successfully!!")
        
          




 