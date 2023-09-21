def add_task(tasks, task):
    tasks.append(task)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]

def print_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(tasks, task)
            print("Task added successfully.")
        elif choice == "2":
            print_tasks(tasks)
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
            print("Task deleted successfully.")
        elif choice == "3":
            print_tasks(tasks)
        elif choice == "4":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
