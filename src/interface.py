import tkinter as tk

score = 0

def start():
    global score
    score += 1
    label.config(text=str(score))

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap("../assets/icon.ico")

header = tk.Frame(root,bg="red", height=100, width=400)
header.pack(side="top", fill="x")

footer = tk.Frame(root,bg="red", height=100, width=400)
header.pack(side="bottom", fill="x")

main = tk.Frame(root,bg="blue", height=100, width=400)
main.pack(side="bottom", fill="x")

button_start = tk.Button(main, text="Старт Движуха", command=start)
button_start.pack()

label = tk.Label(main, text=0, height=1, width=100)
label.pack()



root.mainloop()
