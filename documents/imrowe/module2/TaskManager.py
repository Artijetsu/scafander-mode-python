""" =========================================================
    TaskManager — главный фасад.
    Связывает Task, StorageManager и Interface.
    =========================================================
"""
import tkinter as tk
from task import Task
from storage_manager import StorageManager
from interface import Interface


class TaskManager:
    """Оркестратор приложения. Единственная точка входа для UI."""

    def __init__(self, root: tk.Tk) -> None:
        """Создать StorageManager и Interface, привязать колбэки."""
        pass

    # ---------- CRUD ----------
    def create_task(self) -> None:
        """Прочитать ввод → создать Task → сохранить → обновить список."""
        pass

    def edit_task(self) -> None:
        """Взять выбранную задачу → изменить → сохранить → обновить."""
        pass

    def delete_task(self) -> None:
        """Удалить выбранную задачу (с подтверждением)."""
        pass

    def toggle_status(self) -> None:
        """Переключить статус выбранной задачи."""
        pass

    # ---------- служебное ----------
    def refresh(self) -> None:
        """Перечитать задачи из StorageManager и отрисовать."""
        pass

    def run(self) -> None:
        """Передать управление Interface."""
        pass
