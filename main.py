import common_functions as cf


# ================= INITIAL DATA (KEEP FOR DEMO) =================
tasks_list = ["Do Homework", "Wash Dishes", "Study Python"]

deadline_list = [
    "May 20, at 14:00",
    "May 21, at 10:00",
    "May 25, at 18:00"
]


# ================= DEADLINE FUNCTION =================
def get_deadline():

    while True:
        month = input("➤  What month is it due? (X to cancel): ").strip().title()

        if month.lower() == "x":
            return None

        if month not in cf.months:
            cf.error("Please input a valid month.")
            continue

        month_index = cf.months.index(month)
        break

    while True:
        day_input = input("➤  What day is it due? (X to cancel): ").strip()

        if day_input.lower() == "x":
            return None

        if not cf.is_all_numbers(day_input):
            cf.error("Please input a valid day.")
            continue

        day = int(day_input)
        max_days = cf.days_per_month[month_index]

        if day < 1 or day > max_days:
            cf.error(f"Invalid day! {month} only has {max_days} days.")
            continue

        break

    while True:
        time_input = input("➤  What time is it due? (0-23, X to cancel): ").strip()

        if time_input.lower() == "x":
            return None

        if not cf.is_all_numbers(time_input):
            cf.error("Please enter a time between 0 and 23.")
            continue

        time = int(time_input)

        if time < 0 or time > 23:
            cf.error("Please enter a time between 0 and 23.")
            continue

        break

    return f"{month} {day}, at {time}:00"


# ================= ADD TASK =================
def add_task():

    while True:
        cf.clear_screen()
        cf.print_header("ADD TASK")

        base_task = input("➤  Enter your task (X to cancel): ").strip()

        if base_task.lower() == "x":
            cf.notice("Task addition cancelled.")
            input("\n➤  Press Enter to continue...")
            return

        if len(base_task) == 0:
            cf.error("Task cannot be empty.")
            input("\n➤  Press Enter to continue...")
            continue

        if base_task == "-":
            cf.error("Task cannot be a symbol only.")
            input("\n➤  Press Enter to continue...")
            continue

        if cf.is_all_numbers(base_task):
            cf.error("Task cannot be numbers only.")
            input("\n➤  Press Enter to continue...")
            continue

        if cf.is_negative_number(base_task):
            cf.error("Task cannot be negative numbers.")
            input("\n➤  Press Enter to continue...")
            continue

        if cf.is_duplicate(base_task, tasks_list):
            cf.error("This task already exists.")
            input("\n➤  Press Enter to continue...")
            continue

        if len(base_task) < 3:
            cf.error("Task must be at least 3 characters long.")
            input("\n➤  Press Enter to continue...")
            continue

        deadline = input("➤  Would you like to add a deadline for your task? (yes/no): ").strip().lower()

        formatted_task = base_task.title()
        formatted_deadline = "No Deadline"

        if deadline == "yes":
            result = get_deadline()
            if result is not None:
                formatted_deadline = result

        elif deadline == "no":
            cf.notice("No deadline recorded.")

        else:
            cf.error("Invalid input. Task not saved.")
            input("\n➤  Press Enter to continue...")
            continue

        tasks_list.append(formatted_task)
        deadline_list.append(formatted_deadline)

        cf.success("Task added successfully!")

        cf.display_tasks("UPDATED TASK LIST", tasks_list, deadline_list)
        input("\n➤  Press Enter to continue...")

        another = input("➤  Would you like to add another task? (yes/no): ").strip().lower()

        if another == "yes":
            continue
        elif another == "no":
            break
        else:
            cf.error("Invalid input. Returning to main menu.")
            break


# ================= UPDATE TASK =================
def get_task_name():

    while True:

        new_task = input("➤  Enter new task (Enter X to cancel): ").strip().title()


        # Cancel option
        if new_task.lower() == "x":
            cf.notice("Update cancelled.")
            return None

        elif new_task == "":
            cf.error("Task cannot be empty.")
            input("\n➤  Press Enter to continue...")
            continue
        
        elif new_task == "-":
            cf.error("Task cannot be a symbol only.")
            input("\n➤  Press Enter to continue...")
            continue

        elif cf.is_all_numbers(new_task):
            cf.error("Task cannot be numbers only.")
            input("\n➤  Press Enter to continue...")
            continue

        elif cf.is_negative_number(new_task):
            cf.error("Task cannot be negative numbers.")
            continue

        elif len(new_task) < 3:
            cf.error("Task must be at least 3 characters long.")
            input("\n➤  Press Enter to continue...")
            continue

        elif cf.is_duplicate(new_task, tasks_list):

            while True:

                choice = input(
                    "➤  This task already exists, would you like to update the selected task's deadline instead? (Yes/No): "
                ).strip().lower()

                if choice == "yes":
                    return "UPDATE_DEADLINE"

                elif choice == "no":
                    cf.notice("Please enter a different task.")
                    input("\n➤  Press Enter to continue...")
                    break

                else:
                    cf.error("Please enter Yes or No.")

        else:
            return new_task




