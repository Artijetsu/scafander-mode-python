"""Пользовательские tkinter-компоненты с единым стилем."""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text: str = "", **kwargs) -> None:
        kwargs.setdefault("font", ("Arial", 10))
        kwargs.setdefault("anchor", "w")
        super().__init__(master, text=text, **kwargs)


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs) -> None:
        kwargs.setdefault("font", ("Arial", 10))
        super().__init__(master, **kwargs)


class AppButton(tk.Button):
    def __init__(self, master, text: str, command, **kwargs) -> None:
        kwargs.setdefault("font", ("Arial", 10))
        kwargs.setdefault("padx", 8)
        kwargs.setdefault("pady", 4)
        super().__init__(master, text=text, command=command, **kwargs)


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs) -> None:
        kwargs.setdefault("font", ("Arial", 10))
        kwargs.setdefault("selectmode", tk.SINGLE)
        super().__init__(master, **kwargs)


class AppFrame(tk.Frame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
