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
    file_name=f"{i}.txt"

    full_file_path= os.path.join(directory_path,file_name)
    with open(full_file_path,"w") as file:
       file.write(f"This is the content of a new file-{file_name}")
       print(f'file named {file_name} created successfully in {directory_path}     \n')
i=0
new_file=directory_path
for item_name in os.listdir(directory_path):
    old_file_path = os.path.join(directory_path, item_name)
    new_file_name = f"new_{i}.txt"
    new_file_path = os.path.join(directory_path, new_file_name)
    if not os.path.exists(new_file_path):   # only rename if free
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {item_name} -> {new_file_name}")
    else:
        print(f"Skipped {item_name}, because {new_file_name} already exists")
    i=i+1
    
     
    