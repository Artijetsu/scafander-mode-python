""" =========================================================
    Interface — прослойка между логикой и tkinter.
    Не знает про задачи. Только создаёт и обновляет виджеты.
    =========================================================
"""
import tkinter as tk


class Interface:
    """Фасад над tkinter: единый API для TaskManager."""

    def __init__(self, title: str = "Task Manager", width: int = 520, height: int = 520) -> None:
        """Создать корневое окно, настроить размеры и стиль."""
        pass

    # ---------- жизненный цикл ----------
    def run(self) -> None:
        """Запустить главный цикл."""
        pass

    def quit(self) -> None:
        """Закрыть окно."""
        pass

    def clear(self) -> None:
        """Удалить все дочерние виджеты."""
        pass

    # ---------- построение ----------
    def build(self) -> None:
        """Собрать базовый каркас: заголовок, список, поле ввода, кнопки."""
        pass

    # ---------- ввод ----------
    def get_input(self) -> dict:
        """Вернуть {title, description, author} из полей ввода."""
        pass

    def clear_input(self) -> None:
        """Очистить поля ввода."""
        pass

    # ---------- отображение ----------
    def show_tasks(self, tasks: list) -> None:
        """Заполнить список задач (list[Task] или list[dict])."""
        pass

    def show_message(self, title: str, text: str) -> None:
        """Показать информационное сообщение."""
        pass

    def show_warning(self, title: str, text: str) -> None:
        """Показать предупреждение."""
        pass

    def ask_confirm(self, title: str, text: str) -> bool:
        """Спросить подтверждение. True — да, False — нет."""
        pass

    def get_selected_index(self) -> int | None:
        """Индекс выбранной строки в списке или None."""
        pass
