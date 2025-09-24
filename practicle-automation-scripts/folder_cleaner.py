# Script 20 Folder Cleaner.
import os
import shutil

def organize_folder_by_extension(folder_path):
    """
    Organizes files in a given folder by moving them into subfolders 
    based on their file extensions.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and non-files
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)
        
        # Remove the leading dot from the extension
        if file_extension:
            file_extension = file_extension[1:] 
        else:
            # Handle files without an extension (e.g., 'README')
            file_extension = "no_extension"

        # Create subfolder if it doesn't exist
        destination_folder = os.path.join(folder_path, file_extension)
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file
        destination_path = os.path.join(destination_folder, filename)
        try:
            shutil.move(file_path, destination_path)
            print(f"Moved '{filename}' to '{destination_folder}'")
        except Exception as e:
            print(f"Error moving '{filename}': {e}")

# Example usage:
# Replace 'your_folder_path' with the actual path to your folder
# organize_folder_by_extension('your_folder_path') 