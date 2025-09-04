# utility script 8 countdown timer

# The time.sleep() function in Python is used to pause the execution 
# of a program or a specific thread for a designated duration. 
# This function is part of the built-in time module.
import time

seconds=int(input("Enter the time in seconds: "))
# seconds : Number of seconds for which the code is required to be stopped.
time.sleep(seconds)
print(f"timer stopped the code for {seconds} seconds")
