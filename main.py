


def display_menu():
    print("\n-----------------------")
    print("    TO DO LIST MENU    ")
    print("-----------------------")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Exit")


def show_tasks(task_list):
    
    if len(task_list) == 0:
        print("Your list is currently empty.")
    else:
        print("\nYour Current Tasks:")
        for i in range(len(task_list)):
           
            print(str(i + 1) + ". " + task_list[i])


def add_new_task(task_list):
    new_task = input("\nEnter task description: ")

   
    if new_task != "":
        task_list.append(new_task)
        print("Task added successfully!")
    else:
        print("Error: You cannot enter an empty task.")


def remove_task(task_list):
    show_tasks(task_list)

    if len(task_list) == 0:
        return

    num = input("Enter the task number you want to delete: ")

    
    if num.isdigit():
        task_num = int(num)

        
        if task_num >= 1 and task_num <= len(task_list):
            deleted = task_list.pop(task_num - 1)
            print("Deleted task: " + deleted)
        else:
            print("Invalid task number!")
    else:
        print("Please enter a valid number.")


todo_list = []

while True:
    display_menu()
    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        show_tasks(todo_list)
    elif user_choice == "2":
        add_new_task(todo_list)
    elif user_choice == "3":
        remove_task(todo_list)
    elif user_choice == "4":
        print("\nThank you for using the To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.")
