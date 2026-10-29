"""Загрузка и сохранение задач в JSON."""
import json
from pathlib import Path


def load_tasks(filename):
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(task_collection, filename):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as file:
        json.dump(task_collection, file, ensure_ascii=False, indent=2)
