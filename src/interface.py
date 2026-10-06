import tkinter as tk
from functools import partial

window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x300")

entry = tk.Entry(window, justify="right")
entry.pack(fill="x", padx=10, pady=10)

def click(button):
    if button == "=":
        calculate()
    elif button == "C":
        clear()
    else:
        entry.insert(tk.END, button)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

frame = tk.Frame(window)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

for i in range(len(buttons)):
    row = i // 4
    column = i % 4

    button = tk.Button(
        frame,
        text=buttons[i],
        width=5,
        height=2,
        command=partial(click, buttons[i])
    )

    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(
    frame,
    text="C",
    width=23,
    height=2,
    command=partial(click, "C")
)

clear_button.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=5,
    pady=5
)

window.mainloop()