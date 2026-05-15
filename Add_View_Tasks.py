# the empty list for task names serve as a reference to check for duplicate tasks, while the empty list for tasks is used to store the full task descriptions, including any deadlines that may be added. The months list contains all of the months in a year, while the days_per_month list contains the corresponding number of days for each months.
task_names = []
tasks = []
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
    for  existing_task in task_names:
        if task.lower() == existing_task.lower():
            return True      
    return False
            
# this function allows the user to add a task and optionally set a deadline for it.
def add_task():
    while True:
        print("=" * 40)
        print("           ADD & VIEW TASKS         ")
        print("=" * 40)
        

        task = input("Enter your task: ").strip().title()
        base_task = task

        if is_duplicate(base_task):
            print("Error! This task already exists.")
            continue
         
        if len(base_task) > 0 and not is_all_number(base_task):
            print()
            print("[Notice: Your task has been successfully added to the tasks list!]")
            
            deadline = input("Would you like to add a deadline for your task? (yes/no): ").lower()
            
            if deadline == "yes":
                
                while True:
                    month = input("What month is it due? ").title()
                
                    if len(month) > 0 and is_all_number(month):
                        print("Error! please input the month using letters.")
                        continue
                
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
                        full_task = f"{task} | Due: {month} {day}, at {time}:00"
                        break
                    
            elif deadline == "no":
                full_task = base_task
                print("[Notice: No deadline recorded.]")
                
            
            else:
                print("Invalid input. Task not saved. Returning to main menu.")
                continue
            
            # Storage / Display
            task_names.append(base_task)
            tasks.append(full_task)
            
            another = input("Would you like to add another task? (yes/no): ").lower()
            if another == "yes":
                continue
            elif another == "no":
                break
            else:
                print("Invalid input. Returning to main menu.")
                break
        
        else:
            print("Error! Task cannot be a number or empty. Please enter a valid task.")

# this function displays the list of tasks that have been added.
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    
    else:
        for i, task in enumerate(tasks, 1):
            print(f"[{i}] {task}")

        
add_task()
view_tasks()
