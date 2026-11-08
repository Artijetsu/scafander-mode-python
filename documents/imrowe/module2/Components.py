""" =========================================================
    Компоненты UI. Наследники tk-виджетов с единым стилем.
    Interface использует ТОЛЬКО эти классы.
    =========================================================
"""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text: str = "", **kwargs) -> None:
        pass


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs) -> None:
        pass


class AppButton(tk.Button):
    def __init__(self, master, text: str, command, **kwargs) -> None:
        pass


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs) -> None:
        pass


class AppFrame(tk.Frame):
    def __init__(self, master, **kwargs) -> None:
        pass
