# file and text script 12, Rename files in a folder- add numbering to file names.
import os
# current_directory=os.getcwd()
# print(f"current working directory:{current_directory}")
# new_directory_name="my_new_folder"
# os.mkdir(new_directory_name)
# print(f'Directory {new_directory_name} creatd.')

directory_path='D:/august-2025/scripting-python/file-and-text-scripts/my_new_folder'
# file_name="my_new_file.txt"
for i in range(5):
    file_name=str(i)
    full_file_path= os.path.join(directory_path,file_name)
    with open(full_file_path,"w") as file:
       file.write(f"This is the content of a new file-{file_name}")
       print(f'file named {file_name} created successfully in {directory_path}     \n')
# try: 
# # for item_name in os.listdir(directory_path):
#         full_path=os.path.join(directory_path,item_name)
#         if os.path.isfile(full_path):
#             print(f"File {item_name}")