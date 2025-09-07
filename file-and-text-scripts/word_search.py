# file and text script 11, word search in a file.

# In Python, with open() is the recommended and safest way to interact with files.
#  It utilizes a context manager to ensure that files are properly closed after operations, 
# even if errors occur during file processing.
# Here's how it works and its benefits:
#Automatic File Closing: When you use with open(...) as file_object:, 
# Python automatically calls the __enter__ method when entering the with block and
#  the __exit__ method when exiting it. The __exit__ method ensures the file is closed,
#  regardless of whether the block completes normally or an exception is raised. 
# This prevents resource leaks and potential data corruption

word=input("enter the word you want to search: \n",)
with open ("feel_good.txt") as file:
    content=file.read()
    count=content.count(word)
    if count>0:
        print (f"✅ yes, the word {word} appears {count} times in the file.")
    else:
        print(f"❌ sorry, the word {word} doesn't exists in this file")    