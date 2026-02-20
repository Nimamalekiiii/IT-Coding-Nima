import datetime

tasks = []

def show_menu():
    print("\n=== STUDENT TASK MANAGER ===")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")


def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    try:
        deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        tasks.append({
            "title": title,
            "deadline": deadline_date,
            "created": datetime.datetime.now()
        })
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please try again.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']}")
        print(f"   Deadline: {task['deadline'].date()}")
        print(f"   Created: {task['created'].strftime('%Y-%m-%d %H:%M')}")
        print("-" * 30)


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! 🚀")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
