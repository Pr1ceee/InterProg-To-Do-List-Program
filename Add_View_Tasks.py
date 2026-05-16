# the empty list for task names serve as a reference to check for duplicate tasks, while the empty list for tasks is used to store the full task descriptions, including any deadlines that may be added. The months list contains all of the months in a year, while the days_per_month list contains the corresponding number of days for each months.
tasks = []
deadlines = []
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
    for  existing_task in tasks:
        if task == existing_task:
            return True      
    return False
            
# this function allows the user to add a task and optionally set a deadline for it.
def add_task():
    while True:
        print("=" * 40)
        print("           ADD & VIEW TASKS         ")
        print("=" * 40)
        

        base_task = input("Enter your task: ").strip().title()
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
            
            if deadline == "yes":
                
                while True:
                    month = input("What month is it due? ").strip().title()
                
                    if month not in months:
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
                    day_input = input("What day is it due? ")
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
                    time_input = input("What time is it due? (0-23): ")
                    if not is_all_number(time_input):
                        print("Error! Please enter a time between 0 and 23.")
                        continue
                    
                    time = int(time_input)
                    if time < 0 or time > 23:
                        print("Error! Please enter a time between 0 and 23.")
                        continue
                    else:
                        formatted_task = base_task.title()
                        formatted_deadline = f"{month} {day} at {time}:00"
                        break
                    
            elif deadline == "no":
                formatted_task = base_task.title()
                formatted_deadline = "No Deadline"
                print("[Notice: No deadline recorded.]")
            
            else:
                print("Invalid input. Task not saved. Returning to main menu.")
                continue
            
            # Storage / Display
            tasks.append(formatted_task)
            deadlines.append(formatted_deadline)
            
            print("[Notice: Your task has been successfully added to the tasks list!]")
            
            another = input("Would you like to add another task? (yes/no): ").lower()
            if another == "yes":
                continue
            elif another == "no":
                break
            else:
                print("Invalid input. Returning to main menu.")
                break

# this function displays the list of tasks that have been added.
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    
    else:
        for i in range(len(tasks)):
            print("[" + str(i + 1) + "]", tasks[i], "-Deadline:", deadlines[i])

        
add_task()
view_tasks()
