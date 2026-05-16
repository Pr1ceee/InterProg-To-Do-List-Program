# Sample task list
tasks = ["Do Homework", "Wash Dishes", "Study Python"]

# Separate deadline list
deadlines = ["May 20", "May 22", "May 25"]


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

    if text == "":
        return False

    numbers = "0123456789"

    for char in text:
        if char not in numbers:
            return False

    return True


# Function for valid task name input
def get_task_name():

    while True:

        new_task = input(
            "Enter new task (Enter 0 to cancel): "
        ).strip().title()

        # Cancel option
        if new_task == "0":
            print("Update cancelled.")
            return None

        elif new_task == "":
            print("Task cannot be empty or spaces only.")

        elif is_all_numbers(new_task):
            print("Task name cannot be numbers only.")

        elif len(new_task) < 3:
            print("Task must be at least 3 characters long.")

        elif is_duplicate(new_task):
            print("Task already exists. Please enter a different task.")

        else:
            return new_task


# Function for deadline input
def get_deadline():

    while True:

        deadline = input(
            "Enter deadline (Example: May 20 or 0 to cancel): "
        ).strip().title()

        # Cancel option
        if deadline == "0":
            print("Deadline update cancelled.")
            return None

        elif deadline == "":
            print("Deadline cannot be empty.")

        elif len(deadline) < 3:
            print("Deadline is too short.")

        else:
            return deadline


# Function to update a task
def update_task():

    # Handle empty task list
    if len(tasks) == 0:
        print("\nNo tasks available to update.")
        return

    while True:

        print("\nTASK LIST:")

        for i in range(len(tasks)):
            print(
                "[" + str(i + 1) + "]",
                tasks[i],
                "- Deadline:",
                deadlines[i]
            )

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
                print("Current deadline:", deadlines[choice - 1])

                # Get updated task
                updated_task = get_task_name()

                if updated_task is None:
                    return

                # Get updated deadline
                updated_deadline = get_deadline()

                if updated_deadline is None:
                    return

                # Update task and deadline
                tasks[choice - 1] = updated_task
                deadlines[choice - 1] = updated_deadline

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
            print(
                "[" + str(i + 1) + "]",
                tasks[i],
                "- Deadline:",
                deadlines[i]
            )

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

                        removed_task = tasks.pop(choice - 1)
                        removed_deadline = deadlines.pop(choice - 1)

                        print(
                            "Deleted task:",
                            removed_task,
                            "- Deadline:",
                            removed_deadline
                        )
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
    print(
        "[" + str(i + 1) + "]",
        tasks[i],
        "- Deadline:",
        deadlines[i]
    )