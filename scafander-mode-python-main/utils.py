"""Вспомогательные функции приложения"""
import os
import sys


def check_confirm(select_task, task_list):
    return select_task.isdigit() and 0 < int(select_task) <= len(task_list)


def get_base_din():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.realpath(__file__))


def insure_saves_file(name_file):
    if not os.path.exists(name_file):
        with open(name_file, "w", encoding="utf-8") as file:
            file.write("[]")
