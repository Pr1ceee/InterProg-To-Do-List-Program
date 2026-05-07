# Sample task list
tasks = ["Do homework", "Wash dishes", "Study Python"]


# Function to check if input is a number
def is_number(text):
    numbers = "0123456789"

    if text.strip() == "":
        return False

    for char in text:
        if char not in numbers:
            return False

    return True


# Function to update a task
def update_task():

    while True:

        print("\nTASK LIST:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        choice = input("Enter task number to update: ")

        if choice.strip() == "":
            print("Input cannot be empty or spaces only.")

        elif is_number(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks):

                while True:

                    new_task = input("Enter new task: ")

                    if new_task.strip() == "":
                        print("Task cannot be empty or spaces only.")
                    else:
                        tasks[choice - 1] = new_task
                        print("Task updated successfully!")
                        return

            else:
                print("Invalid task number.")

        else:
            print("Please enter numbers only.")


# Function to delete a task
def delete_task():

    while True:

        print("\nTASK LIST:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        choice = input("Enter task number to delete: ")

        if choice.strip() == "":
            print("Input cannot be empty or spaces only.")

        elif is_number(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks):

                removed = tasks.pop(choice - 1)
                print("Deleted task:", removed)
                return

            else:
                print("Invalid task number.")

        else:
            print("Please enter numbers only.")


# Example calls
update_task()
delete_task()

print("\nUpdated Task List:")
for task in tasks:
    print("-", task)