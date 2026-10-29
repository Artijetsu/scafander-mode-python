"""Графический интерфейс приложения Task Manager"""

import tkinter as tk
from tkinter import messagebox, simpledialog


class Interface:
    """Создает главное окно и элементы управления приложения"""

    def __init__(self, collection, on_save):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("600x400")
        self.root.minsize(400, 300)
        self.collection = collection
        self.on_save = on_save

        self.root.configure(padx=12, pady=12)
        self.listbox = tk.Listbox(self.root, height=14)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        buttons = tk.Frame(self.root)
        buttons.pack(fill=tk.X, pady=(10, 0))
        tk.Button(buttons, text="Добавить", command=self.add_task).pack(side=tk.LEFT, padx=3)
        tk.Button(buttons, text="Изменить", command=self.edit_task).pack(side=tk.LEFT, padx=3)
        tk.Button(buttons, text="Удалить", command=self.delete_task).pack(side=tk.LEFT, padx=3)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for item in self.collection:
            name, _, content = item.strip().partition("|")
            self.listbox.insert(tk.END, f"{name.strip()} - {content.strip()}")

    def selected_index(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Task Manager", "Выберите задачу из списка.")
            return None
        return selection[0]

    def add_task(self):
        name = simpledialog.askstring("Новая задача", "Название задачи:", parent=self.root)
        if name is None:
            return
        content = simpledialog.askstring("Новая задача", "Содержание задачи:", parent=self.root)
        if content is None:
            return
        if not name.strip() or not content.strip():
            messagebox.showwarning("Task Manager", "Название и содержание не должны быть пустыми.")
            return
        self.collection.append(f"{name.strip()} | {content.strip()}\n")
        self.refresh()
        self.on_save()

    def edit_task(self):
        index = self.selected_index()
        if index is None:
            return
        name, _, content = self.collection[index].strip().partition("|")
        new_name = simpledialog.askstring("Изменить задачу", "Название:", initialvalue=name.strip(), parent=self.root)
        if new_name is None:
            return
        new_content = simpledialog.askstring("Изменить задачу", "Содержание:", initialvalue=content.strip(), parent=self.root)
        if new_content is None:
            return
        if not new_name.strip() or not new_content.strip():
            messagebox.showwarning("Task Manager", "Название и содержание не должны быть пустыми.")
            return
        self.collection[index] = f"{new_name.strip()} | {new_content.strip()}\n"
        self.refresh()
        self.on_save()

    def delete_task(self):
        index = self.selected_index()
        if index is None:
            return
        if messagebox.askyesno("Удалить задачу", "Удалить выбранную задачу?", parent=self.root):
            self.collection.pop(index)
            self.refresh()
            self.on_save()

    def run(self):
        self.root.mainloop()
