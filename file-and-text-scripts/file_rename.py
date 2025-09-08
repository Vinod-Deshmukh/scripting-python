# file and text script 12, Rename files in a folder- add numbering to file names.
import os
# current_directory=os.getcwd()
# print(f"current working directory:{current_directory}")
# new_directory_name="my_new_folder"
# os.mkdir(new_directory_name)
# print(f'Directory {new_directory_name} creatd.')

path='D:/august-2025/scripting-python/file-and-text-scripts/my_new_folder'
dir=os.listdir(path)
print(f'the list of files and directories {dir} \n')
