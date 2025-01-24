def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to display.")
        return

    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
