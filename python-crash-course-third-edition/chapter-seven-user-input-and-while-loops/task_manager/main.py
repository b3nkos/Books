from tasks import tasks, completed_tasks
from manager import show_tasks, add_task, complete_task

active = True

print("📝 Task Manager")

while active:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Quit")

    choice = input("Choose an option: ")
    if choice == "4":
        active = False
        print("Goodbyte!")
    elif choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        complete_task(tasks, completed_tasks)