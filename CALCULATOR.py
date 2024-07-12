import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_label.config(text="Result: " + str(result))
    
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and labels using grid layout
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Create operation selection using grid layout
operation_var = tk.StringVar(window)
operation_choices = ['+', '-', '*', '/']
operation_var.set('+')  # default value
operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create calculate button using grid layout
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create label for displaying result using grid layout
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
window.mainloop()
