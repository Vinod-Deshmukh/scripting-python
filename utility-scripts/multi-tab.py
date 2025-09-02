# utility script 6 Mutliplication Tablet Generator. 
number=int(input("Enter the number:"))

# for i in range(1,11):
#     print(f"{number} * {i} : {number*i}")
# open file in write mode
with open(f"table_{number}.txt","w") as file:  
    for i in range(1, 11):
       line= f"{number} x {i:2} = {number*i:3}\n"
       file.write(line) # write each line to file
       print(line,end="")# Also print on screen
        