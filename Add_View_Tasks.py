print("=" * 40)
print("           TASK MANAGER         ")
print("=" * 40)

# the empty lists below are used to store the tasks and their corresponding deadlines. The 'tasks_list' list will hold the names of the tasks, while the 'deadline_list' list will hold the deadlines associated with each task. The 'months' list contains the names of the months, and the 'days_per_month' list contains the number of days in each month, which is used for validating user input when setting deadlines.
tasks_list = []
deadline_list = []
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
# this function checks if the input text consists entirely of numbers. It returns False if the text is empty or contains any non-numeric characters and True if all characters in the text are numbers.
def is_all_number(text):
    if len(text) == 0:
        return False
    
    numbers = "0123456789"
    for char in text:
        if char not in numbers:
            return False
    return True

# this function checks if the task is a duplicate of an existing task in the list.   
def is_duplicate(task):
    for  existing_task in tasks_list:
        if task.lower() == existing_task.lower():
            return True      
    return False
            
# this function displays the list of tasks that have been added.
def view_tasks():
    print("=" * 40)
    print("            VIEW TASKS         ")
    print("=" * 40)

    if len(tasks_list) == 0:
        print("No tasks found.")
    
    else:
        for i in range(len(tasks_list)):
            print("[" + str(i + 1) + "]", tasks_list[i], "- Deadline:", deadline_list[i])

# this function allows the user to add a task and optionally set a deadline for it.
def add_task():
    while True:
        print("=" * 40)
        print("           ADD TASKS         ")
        print("=" * 40)
        

        base_task = input("Enter your task (0 to cancel): ").strip().title()       
                
        if base_task == "0":
            print("Task addition cancelled.")
            return None
        
        normalized_task = base_task.lower()

        if len(base_task) == 0:
            print("Error! Task cannot be empty.")
            continue
        
        elif len(base_task) < 3:
            print("Error! Task must be at least 3 characters long.")
            continue

        elif is_all_number(base_task):
            print("Error! Task cannot be numbers only.")
            continue
        
        elif is_duplicate(normalized_task):
            print("Error! This task already exists.")
            continue

        else:
            deadline = input("Would you like to add a deadline for your task? (yes/no): ").strip().lower()
            
            if deadline == "yes".strip().lower():
                
                while True:
                    month = input("What month is it due? (0 to cancel): ").strip().title()

                    if month == "0":
                        print("Month input cancelled.")
                        return None
                        
                    elif month not in months:
                        print("Error! Please input a valid month.")
                        continue

                    else:
                        print("[Notice: Month added successfully!]")
                        break
                    
                month_index = 0
                for i in range(len(months)):
                    if months[i] == month:
                        month_index = i
                        break
                
                while True:    
                    day_input = input("What day is it due? (0 to cancel) ").strip()
                    
                    if day_input == "0":
                        print("Day input cancelled.")
                        return None
                    
                    if not is_all_number(day_input):
                        print("Error! Please input the day using only numbers.")
                        continue
                
                    day = int(day_input)
                    max_days = days_per_month[month_index]
                    if day < 1 or day > max_days:
                        print(f"Invalid day! {month} only has {max_days} days.")
                        continue

                    else:
                        print("[Notice: Day added successfully!]")
                        break
                    
                while True:
                    time_input = input("What time is it due? (0-23) (0 to cancel): ")
                    
                    if time_input == "0":
                        print("Time input cancelled.")
                        return None
                    
                    if not is_all_number(time_input):
                        print("Error! Please enter a time between 0 and 23.")
                        continue
                    
                    time = int(time_input)
                    if time < 0 or time > 23:
                        print("Error! Please enter a time between 0 and 23.")
                        continue

                    else:
                        formatted_task = base_task.title()
                        formatted_deadline = f"{month} {day}, at {time}:00"
                        break
                    
            elif deadline == "no".strip().lower():
                formatted_task = base_task.title()
                formatted_deadline = "No Deadline"
                print("[Notice: No deadline recorded.]")
            
            else:
                print("Invalid input. Task not saved.")
                continue
            
            # Storage / Display
            tasks_list.append(formatted_task)
            deadline_list.append(formatted_deadline)
            print("[Notice: Your task has been successfully added to the tasks list!]")
            
            view_tasks()
            
            another = input("Would you like to add another task? (yes/no): ").lower()
            if another == "yes":
                continue
            elif another == "no":
                break
            else:
                print("Invalid input. Returning to main menu.")
                break
  
add_task()

