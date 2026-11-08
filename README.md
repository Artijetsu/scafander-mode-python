# Task Manager

Модульное приложение для управления задачами на Python и tkinter.

## Запуск

Запустите файл `main.py`:

```bash
python main.py
```

Задачи автоматически сохраняются в файл `tasks.json` в формате JSON.

## Структура проекта

- `main.py` — точка входа.
- `task.py` — модель задачи `Task`.
- `storage_manager.py` — загрузка и сохранение задач (`StorageManager`).
- `components.py` — компоненты интерфейса на основе tkinter.
- `interface.py` — графический интерфейс (`Interface`).
- `task_manager.py` — логика CRUD и связь компонентов (`TaskManager`).
