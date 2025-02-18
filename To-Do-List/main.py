import os
import json
FILENAME = "task.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return  json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Creates a menu for action
def display_menu():
    print("\nTodo-list")
    print("1. View Tasks")
    print("2. Create a Task")
    print("3. Mark as done")
    print("4. Remove Task")
    print("5. Exit")

# To view ongoing tasks and their status
def view_tasks(tasks):
    print("\nYour Tasks")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task['done'] else "✗"
        print(f"{i}. {task['task']} [{status}")

# To add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    task.append({"task": task, "done": False})
    print("Task added!")

 # To mark a task as done
def mark_as_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['done'] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# To remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
#
def main():
    task = []
    while True:
        display_menu()
        choice = input("Choose a action: ")
        if choice == "1":
            view_tasks(task)
        elif choice == "2":
            add_task(task)
        elif choice == "3":
            mark_as_done(task)
        elif choice == "4":
            remove_task(task)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please try again!")

if __name__ == "__main__":
    main()