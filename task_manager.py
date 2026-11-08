"""Главный фасад приложения: связывает модель, хранилище и интерфейс."""
import tkinter as tk

from interface import Interface
from storage_manager import StorageManager
from task import Task


class TaskManager:
    """Управляет CRUD-операциями над задачами."""

    def __init__(self, root: tk.Tk) -> None:
        self.storage = StorageManager()
        self.interface = Interface(root)
        self.tasks = self.storage.load()

        self.interface.on_create = self.create_task
        self.interface.on_edit = self.edit_task
        self.interface.on_delete = self.delete_task
        self.interface.on_toggle = self.toggle_status
        self.refresh()

    def create_task(self) -> None:
        """Создать задачу из введенных данных."""
        data = self.interface.get_input()
        if not data["title"]:
            self.interface.show_warning("Ошибка", "Введите название задачи.")
            return
        task = Task(
            title=data["title"],
            description=data["description"],
            author=data["author"] or "—",
        )
        self.storage.add(task)
        self.interface.clear_input()
        self.refresh()

    def edit_task(self) -> None:
        """Изменить выбранную задачу."""
        index = self.interface.get_selected_index()
        if index is None:
            self.interface.show_warning("Внимание", "Выберите задачу из списка.")
            return
        old_task = self.tasks[index]
        data = self.interface.get_input()
        if not data["title"]:
            self.interface.show_warning("Ошибка", "Введите название задачи.")
            return
        updated_task = Task(
            id=old_task.id,
            title=data["title"],
            description=data["description"],
            status=old_task.status,
            author=data["author"] or "—",
            created_at=old_task.created_at,
        )
        self.storage.update(old_task.id, updated_task)
        self.interface.clear_input()
        self.refresh()

    def delete_task(self) -> None:
        """Удалить выбранную задачу после подтверждения."""
        index = self.interface.get_selected_index()
        if index is None:
            self.interface.show_warning("Внимание", "Выберите задачу из списка.")
            return
        task = self.tasks[index]
        if self.interface.ask_confirm("Удаление", f"Удалить задачу «{task.title}»?"):
            self.storage.delete(task.id)
            self.refresh()

    def toggle_status(self) -> None:
        """Изменить статус выбранной задачи."""
        index = self.interface.get_selected_index()
        if index is None:
            self.interface.show_warning("Внимание", "Выберите задачу из списка.")
            return
        task = self.tasks[index]
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            status=not task.status,
            author=task.author,
            created_at=task.created_at,
        )
        self.storage.update(task.id, updated_task)
        self.refresh()

    def refresh(self) -> None:
        """Загрузить актуальные данные и обновить список."""
        self.tasks = self.storage.load()
        self.interface.show_tasks(self.tasks)

    def run(self) -> None:
        """Запустить интерфейс."""
        self.interface.run()
