# Codsoft
# To do list app
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        update_task_listbox()
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        del tasks[task_index]
        update_task_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def edit_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_text = tasks[task_index]
        new_task_text = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task_text)
        if new_task_text:
            tasks[task_index] = new_task_text
            update_task_listbox()
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to edit.")

def mark_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_text = tasks[task_index]
        tasks[task_index] = f"[Completed] {task_text}"
        update_task_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            return file.read().splitlines()
    return []

def save_tasks():
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Initialize tasks and file name
tasks = []
tasks_file = "tasks.txt"

# Create the GUI components
frame = tk.Frame(root)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width=50, height=10, bd=0, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", width=48, command=delete_task)
delete_task_button.pack(pady=5)

edit_task_button = tk.Button(root, text="Edit Task", width=48, command=edit_task)
edit_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Mark Task as Completed", width=48, command=mark_task)
mark_task_button.pack(pady=5)

# Load tasks from file and update the listbox
tasks = load_tasks()
update_task_listbox()

# Run the main loop
root.mainloop()
