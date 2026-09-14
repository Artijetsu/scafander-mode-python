"""Основной файл приложения

    версия 0.0.3

    === Описание ===
        Приложение может сохранять задачи, выдает список задач, и может удалять и редактировтаь задачи

"""
from random import choice

collection = ['task1', 'task2'] #list of tusks
is_running = True

def show_collection(task_collection):
    print("=" * 45)
    for i, j in enumerate(collection):
        print(i + 1, j)
    print("=" * 45)

def show_menu():
    print("1 - Показать задачи \n"
          "2 - Добавить задачу \n"
          "3 - Редактировать задачи \n"
          "4 - Удаление задачи \n"
          "5 - Выход")

while (is_running):
    choice_user = input('Введите ваш выбор: ')
    match str(choice_user):
        case "1":
            show_collection(collection)

        case "2":
            add_tusk = input("Введите имя задачи для добавления: ")
            collection.append(add_tusk)

        case "3":
            show_collection(collection)
            select_tusk = int(input("Введите номер задачи: "))
            edit_tusk = input("Введите новое имя задачи для редактирования: ")
            collection[select_tusk - 1] = edit_tusk

        case "4":
            show_collection(collection)
            delete_tusk = int(input("Введите номер задачи для удаления: "))
            collection.pop(delete_tusk - 1)

        case "5":
            is_running = False
            print("До свидиния!")

        case _:
            print('Такого пункта нет...')