import os
 
# ================= SCREEN CLEAR =================
 
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
 
# ================= SIMPLE HEADER =================
 
def print_header(title):

    total_width = 40
    spaces = (total_width - len(title)) // 2

    print("╔" + "═"*40 + "╗")
    print("║" + " " * spaces + title + " " * spaces + "║")
    print("╚" + "═"*40 + "╝")
 
 # ================= COLUMN CENTER =================
 
def column_header(text, width):
 
    spaces = (width - len(text)) // 2
 
    return (
        " " * spaces
        + text
        + " " * spaces
    )

# ================= STATUS MESSAGES =================

def success(message):
    print("[✓]", message)

def error(message):
    print("[✗]", message)

def notice(message):
    print("[!]", message)
    
# ================= MONTHS =================
 
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
 
# ================= NUMBER CHECK =================
 
def is_all_numbers(text):
 
    if len(text) == 0:
        return False
 
    numbers = "0123456789"
 
    for char in text:
        if char not in numbers:
            return False
 
    return True
 
# ================= DUPLICATE CHECK =================
 
def is_duplicate(task, tasks_list):
 
    for existing_task in tasks_list:
 
        if task.lower() == existing_task.lower():
            return True
 
    return False
 
# ================= TABLE VIEW =================
 
def display_tasks(title, tasks_list, deadline_list):
 
    print_header(title)
 
    if len(tasks_list) == 0:
        notice("No tasks found.")
        return
 
    print("┌─────┬────────────────────────┬──────────────────┐")
 
    print(
        "│"
        + column_header("No.",5)
        + "│"
        + column_header("Task",24)
        + "│"
        + column_header("Deadline",18)
        + "│"
    )
 
    print("├─────┼────────────────────────┼──────────────────┤")
 
    for i in range(len(tasks_list)):
 
        number = str(i + 1)
 
        print(
            "│ "
            + number
            + "   │ "
            + tasks_list[i][:22]
            + " │ "
            + deadline_list[i][:16]
            + " │"
        )
 
    print("└─────┴────────────────────────┴──────────────────┘")