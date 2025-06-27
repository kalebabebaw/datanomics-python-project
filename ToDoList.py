################## To-Do List App###################

tasks = []

print("Welcome to the To-Do List App!")
print("Commands: add, view, delete, complete, exit")

while True:
    command = input("\nEnter a command: ").strip().lower()

    if command == "add":
        task = input("Enter the task description: ").strip()
        priority = input(
            "Enter the priority (low/medium/high): ").strip().lower()
        tasks.append({"task": task, "priority": priority, "completed": False})
        print(f"Task added: {task} ({priority})")

    elif command == "view":
        if not tasks:
            print("No tasks in your list.")
        else:
            print("\nYour To-Do List:")
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["completed"] else "✗"
                print(f"{i}. [{status}] {t['task']} ({t['priority']})")

    elif command == "delete":
        num = input("Enter the task number to delete: ").strip()
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            removed = tasks.pop(int(num) - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    elif command == "complete":
        num = input("Enter the task number to mark as complete: ").strip()
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            tasks[int(num) - 1]["completed"] = True
            print(f"Task marked as complete: {tasks[int(num) - 1]['task']}")
        else:
            print("Invalid task number.")

    elif command == "exit":
        break

    else:
        print("Invalid command. Try again.")

completed = sum(1 for t in tasks if t["completed"])
pending = len(tasks) - completed

print("\n--- Summary ---")
print(f"Completed tasks: {completed}")
print(f"Pending tasks: {pending}")
print("Goodbye!")
