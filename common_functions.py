import os
 
# ================= SCREEN CLEAR =================
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
 
 
# ================= HEADER =================
def print_header(title):
 
    width = 40
    space = (width - len(title)) // 2
    extra = width - len(title) - space
 
    print("╔" + "═" * width + "╗")
    print("║" + " " * space + title + " " * extra + "║")
    print("╚" + "═" * width + "╝")
 
 
# ================= STATUS MESSAGES =================
def success(msg):
    print("[✓]", msg)
 
def error(msg):
    print("[✗]", msg)
 
def notice(msg):
    print("[!]", msg)
 
 
# ================= DATA =================
months = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
 
days_per_month = [
    31,28,31,30,31,30,
    31,31,30,31,30,31
]
 
 
# ================= VALIDATION =================
def is_all_numbers(text):
    if len(text) == 0:
        return False
    for c in text:
        if c not in "0123456789":
            return False
    return True
 
 
def is_negative_number(text):
    if len(text) == 0:
        return False
 
    if text[0] != "-":
        return False
 
    i = 1
    while i < len(text):
        if text[i] not in "0123456789":
            return False
        i += 1
 
    return True
 
 
def is_special_characters(text):
    for c in text:
        if c not in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~":
            return False
        return True
 
 
def is_duplicate(task, task_list):
    for t in task_list:
        if task.lower() == t.lower():
            return True
    return False
 
 
# ================= TABLE DISPLAY =================
def pad(text, width):
    text = str(text)
 
    if len(text) > width:
        text = text[:width]
 
    return text + " " * (width - len(text))
 
 
def display_tasks(title, tasks_list, deadline_list):
 
    print_header(title)
 
    if len(tasks_list) == 0:
        notice("No tasks found.")
        return
 
    no_width = 6
    task_width = 26
    deadline_width = 22
 
    print("┌" + "─" * no_width + "┬" + "─" * task_width + "┬" + "─" * deadline_width + "┐")
 
    print(
        "│" +
        pad("No.", no_width) +
        "│" +
        pad("Task", task_width) +
        "│" +
        pad("Deadline", deadline_width) +
        "│"
    )
 
    print("├" + "─" * no_width + "┼" + "─" * task_width + "┼" + "─" * deadline_width + "┤")
 
    for i in range(len(tasks_list)):
        print(
            "│" +
            pad(i + 1, no_width) +
            "│" +
            pad(tasks_list[i], task_width) +
            "│" +
            pad(
                "No Deadline" if deadline_list[i] is None else deadline_list[i],
                deadline_width
            ) +
            "│"
        )
 
    print("└" + "─" * no_width + "┴" + "─" * task_width + "┴" + "─" * deadline_width + "┘")