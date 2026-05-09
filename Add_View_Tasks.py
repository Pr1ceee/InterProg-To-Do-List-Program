# the empty list for tasks serves as a storage for the tasks that the user will input.

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
# this function checks if the input is a number.  
def is_number(text):
    numbers = "0123456789"
    
    for char in text:
        if char not in numbers:
            return True
    return False

# this function checks if the task is a duplicate of an existing task in the list.   
def is_duplicate(task):
    if task in tasks:
        return True
    return False

def add_task():
    while True:
        print("=" * 40)
        print("           ADD & VIEW TASKS         ")
        print("=" * 40)
        

        task = input("Enter your task: ").strip().title()
        
        if is_duplicate(task):
            print("Error! This task already exists. Please enter a different task.")
            continue
         
        if len(task) > 0 and is_number(task):
            full_task = task
            print()
            print("[Notice: Your task has been successfully added to the tasks list!]")
            
            deadline = input("Would you like to add a deadline for your task? (yes/no): ").lower()
            
            if deadline == "yes":
                month = input("What month is it due? ").title()
                if month not in months:
                    print("Error! Please input a valid month.")
                    continue
                else:
                    print("[Notice: Month added successfully!]")
                month_index = 0
                for i in range(len(months)):
                    if months[i] == month:
                        month_index = i
                        break
                    
                day = int(input("What day is it due? "))
                max_days = days_per_month[month_index]
                if day < 1 or day > max_days:
                    print(f"Invalid day! {month} only has {max_days} days.")
                    continue
                else:
                    print("[Notice: Day added successfully!]")
                    
                while True:
                    time = int(input("What time is it due? (0-23): "))
                    if time < 0 or time > 23:
                        print("Error! Please enter a time between 0 and 23.")
                    else:
                        full_task = f"{task} | Due: {month} {day}, at {time}:00"
                        break
            elif deadline == "no":
                print("[Notice: No deadline recorded.")
            
            else:
                print("Invalid input. Please try again.")
            
            tasks.append(full_task)
            
            another = input("Would you like to add another task? yes = 1, no = 0: ")
            if another == "1":
                continue
            elif another == "0":
                break
            else:
                print("Invalid input. Returning to main menu.")
                break
        
        else:
            print("Error! Task cannot be a number or empty. Please enter a valid task.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    
    else:
        for i, task in enumerate(tasks, 1):
            print(f"[{i}] {task}")

        
add_task()
view_tasks()