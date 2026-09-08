"""Основной файл приложения
    версия 0.0.2
"""
from random import choice

collection = ['task1', 'task2', 'task3']
is_start = True

while (is_start):
    print("1 - Показать задачи / 2 - Добавить заметку")
    choice_user = input("Введите ваш выбор (1 или 2): ")

    match choice_user:
        case 1:
            print(collection)
        case 2:
            collection.append('task')
            print(collection)
        case _:
            print("Такого пункта нет!")