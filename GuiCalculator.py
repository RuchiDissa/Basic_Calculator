import tkinter as tk

root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg="#222831")  # Dark background for the window

for i in  range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Entry box styling
entry = tk.Entry(root, width=18, font=('Arial', 24), bd=5, relief='sunken',
                 justify='right', bg="#eeeeee", fg="#222831")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def add_plus(): entry.insert(tk.END, "+")
def add_minus(): entry.insert(tk.END, "-")
def add_multy(): entry.insert(tk.END, "*")
def add_div(): entry.insert(tk.END, "/")
def clear_entry(): entry.delete(0, tk.END)
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def num_entry(num): entry.insert(tk.END, str(num))

# Button style presets
button_style = {
    'width': 10,
    'height': 2,
    'font': ('Arial', 12),
    'bg': '#393E46',
    'fg': '#EEEEEE',
    'activebackground': '#00ADB5',
    'activeforeground': '#FFFFFF',
    'bd': 0
}
operator_style = button_style.copy()
operator_style['bg'] = '#00ADB5'
operator_style['fg'] = '#FFFFFF'

# Buttons grid layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('Clear', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, command=equal, **operator_style)
    elif text == 'Clear':
        btn = tk.Button(root, text=text, command=clear_entry, **operator_style)
        btn.config(width=42)
        btn.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
        continue
    elif text in ['+', '-', '*', '/']:
        cmd = {'+': add_plus, '-': add_minus, '*': add_multy, '/': add_div}[text]
        btn = tk.Button(root, text=text, command=cmd, **operator_style)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: num_entry(t), **button_style)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Keyboard binding
def key_pressed(event):
    key = event.char
    if key in '0123456789.+-*/':
        entry.insert(tk.END, key)
    elif event.keysym == 'Return':
        equal()
    elif event.keysym == 'BackSpace':
        entry.delete(len(entry.get()) - 1, tk.END)
    elif event.keysym == 'Escape':
        clear_entry()

root.bind("<Key>", key_pressed)

root.mainloop()
