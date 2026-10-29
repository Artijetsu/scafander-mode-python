"""Список задач с методом обновления отображения."""
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def show_tasks(self, tasks):
        self.delete(0, tk.END)
        for task in tasks:
            self.insert(tk.END, f"{task.get('name', '')} - {task.get('content', '')}")
