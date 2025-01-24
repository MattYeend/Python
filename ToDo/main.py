# Potential to comment out
import sys
import os

# Add the parent directory of "Python" to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# Potential to comment out above
from Python.ToDo.task_manager import view_tasks, add_task, complete_task, delete_task
from Python.ToDo.file_manager import load_tasks, save_tasks

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print('5. Exit')

        choice = input("Choose an option (1-5)").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()