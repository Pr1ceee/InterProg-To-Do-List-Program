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
        new_task = input(
            "Enter new task (Enter 0 to cancel): "
        ).strip().title()

        # Cancel option
        if new_task == "0":
            print("Update cancelled.")
            return None

        # Check empty input
        elif new_task == "":
            print("Task cannot be empty or spaces only.")

        # Prevent numbers only
        elif is_all_numbers(new_task):
            print("Task name cannot be numbers only.")

        # Minimum characters
        elif len(new_task) < 3:
            print("Task must be at least 3 characters long.")

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
            print("[" + str(i + 1) + "]", tasks[i])

        print("[0] Cancel")

        choice = input(
            "Enter task number to update: "
        ).strip()

        # Cancel option
        if choice == "0":
            print("Update process cancelled.")
            return

        if choice == "":
            print("Input cannot be empty or spaces only.")

        elif is_number(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks):

                print("Current task:", tasks[choice - 1])

                # Use separate function for task input
                updated_task = get_task_name()

                # If cancelled
                if updated_task is None:
                    return

                tasks[choice - 1] = updated_task

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
            print("[" + str(i + 1) + "]", tasks[i])

        print("[0] Cancel")

        choice = input(
            "Enter task number to delete: "
        ).strip()

        # Cancel option
        if choice == "0":
            print("Delete process cancelled.")
            return

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
                        + "'? (Yes/No or 0 to cancel): "
                    ).strip().title()

                    # Cancel option
                    if confirm == "0":
                        print("Delete process cancelled.")
                        return

                    if confirm == "Yes":

                        removed = tasks.pop(choice - 1)
                        print("Deleted task:", removed)
                        return

                    elif confirm == "No":
                        print("Delete cancelled.")
                        return

                    else:
                        print("Please enter Yes, No, or 0.")

            else:
                print("Invalid task number.")
                print("Please choose a number between 1 and", len(tasks))

        else:
            print("Please enter numbers only.")


# Example calls
update_task()
delete_task()

print("\nUpdated Task List:")

for i in range(len(tasks)):
    print("[" + str(i + 1) + "]", tasks[i])