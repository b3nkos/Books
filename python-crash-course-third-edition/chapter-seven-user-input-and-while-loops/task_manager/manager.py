def show_tasks(tasks):
    print("\nCurrent tasks:")
    for task in tasks:
        print(f"- {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)

def complete_task(tasks, completed_task):
    task = input("Completed task: ")
    tasks.remove(task)
    completed_task.append(task)