# method for asking try again
def try_again():
    """
    This function asks the user if they want to try again with action.
    """
    while True:
        decision = input("""Do you want to try again?
                         Enter 'y' for yes and 'n' for no:""")
        if decision == 'y' or 'Y':
            return True
        elif decision == 'n' or 'N':
            return False
        else:
            print("Invalid input!")


# method for adding a task to todo list
def Add():
    """
    This function is used to add a new task to the todo list.
    """
    entry = input("Enter the task:")

    todo_list[entry] = "pending"

    print("\nYour task has been added to the todo list with status as pending.\n")


# method for listing all tasks in todo list
def List_all():
    """
    This function is used to list all task present in the todo list.

    """
    if len(todo_list) == 0:
        print("\nThere are no tasks in your todo list.\n")
    else:
        print("\nYour todo list contain the following tasks:\n")
        for key, value in todo_list.items():
            print(f"{key}: {value}")


# method for listing tasks according to the status provided
def List_by_status(selected_status):
    """
    This function is used to list tasks in todo list according to provided status.

    """
    if len(todo_list)==0:
        print("\nThere are no tasks in your todo list.\n")
    else:
        print(f"\nYour todo list contain the following {selected_status} tasks:\n")
        for key,status in todo_list.items():
            if selected_status in todo_list[key]:
                print(f"{key}: {status}")
        else:
            print(f"There are no {selected_status} tasks in your todo list.")


# method for closing a pending task
def Close():
    """
    This function is used to close an existing task in the todo list.

    """
    for key, value in todo_list.items():
        print(key+": "+value)
    while True:
        choice = input("Choose the task that need to be closed:")

        if choice in todo_list:
            if todo_list[choice]=="pendind":
                todo_list[choice]="completed"
                print("\nThe task \'"+choice+"\' has been completed.\n")
            else:
                print("\nThe task is already completed!.\n")
            return False
        else:
            print("\nNo such task exist in the todo list.\n")
            try_again()


# method to update a task name
def Update():
    """
    This function is used to update an existing task in the todo list.

    """
    for key, value in todo_list.items():
        print(key+": "+value)
    while True:
        choice = input("Choose the task that need to be updated:")

        if choice in todo_list:
            new_task = input("Enter the new task name:")
            todo_list[new_task] = todo_list.pop(choice)
            print("\nYour task has been updated.\n")
            return False
        else:
            print("Enter the task name carefully!")
            try_again()


# method to delete a task from todo list
def Delete():
    """
    This function is used to delete an existing task in the todo list.

    """
    for key, value in todo_list.items():
        print(key+": "+value)
    while True:
        choice = input("Choose the task that need to be deleted:")
        try:
            decision = input("Are you sure you want to delete the task-  "+ choice+"(y/n):")
            if decision == 'y' or decision == 'Y':
                if choice in todo_list:
                    todo_list.pop(choice)
                    print("\nYour task has been deleted.\n")
                    return False
                else:
                    print("\nNo such task exist in the todo list.\n")
            else:
                print("Invalid input!!")
                try_again()
        except ValueError:
            print("Invalid input.")
            try_again()


# method to write pending and completed task into separate files
def Write_to_file(todo_list):
    """
    This function write all the tasks into different files.

    Each time this function is called it re-write the existing data on the both files.
    """
    if len(todo_list) == 0:
        print("Your list is empmty!!")
    else:
        with open("Pending.txt", "w") as file_pending:
            file_pending.write("Completed tasks:")

            for task, status in todo_list.items():
                if status == "pending":
                    file_pending.write(f"\n{task}")

        with open("Completed.txt", "w") as file_completed:
            file_completed.write("Completed tasks:")

            for task, status in todo_list.items():
                if status == "completed":
                    file_completed.write(f"\n{task}")

        print("Your files has been created.")


# main program
todo_list = {}
repeat = True
while repeat:
    print("\nManage your todo list.")
    print("*********\nOptions: \n*********")
    print('''
    1.Add tasks to the todo list
    2.List all the tasks in todo list
    3.List pending or closed tasks
    4.Close a task
    5.Update a task
    6.Delete a task
    7.Write to different files (Pending and Completed)
    8.Exit the program''')
    try:
        choice = int(input("Choose an option from above \n(Your choice has to be the numbers corresponding to the options.):"))
        match choice:

            case 1:
                no_of_entry = int(input("Enter the number of tasks you want to add:"))
                i = 0
                for i in range(no_of_entry):
                    Add()

            case 2:
                List_all()

            case 3:
                try:
                    selected_choice = int(input(" 1.pending \n 2.completed \n Choose '1' or '2' for status:"))
                    if selected_choice == 1:
                        selected_status = "pending"
                        List_by_status(selected_status)
                    elif selected_choice == 2:
                        selected_status = "completed"
                        List_by_status(selected_status)
                    else:
                        print("\nWrong input\n")
                except ValueError:
                    print("\nInvalid input\n")

            case 4:
                Close()

            case 5:
                Update()
                for key, value in todo_list.items():
                    print(key+": "+value)

            case 6:
                Delete()

            case 7:
                Write_to_file(todo_list)

            case 8:
                decision = input("Do you want to exit(y/n:)")
                if decision == 'y' or decision == 'Y':
                    repeat = False

            case _:
                print("\nInvalid Input\n")
    except ValueError:
        print("Invalid input!")

# The changes are:
# 1)Docstrings and comments has been added.
# 2)Validation error has been dealt.
# 3)Clear instructions has been added for the user.
# 4)In add task;
#   it will ask for number tasks that need to be added.
# 5)Some internal loops for validation fails has been added.
# 6)In listing tasks by status;
#   if there are no tasks in the given status a message will be displayed.
# 7)In closing tasks;
#   If the task have already closed then an appropriate message is shown.
# 8)In write to file;
#   if there are notasks in the list an appropriate message will be displayed.