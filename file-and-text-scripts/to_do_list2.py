#Script 15 to_do_list
# display ,add , delete.
# to display use for loop. 
# to add use appen() method.
# to delete use pop() method.
def display(tasks):
    if not tasks:
      print("\n ----Your To Do List is empty ----\n ")
    else:
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")  
            
def add(tasks):
    new_task=input("Enter the Task: \n").strip()
    tasks=tasks.append(new_task)
    print(f" {new_task} added to list \n")

def main():
    tasks=["Reading"]
    while True:
        print("\n -- Welcome to To Do List App -- \n")
        print("1. View Task \n")
        print("2. Add Task \n")
        choice=input("Enter Your Choice: \n")
        if choice=='1':
            display(tasks)
        elif choice=='2':
            add(tasks)    
        else:
            break

if __name__=="__main__":
    main()
  
  