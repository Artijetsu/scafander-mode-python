"""Классы задач для приложения Task Manager"""


class Task:
    """Родительский класс задачи"""

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_description(self):
        return f"{self.name}: {self.content}"

    def get_type(self):
        return "Обычная задача"


class PersonalTask(Task):
    """Класс личной задачи"""

    def get_description(self):
        return f"Личная задача: {self.name} - {self.content}"

    def get_type(self):
        return "Личная"


class WorkTask(Task):
    """Класс рабочей задачи"""

    def get_description(self):
        return f"Рабочая задача: {self.name} - {self.content}"

    def get_type(self):
        return "Рабочая"
