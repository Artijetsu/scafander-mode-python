"""Функции отображения задач в консольной версии"""

def show_collection(task_collection):
    print("=" * 45)
    if not task_collection:
        print("Список задач пуст!")
    else:
        for number, task in enumerate(task_collection, start=1):
            if isinstance(task, dict):
                name = task.get("name", "")
                content = task.get("content", "")
            else:
                name, _, content = task.strip().partition("|")
            print(f"{number}. {name.strip()}\n   Содержание: {content.strip()}")
    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удаление задачи")
    print("5 - Выход")
