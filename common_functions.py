# List of months
months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

# List of days per month
days_per_month = [
    31, 28, 31,
    30, 31, 30,
    31, 31, 30,
    31, 30, 31
]

# Function to check if task name is all numbers
def is_all_numbers(text):
    if len(text) == 0:
        return False
    
    numbers = "0123456789"
    for char in text:
        if char not in numbers:
            return False
    return True

# Function to check duplicate tasks
def is_duplicate(task, tasks_list):
    for existing_task in tasks_list:
        if task.lower() == existing_task.lower():
            return True      
    return False

# Function to display tasks with a custom title
def display_tasks(title, tasks_list, deadline_list):
    print("=" * 40)
    print(title)
    print("=" * 40)

    if len(tasks_list) == 0:
        print("No tasks found.")
        return

    for i in range(len(tasks_list)):
        print("[" + str(i + 1) + "]", tasks_list[i], "- Deadline:", deadline_list[i])
