# Script 14, To-Do-List.
def display_tasks(tasks):
    """Displays the current tasks in the to-do list."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['description']}")
        print("-----------------------")

def add_task(tasks):
    """Adds a new task to the to-do list."""
    description = input("Enter the task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        print(f"Task '{description}' added.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    """Marks a task as complete."""
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to mark complete.")

def delete_task(tasks):
    """Deletes a task from the to-do list."""
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task['description']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to delete.")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
