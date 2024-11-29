import tkinter as tk

# Function to update the entry widget when buttons are pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current value in the entry widget
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())  # Evaluates the mathematical expression entered
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, result)  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Display error if invalid expression

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget to display calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create the buttons and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='Clear', width=22, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the Tkinter event loop
root.mainloop()