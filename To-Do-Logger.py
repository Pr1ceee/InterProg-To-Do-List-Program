# Sample task list
tasks = ["Do Homework", "Wash Dishes", "Study Python"]


# Function to check if input is a number
def is_number(text):
    numbers = "0123456789"

    if text.strip() == "":
        return False

    for char in text:
        if char not in numbers:
            return False

    return True


# Function to check duplicate tasks
def is_duplicate(task_name):

    for task in tasks:
        if task.lower() == task_name.lower():
            return True

    return False


# Function to check if task name is only numbers
def is_all_numbers(text):

    numbers = "0123456789"

    for char in text:
        if char not in numbers:
            return False

    return True


# Function for valid task name input
def get_task_name():

    while True:

        # Added .title()
        new_task = input("Enter new task: ").strip().title()

        # Check empty input
        if new_task == "":
            print("Task cannot be empty or spaces only.")

        # Minimum characters
        elif len(new_task) < 7:
            print("Task must be at least 7 characters long.")

        # Prevent numbers only
        elif is_all_numbers(new_task):
            print("Task name cannot be numbers only.")

        # Check duplicate task
        elif is_duplicate(new_task):
            print("Task already exists. Please enter a different task.")

        else:
            return new_task


# Function to update a task
def update_task():

    # Handle empty task list
    if len(tasks) == 0:
        print("\nNo tasks available to update.")
        return

    while True:

        print("\nTASK LIST:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        choice = input("Enter task number to update: ").strip()

        if choice == "":
            print("Input cannot be empty or spaces only.")

        elif is_number(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks):

                print("Current task:", tasks[choice - 1])

                # Use separate function for task input
                tasks[choice - 1] = get_task_name()

                print("Task updated successfully!")
                return

            else:
                print("Invalid task number.")
                print("Please choose a number between 1 and", len(tasks))

        else:
            print("Please enter numbers only.")


# Function to delete a task
def delete_task():

    # Handle empty task list
    if len(tasks) == 0:
        print("\nNo tasks available to delete.")
        return

    while True:

        print("\nTASK LIST:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        choice = input("Enter task number to delete: ").strip()

        if choice == "":
            print("Input cannot be empty or spaces only.")

        elif is_number(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks):

                while True:

                    # Added .title()
                    confirm = input(
                        "Are you sure you want to delete '"
                        + tasks[choice - 1]
                        + "'? (Yes/No): "
                    ).strip().title()

                    if confirm == "Yes":

                        removed = tasks.pop(choice - 1)
                        print("Deleted task:", removed)
                        return

                    elif confirm == "No":
                        print("Delete cancelled.")
                        return

                    else:
                        print("Please enter Yes or No.")

            else:
                print("Invalid task number.")
                print("Please choose a number between 1 and", len(tasks))

        else:
            print("Please enter numbers only.")


# Example calls
update_task()
delete_task()

print("\nUpdated Task List:")
for task in tasks:
    print("-", task)