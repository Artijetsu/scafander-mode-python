"""Загрузка и сохранение задач в JSON."""
import json
from pathlib import Path

from task import Task


class StorageManager:
    """Управляет сохранением коллекции задач."""

    def __init__(self, path: str = "tasks.json") -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.save([])

    def load(self) -> list[Task]:
        """Прочитать задачи из JSON-файла."""
        with self.path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return [Task.from_dict(item) for item in data]

    def save(self, tasks: list[Task]) -> None:
        """Записать список задач в JSON-файл."""
        with self.path.open("w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)

    def add(self, task: Task) -> None:
        """Добавить задачу и назначить ей id."""
        tasks = self.load()
        task.id = max((item.id or 0 for item in tasks), default=0) + 1
        tasks.append(task)
        self.save(tasks)

    def update(self, task_id: int, task: Task) -> None:
        """Обновить задачу с указанным id."""
        tasks = self.load()
        for index, item in enumerate(tasks):
            if item.id == task_id:
                task.id = task_id
                tasks[index] = task
                self.save(tasks)
                return

    def delete(self, task_id: int) -> None:
        """Удалить задачу с указанным id."""
        tasks = [task for task in self.load() if task.id != task_id]
        self.save(tasks)
