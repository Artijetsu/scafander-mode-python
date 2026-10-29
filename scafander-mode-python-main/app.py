"""Основное приложение Task Manager."""
from storage import load_tasks, save_tasks
from config import NAME_FILE_SAVES
from utils import insure_saves_file
from interface import Interface


def app():
    name_file = NAME_FILE_SAVES
    insure_saves_file(name_file)
    collection = load_tasks(name_file)

    def save():
        save_tasks(collection, name_file)

    window = Interface(collection, save)
    window.run()
