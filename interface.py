"""Графический интерфейс. Не содержит логику управления задачами."""
import tkinter as tk
from tkinter import messagebox

from components import AppButton, AppEntry, AppFrame, AppLabel, AppListbox


class Interface:
    """Создает окно и предоставляет API для TaskManager."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x560")
        self.root.minsize(480, 440)

        self.on_create = None
        self.on_edit = None
        self.on_delete = None
        self.on_toggle = None

        self.build()

    def run(self) -> None:
        """Запустить главный цикл tkinter."""
        self.root.mainloop()

    def quit(self) -> None:
        """Закрыть приложение."""
        self.root.destroy()

    def clear(self) -> None:
        """Удалить все виджеты из окна."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def build(self) -> None:
        """Создать поля ввода, список задач и кнопки управления."""
        form = AppFrame(self.root, padx=12, pady=10)
        form.pack(fill=tk.X)

        AppLabel(form, text="Название задачи").grid(row=0, column=0, sticky="w", pady=3)
        self.title_entry = AppEntry(form)
        self.title_entry.grid(row=0, column=1, sticky="ew", pady=3)

        AppLabel(form, text="Описание").grid(row=1, column=0, sticky="w", pady=3)
        self.description_entry = AppEntry(form)
        self.description_entry.grid(row=1, column=1, sticky="ew", pady=3)

        AppLabel(form, text="Автор").grid(row=2, column=0, sticky="w", pady=3)
        self.author_entry = AppEntry(form)
        self.author_entry.grid(row=2, column=1, sticky="ew", pady=3)
        form.columnconfigure(1, weight=1)

        self.listbox = AppListbox(self.root, height=14)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

        buttons = AppFrame(self.root, padx=12, pady=8)
        buttons.pack(fill=tk.X)
        AppButton(buttons, "Добавить", self._create).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Изменить", self._edit).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Удалить", self._delete).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Статус", self._toggle).pack(side=tk.LEFT, padx=3)
        AppButton(buttons, "Выход", self.quit).pack(side=tk.RIGHT, padx=3)

    def _create(self) -> None:
        if self.on_create:
            self.on_create()

    def _edit(self) -> None:
        if self.on_edit:
            self.on_edit()

    def _delete(self) -> None:
        if self.on_delete:
            self.on_delete()

    def _toggle(self) -> None:
        if self.on_toggle:
            self.on_toggle()

    def get_input(self) -> dict:
        """Вернуть значения полей ввода."""
        return {
            "title": self.title_entry.get().strip(),
            "description": self.description_entry.get().strip(),
            "author": self.author_entry.get().strip(),
        }

    def clear_input(self) -> None:
        """Очистить поля ввода."""
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)

    def show_tasks(self, tasks: list) -> None:
        """Показать список задач."""
        self.listbox.delete(0, tk.END)
        for task in tasks:
            status = "Выполнена" if task.status else "Не выполнена"
            self.listbox.insert(tk.END, f"{task.id}. {task.title} | {status} | {task.author}")

    def show_message(self, title: str, text: str) -> None:
        messagebox.showinfo(title, text, parent=self.root)

    def show_warning(self, title: str, text: str) -> None:
        messagebox.showwarning(title, text, parent=self.root)

    def ask_confirm(self, title: str, text: str) -> bool:
        return messagebox.askyesno(title, text, parent=self.root)

    def get_selected_index(self) -> int | None:
        selection = self.listbox.curselection()
        return selection[0] if selection else None
