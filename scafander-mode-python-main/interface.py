"""Графический интерфейс приложения Task Manager."""
import tkinter as tk
from tkinter import messagebox, simpledialog

from AppButton import AppButton
from AppLabel import AppLabel
from AppListbox import AppListbox


class Interface:
    """Главное окно и элементы управления."""

    def __init__(self, collection, on_save):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("600x420")
        self.root.minsize(420, 300)
        self.collection = collection
        self.on_save = on_save

        AppLabel(self.root, text="Мои задачи", font=("Arial", 14, "bold")).pack(pady=(0, 8))
        self.listbox = AppListbox(self.root, height=14)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        buttons = tk.Frame(self.root)
        buttons.pack(fill=tk.X, pady=(10, 0))
        AppButton(buttons, "Добавить", self.add_task).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Изменить", self.edit_task).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Удалить", self.delete_task).pack(side=tk.LEFT, padx=3)
        self.show_tasks()

    def show_tasks(self):
        """Показывает актуальный список задач."""
        self.listbox.show_tasks(self.collection)

    def selected_index(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Task Manager", "Выберите задачу из списка.", parent=self.root)
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
            messagebox.showwarning("Task Manager", "Название и содержание не должны быть пустыми.", parent=self.root)
            return
        self.collection.append({"name": name.strip(), "content": content.strip()})
        self.show_tasks()
        self.on_save()

    def edit_task(self):
        index = self.selected_index()
        if index is None:
            return
        task = self.collection[index]
        new_name = simpledialog.askstring("Изменить задачу", "Название:", initialvalue=task.get("name", ""), parent=self.root)
        if new_name is None:
            return
        new_content = simpledialog.askstring("Изменить задачу", "Содержание:", initialvalue=task.get("content", ""), parent=self.root)
        if new_content is None:
            return
        if not new_name.strip() or not new_content.strip():
            messagebox.showwarning("Task Manager", "Название и содержание не должны быть пустыми.", parent=self.root)
            return
        self.collection[index] = {"name": new_name.strip(), "content": new_content.strip()}
        self.show_tasks()
        self.on_save()

    def delete_task(self):
        index = self.selected_index()
        if index is None:
            return
        if messagebox.askyesno("Удалить задачу", "Удалить выбранную задачу?", parent=self.root):
            self.collection.pop(index)
            self.show_tasks()
            self.on_save()

    def run(self):
        self.root.mainloop()
