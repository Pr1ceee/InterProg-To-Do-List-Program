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

while True:
    print("=" * 40)
    print("           ADD & VIEW TASKS         ")
    print("=" * 40)

    def add_task():
        task = input("Enter your task: ").strip().title()
        
        if len(task) >0:
            full_task = task
            print()
            print("[Notice: Your task has been successfully added to the tasks list!]")
            deadline = input("Would you like to add a deadline for your task? (yes/no): ").lower()
            
            if deadline == "yes":
                month = input("What month is it due? ").title()
                if month not in months:
                    print("Error! Please input a valid month.")
                    return
                else:
                    print("[Notice: Month added successfully!]")
                month_index = months.index(month)
                max_days = days_per_month[month_index]
                    
                day = int(input("What day is it due? "))
                if day < 1 or day > max_days:
                    print(f"Invalid day! {month} only has {max_days} days.")
                    return
                else:
                    print("[Notice: Day added successfully!]")
                    
                while True:
                    time = int(input("What time is it due? (0-23): "))
                    if time <= 0 or time <= 23:
                        full_task = f"{task} - Due: {month} {day}, at {time}:00"
                        break
                    else:
                        print("Error! Please enter a time between 0 and 23.")
                
            elif deadline == "no":
                print("[Notice: No deadline recorded.")
            
            else:
                print("Invalid input. Please try again.")
            
            tasks.append(full_task)
        
        else:
            print("Error!")
        
    def view_tasks():
        if len(tasks) == 0:
            print("No tasks found.")
    
        else:
            for i, task in enumerate(tasks, 1):
                print(f"[{i}] {task}")

        
    add_task()
    view_tasks()