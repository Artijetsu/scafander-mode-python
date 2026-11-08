"""Точка входа приложения Task Manager."""
import tkinter as tk

from task_manager import TaskManager


def main() -> None:
    root = tk.Tk()
    app = TaskManager(root)
    app.run()


if __name__ == "__main__":
    main()
