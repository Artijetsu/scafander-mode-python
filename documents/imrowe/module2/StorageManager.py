""" =========================================================
    StorageManager — сохранение и загрузка задач.
    Сейчас JSON, в будущем — замена на БД без смены API.
    =========================================================
"""
from task import Task


class StorageManager:
    """Управляет персистентностью коллекции задач."""

    def __init__(self, path: str = "tasks.json") -> None:
        """Запомнить путь к файлу, при необходимости — создать."""
        pass

    def load(self) -> list[Task]:
        """Прочитать все задачи из хранилища."""
        pass

    def save(self, tasks: list[Task]) -> None:
        """Записать весь список задач в хранилище."""
        pass

    def add(self, task: Task) -> None:
        """Добавить одну задачу."""
        pass

    def update(self, task_id: int, task: Task) -> None:
        """Обновить задачу по id."""
        pass

    def delete(self, task_id: int) -> None:
        """Удалить задачу по id."""
        pass
