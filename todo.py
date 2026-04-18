tasks = []

def show_tasks():
    print("\n===== Your To-Do List =====")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['name']}")
    print("===========================\n")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print(f"✅ Task '{name}' added!")

def update_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to update: "))
        new_name = input("Enter new task name: ")
        tasks[num - 1]["name"] = new_name
        print("✅ Task updated!")
    except (IndexError, ValueError):
        print("❌ Invalid task number!")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print("✅ Task marked as done!")
    except (IndexError, ValueError):
        print("❌ Invalid task number!")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"🗑️ Task '{removed['name']}' deleted!")
    except (IndexError, ValueError):
        print("❌ Invalid task number!")

def main():
    print("🗒️ Welcome to To-Do List App!")
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

main()