def update_task():

    # Handle empty task list
    if len(tasks_list) == 0:
        cf.display_tasks("UPDATE TASK", tasks_list, deadline_list)
        input("\n➤  Press Enter to continue...")
        return

    while True:

        cf.clear_screen()
        cf.display_tasks("UPDATE TASK", tasks_list, deadline_list)

        print("[X] Cancel")

        choice = input("➤  Enter task number to update (X to cancel): ").strip()

        # Cancel option
        if choice.lower() == "x":
            cf.notice("Update process cancelled.")
            input("\n➤  Press Enter to continue...")
            return

        if choice == "":
            cf.error("Task cannot be empty.")
            input("\n➤  Press Enter to continue...")
            continue

        if not cf.is_all_numbers(choice):
            cf.error("Please enter numbers only.")
            input("\n➤  Press Enter to continue...")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(tasks_list):
            cf.error("Invalid task number.")
            cf.notice(f"Please choose a number between 1 and {len(tasks_list)}")
            input("\n➤  Press Enter to continue...")
            continue

        cf.notice(f"Current Task: {tasks_list[choice - 1]}")
        cf.notice(f"Current Deadline: {deadline_list[choice - 1]}")

        # Get updated task
        new_task = get_task_name()

        if new_task is None:
            cf.notice("Update cancelled.")
            input("\n➤  Press Enter to continue...")
            return

        # =================  UPDATE DEADLINE FEATURE =================
        if new_task == "UPDATE_DEADLINE":

            new_deadline = get_deadline()

            if new_deadline is not None:
                deadline_list[choice - 1] = new_deadline
                cf.success("Deadline updated!")
                cf.display_tasks("UPDATED TASK LIST", tasks_list, deadline_list)

            else:
                cf.notice("Deadline update cancelled.")

            input("\n➤  Press Enter to continue...")
            return

        # Ask if user wants to update deadline
        while True:

            update_deadline = input(
                "➤  Would you like to update the deadline? (Yes or No): "
            ).strip().lower()

            if update_deadline == "yes":

                new_deadline = get_deadline()

                if new_deadline is None:
                    cf.notice("Original deadline retained.")
                    break

                deadline_list[choice - 1] = new_deadline
                break

            elif update_deadline == "no":
                break

            else:
                cf.error("Please enter Yes or No.")

        # Update task
        tasks_list[choice - 1] = new_task

        cf.success("Task updated!")
        cf.display_tasks("UPDATED TASK LIST", tasks_list, deadline_list)
        input("\n➤  Press Enter to continue...")
        return

# ================= DELETE TASK =================
def delete_task():

    if len(tasks_list) == 0:
        cf.display_tasks("DELETE TASK", tasks_list, deadline_list)
        input("\n➤  Press Enter to continue...")
        return

    while True:

        cf.clear_screen()
        cf.display_tasks("DELETE TASK", tasks_list, deadline_list)

        print("[X] Cancel")

        choice = input("➤  Enter task number to delete (X to cancel): ").strip()

        if choice.lower() == "x":
            cf.notice("Delete process cancelled.")
            input("\n➤  Press Enter to continue...")
            return

        if choice == "":
            cf.error("Task cannot be empty.")
            input("\n➤  Press Enter to continue...")
            continue

        if not cf.is_all_numbers(choice):
            cf.error("Please enter numbers only.")
            input("\n➤  Press Enter to continue...")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(tasks_list):
            cf.error("Invalid task number.")
            input("\n➤  Press Enter to continue...")
            continue

        confirm = input("➤  Delete '" + tasks_list[choice - 1] + "'? (Yes/No): ").strip().lower()

        if confirm == "yes":
            removed_task = tasks_list.pop(choice - 1)
            removed_deadline = deadline_list.pop(choice - 1)
            cf.success("Deleted task: " + removed_task + " - Deadline: " + removed_deadline)
            cf.display_tasks("UPDATED TASK LIST", tasks_list, deadline_list)

        elif confirm == "no":
            cf.notice("Delete cancelled.")

        else:
            cf.error("Please enter Yes, No, or 0.")

        input("\n➤  Press Enter to continue...")
        return


# ================= MENU =================
def main_menu():

    while True:
        cf.clear_screen()
        cf.print_header("TASK MANAGER")

        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("➤  Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            cf.display_tasks("TASK LIST", tasks_list, deadline_list)
            input("\n➤  Press Enter to continue...")
        elif choice == "5":
            cf.clear_screen()
            cf.print_header("GOODBYE!")
            print("\nThanks for using our To-Do List Manager!")
            print(
    """
    ____                 ____                 
   / __ ) __  __ ___    / __ ) __  __ ___     
  / __  |/ / / // _ \  / __  |/ / / // _ \    
 / /_/ // /_/ //  __/ / /_/ // /_/ //  __/    
/_____/ \__, / \___/ /_____/ \__, / \___/     
       /____/               /____/            

    Stay productive! See you next time.
"""
)
            break
        else:
            cf.error("Invalid input.")
            input("\n➤  Press Enter to continue...")


# ================= RUN =================
main_menu()