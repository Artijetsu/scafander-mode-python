""" Документация

В данном файле я получал информацию о системе текущего ПК и информацию о нем. Например: Платформа процессора; Версия API; Версия компилятора Python.

"""

import os
import sys
import platform
import datetime
import time


os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
sys_in = sys.path

print(f"Система, ее версия и биты: {os_name, os_version, os_arch}")
print(f"Точная дата: {now.year, now.month, now.day}")


os_processor = platform.processor()
os_name = platform.python_build()
os_version = platform.python_compiler()
haha = sys.float_info
hihi = sys.api_version

print(f"Платформа процессора: {platform.processor()}")
print(f"Пайтон Билд: {platform.python_build()}")
print(f"Компилятор пайтона: {platform.python_compiler()}")
print(f"Информация о float системы: {sys.float_info}")
print(f"Версия API: {sys.api_version}")







