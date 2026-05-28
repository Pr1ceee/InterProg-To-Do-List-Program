import os
 
# ================= SCREEN CLEAR =================
 
def clear_screen():
 
    if os.name == "nt":
        os.system("cls")
 
    else:
        os.system("clear")
 
# ================= HEADER BOX =================
 
def print_header(title):
 
    total_width = 40
 
    left_spaces = (total_width - len(title)) // 2
    right_spaces = total_width - len(title) - left_spaces
 
    print("╔" + "═"*40 + "╗")
 
    print(
        "║"
        + " " * left_spaces
        + title
        + " " * right_spaces
        + "║"
    )
 
    print("╚" + "═"*40 + "╝")
 
# ================= COLUMN CENTER =================
 
def column_header(text, width):
 
    left = (width - len(text)) // 2
    right = width - len(text) - left
 
    return (
        " " * left
        + text
        + " " * right
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
    "January","February","March",
    "April","May","June",
    "July","August","September",
    "October","November","December"
]
 
days_per_month = [
    31,28,31,
    30,31,30,
    31,31,30,
    31,30,31
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
 
# ================= TASK TABLE =================
 
def display_tasks(title, tasks_list, deadline_list):
 
    print_header(title)
 
    if len(tasks_list) == 0:
        notice("No tasks found.")
        return
 
    no_width = 5
    task_width = 24
    deadline_width = 18
 
    print(
        "┌" + "─"*no_width +
        "┬" + "─"*task_width +
        "┬" + "─"*deadline_width +
        "┐"
    )
 
    print(
        "│"
        + column_header("No.", no_width)
        + "│"
        + column_header("Task", task_width)
        + "│"
        + column_header("Deadline", deadline_width)
        + "│"
    )
 
    print(
        "├" + "─"*no_width +
        "┼" + "─"*task_width +
        "┼" + "─"*deadline_width +
        "┤"
    )
 
    for i in range(len(tasks_list)):
 
        number = str(i + 1)
 
        task = tasks_list[i][:22]
        deadline = deadline_list[i][:16]
 
        print(
            "│ "
            + number
            + " "*(no_width-1-len(number))
            + "│ "
            + task
            + " "*(task_width-2-len(task))
            + "│ "
            + deadline
            + " "*(deadline_width-2-len(deadline))
            + "│"
        )
 
    print(
        "└" + "─"*no_width +
        "┴" + "─"*task_width +
        "┴" + "─"*deadline_width +
        "┘"
    )