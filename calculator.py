import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Display
display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.pack(fill="both", ipadx=8, pady=10, padx=10)

# Functions
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: click(x) if x not in ['C', '='] else (clear() if x == 'C' else calculate())
        tk.Button(frame, text=btn, font=("Arial", 16), command=action).pack(side="left", expand=True, fill="both")

# Run app
root.mainloop()


#tayyab