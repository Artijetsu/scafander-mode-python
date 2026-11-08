# BUGFIX.md — Task Manager

---

## Версия → Проблема

---

### ![v0.0.1](https://img.shields.io/badge/version-0.0.1-orange) — Каркас приложения

- [x] меню с пунктами: добавить / показать / выход
- [x] обработка неверного пункта меню (сообщение + возврат)

---

### ![v0.0.2](https://img.shields.io/badge/version-0.0.2-orange) — Ввод задач

- [x] тест: 3 задачи подряд, все видны в списке

---

### ![v0.0.3](https://img.shields.io/badge/version-0.0.3-orange) — Функции цикла

- [x] вынести обработку команд `1..5` в отдельные функции

---

### ![v0.0.4](https://img.shields.io/badge/version-0.0.4-orange) — Проверки и подтверждения

- [x] **баг:** `check_confirm` всегда возвращает `False` (`startswith('')`)
- [x] **баг:** `core.deleated_task` удаляет при ответе «нет»
- [x] исправить оба бага, протестировать удаление

---

### ![v0.0.5](https://img.shields.io/badge/version-0.0.5-orange) — Файловые сохранения

- [x] тест: добавили → вышли → запустили → задача на месте

---

### ![v0.0.6](https://img.shields.io/badge/version-0.0.6-orange) — Логика вне цикла

- [x] возврат `True/False` из `core`-функций — успех/неудача
- [x] `app.py` решает, сохранять файл или нет, по результату функции

---

### ![v0.0.7](https://img.shields.io/badge/version-0.0.7-orange) — Точка входа

- [x] обновить docstring версии до `0.0.7` (сейчас `0.0.7`, но список версий отстаёт)

---

### ![v0.0.8](https://img.shields.io/badge/version-0.0.8-orange) — Контент задачи

- [x] **проблема:** `edited_task` теряет содержание (заменяет строку целиком)
- [x] при редактировании спрашивать, что меняем: имя или содержание
- [x] при просмотре показывать имя и содержание раздельно

---

### ![v0.0.9](https://img.shields.io/badge/version-0.0.9-orange) — Модульная разгрузка

- [x] единый стиль комментариев (`"""..."""` сверху модуля)
- [x] пройтись по всем функциям: есть ли docstring

---

### ![v0.1.0](https://img.shields.io/badge/version-0.1.0-orange) — Сборка и документация

- [x] `README.md` с описанием запуска и скриншотом
- [x] `documents/ROADMAP.md` — этот файл
- [x] проверка `.exe` на чистой машине

---

### ![v0.1.1](https://img.shields.io/badge/version-0.1.1-orange) — Структура src и первый GUI

- [x] вынести `view.py` в `ui/` (сейчас он в `src/`, но по смыслу это UI)
- [x] обновить импорты после переноса

---

### ![v0.1.2](https://img.shields.io/badge/version-0.1.2-orange) — Основные экраны Tkinter

- [x] **баг:** `frame_memu` (опечатка, должно быть `frame_menu`)
- [x] **баг:** в `show_all_tasks` переменная `tack` (опечатка)
- [x] **баг:** `root.iconbitmap("../assets/icon.ico")` — путь не работает при запуске из `src/`
- [x] **баг:** двойной `Button` «Выход» создаётся в `frame_menu` (должен быть в `frame_tasks`?)
- [x] кнопки «Посмотреть / Редактировать / Удалить» у каждой задачи
- [x] `messagebox` вместо `print` для сообщений
- [x] `show_edit` и `on_delete` вместо `pass`

---

### ![v0.1.3](https://img.shields.io/badge/version-0.1.3-orange) — Кастомные компоненты

- [x] заменить все `tk.Button` в проекте на `AppButton`
- [x] `PrimaryButton` — синий (Сохранить / Добавить)
- [x] `DangerButton` — красный (Удалить / Выход)
- [x] `SmallButton` — компактный (кнопки в строках задач)
- [x] `AppLabel`, `AppEntry`, `AppFrame` — единый стиль
- [x] `ui/Button.py` → `ui/widgets.py`
- [x] правило: виджеты — только через эти классы
- [x] поиск по проекту: `tk.Button(` — только в `widgets.py`

---
