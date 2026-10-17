import tkinter as tk

SIZE = 5
CELL = 60
GAP = 8
COLORS = ["#2d6cdf", "#ef476f", "#ffd166", "#06d6a0"]

root = tk.Tk()
root.title("Узор из кнопок")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

i = 0
while i < SIZE * SIZE:
    row = i // SIZE
    col = i % SIZE
    button = tk.Button(
        frame,
        text=str(i + 1),
        width=5,
        height=2,
        bg=COLORS[(row + col) % len(COLORS)],
        activebackground="#ffffff"
    )
    button.grid(row=row, column=col, padx=GAP // 2, pady=GAP // 2)
    i += 1

root.mainloop()
