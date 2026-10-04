tasks = []

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        number = int(input("Task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Deleted:", removed)
        else:
            print("Invalid number.")
    elif choice == "4":
        print("Bye!")
        break
