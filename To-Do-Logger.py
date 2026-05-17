# Sample task list
tasks_list = ["Do Homework", "Wash Dishes", "Study Python"]

# Sample deadline list
deadline_list = [
    "May 20, at 14:00",
    "May 21, at 10:00",
    "May 25, at 18:00"
]

months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

days_per_month = [
    31, 28, 31,
    30, 31, 30,
    31, 31, 30,
    31, 30, 31
]


# Function to check duplicate tasks
def is_duplicate(task):

    for task_name in tasks_list:
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
            print("Error! Task name cannot be numbers only.")

        elif len(new_task) < 3:
            print("Task must be at least 3 characters long.")

        elif is_duplicate(new_task):
            print("Task already exists. Please enter a different task.")

        else:
            return new_task


# Function for deadline input
def get_deadline():

    # Month Validation
    while True:

        month = input(
            "What month is it due? "
        ).strip().title()

        if month not in months:
            print("Error! Please input a valid month.")
            continue

        month_index = months.index(month)
        break

    # Day Validation
    while True:

        day_input = input(
            "What day is it due? "
        ).strip()

        if not is_all_numbers(day_input):
            print("Error! Please input the day using only numbers.")
            continue

        day = int(day_input)
        max_days = days_per_month[month_index]

        if day < 1 or day > max_days:
            print(f"Invalid day! {month} only has {max_days} days.")
            continue

        break

    # Time Validation
    while True:

        time_input = input(
            "What time is it due? (0-23): "
        ).strip()

        if not is_all_numbers(time_input):
            print("Error! Please enter a time between 0 and 23.")
            continue

        time = int(time_input)

        if time < 0 or time > 23:
            print("Error! Please enter a time between 0 and 23.")
            continue

        break

    return f"{month} {day}, at {time}:00"


# Function to update a task
def update_task():

    # Handle empty task list
    if len(tasks_list) == 0:
        print("\nNo task found.")
        return

    while True:

        print("=" * 40)
        print("         UPDATE TASK         ")
        print("=" * 40)

        for i in range(len(tasks_list)):
            print(
                "[" + str(i + 1) + "]",
                tasks_list[i],
                "- Deadline:",
                deadline_list[i]
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

        elif is_all_numbers(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks_list):

                print("Current task:", tasks_list[choice - 1])
                print("Current deadline:", deadline_list[choice - 1])

                # Get updated task
                new_task = get_task_name()

                if new_task is None:
                    return

                # Get updated deadline
                new_deadline = get_deadline()

                if new_deadline is None:
                    return

                # Update task and deadline
                tasks_list[choice - 1] = new_task
                deadline_list[choice -1] = new_deadline

                print("Task updated successfully!")
                return

            else:
                print("Invalid task number.")
                print("Please choose a number between 1 and", len(tasks_list))

        else:
            print("Please enter numbers only.")


# Function to delete a task
def delete_task():

    # Handle empty task list
    if len(tasks_list) == 0:
        print("\nNo tasks found.")
        return

    while True:

        print("\nDELETE TASK:")

        for i in range(len(tasks_list)):
            print(
                "[" + str(i + 1) + "]",
                tasks_list[i],
                "- Deadline:",
                deadline_list[i]
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

        elif is_all_numbers(choice):

            choice = int(choice)

            if choice >= 1 and choice <= len(tasks_list):

                while True:

                    confirm = input(
                        "Are you sure you want to delete '"
                        + tasks_list[choice - 1]
                        + "'? (Yes/No): "
                    ).strip().title()

                    # Cancel option
                    if confirm == "0":
                        print("Delete process cancelled.")
                        return

                    if confirm == "Yes":

                        removed_task = tasks_list.pop(choice - 1)
                        removed_deadline = deadline_list.pop(choice - 1)

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
                print("Please choose a number between 1 and", len(tasks_list))

        else:
            print("Please enter numbers only.")


# Example calls
update_task()
delete_task()

print("\nUPDATED TASK LIST:")

for i in range(len(tasks_list)):
    print(
        "[" + str(i + 1) + "]",
        tasks_list[i],
        "- Deadline:",
        deadline_list[i]
    )