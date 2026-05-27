import common_functions as cf 

cf.clear_screen()
cf.print_header("TASK MANAGER")

# Empty task list and deadline list
tasks_list = []
deadline_list = []

# Function to handle cancelled deadline input and return a default value
def get_cancelled_deadline():
    print("Deadline input cancelled.")
    return "No Deadline"
 
# Function to get and validate deadline input from the user      
def get_deadline():
    # Month Validation
    while True:
        month = input("➤ What month is it due? (0 to cancel): ").strip().title()

        # Cancel option
        if month == "0":
            return get_cancelled_deadline()
                        
        elif month not in cf.months:
            cf.error("Please input a valid month.")
            continue

        else:
            break
                
    # Finds the index of the month in the months list for days_per_month reference
    month_index = cf.months.index(month)
        
    # Day Validation
    while True:    
        day_input = input("➤ What day is it due? (0 to cancel) ").strip()
                    
        # Cancel option
        if day_input == "0":
            return get_cancelled_deadline()
                    
        if not cf.is_all_numbers(day_input):
            cf.error("Please input the day using only numbers.")
            continue
                    
        # Checks if the day is valid for the month
        day = int(day_input)
        max_days = cf.days_per_month[month_index]
        if day < 1 or day > max_days:
            cf.error(f"Invalid day! {month} only has {max_days} days.")
            continue

        else:
            break
    
    # Time Validation   
    while True:
        time_input = input("➤ What time is it due? (0-23) (-1 to cancel): ")
                    
        if time_input == "-1":
            return get_cancelled_deadline()
                    
        if not cf.is_all_numbers(time_input):
            cf.error("Please enter a time between 0 and 23.")
            continue
                    
        time = int(time_input)
        if time < 0 or time > 23:
            cf.error("Please enter a time between 0 and 23.")
            continue
        else:
            break
        
    return f"{month} {day}, at {time}:00"
        
# Function to add a task and optionally set a deadline for it
def add_task():
    while True:
        cf.clear_screen()
        cf.print_header("ADD TASK")

        base_task = input("➤ Enter your task (0 to cancel): ").strip()      
         
        # Cancel option       
        if base_task == "0":
            cf.notice("Task addition cancelled.")
            return

        if len(base_task) == 0:
            cf.error("Task cannot be empty.")
            continue
        
        elif len(base_task) < 3:
            cf.error("Task must be at least 3 characters long.")
            continue

        elif cf.is_all_numbers(base_task):
            cf.error("Task cannot be numbers only.")
            continue
        
        elif cf.is_duplicate(base_task, tasks_list):
            cf.error("This task already exists.")
            continue

        else:
            deadline = input("➤ Would you like to add a deadline for your task? (yes/no): ").strip().lower()
            
            formatted_task = base_task.title()
            formatted_deadline = "No Deadline"
                
            if deadline == "yes":
                formatted_deadline = get_deadline()
                
            # If the user chooses not to add a deadline, deadline = "No Deadline" but the task is still added to the list with a notice that no deadline was recorded.
            elif deadline == "no":
                cf.notice("No deadline recorded.")
            
            else:
                cf.error("Invalid input. Task not saved.")
                continue
            
            # Storage / Display
            tasks_list.append(formatted_task)
            deadline_list.append(formatted_deadline)
            cf.success("Your task has been successfully added to the tasks list!")
            
            cf.display_tasks("UPDATED TASK LIST", tasks_list, deadline_list)
            input("\n➤ Press Enter to continue...")
            
            # Ask if user wants to add another task
            another = input("➤ Would you like to add another task? (yes/no): ").strip().lower()
            if another == "yes":
                continue
            elif another == "no":
                break
            else:
                cf.error("Invalid input. Returning to main menu.")
                break
  
add_task()

