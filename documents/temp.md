# Старые участки кода

## view.py

```
====================================================
        Модуль который отображает информацию в консоли 
    ====================================================
"""

"""функция для показа списка задач"""
def show_collection(task_collection):
    print("=" * 30)
    for number, content in enumerate(task_collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word = f"{word}{symbol}"
            else:
                break
        print(number + 1, str(word))
    print("=" * 30)

"""функция для показа меню"""
def show_menu():
    print(' 1 - показать задачи \n'
          ' 2 - добавить задачу \n'
          ' 3 - редактировать \n'
          ' 4 - удалить \n'
          ' 0 - выход ')

``` 
