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
    print(" " * spaces + title)
    print("╚" + "═"*40 + "╝")
 
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
        print("No tasks found.")
        return
 
    print("----------------------------------------------")
 
    for i in range(len(tasks_list)):
 
        print(
            "[" + str(i + 1) + "]",
            tasks_list[i],
            "|",
            deadline_list[i]
        )
 
    print("----------------------------------------------")