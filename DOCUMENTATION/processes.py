"""программа для работы с процессами"""

import subprocess as sp
import os
import multiprocessing as mp
import time


def main():
    print("Starting...")
    print(f"pid : {os.getpid()}")
    print(f"ppid : {os.getppid()}")
    time.sleep(5)
    welcome()

def welcome():
    print("Welcome!")
    print(f"pid : {os.getpid()}")
    time.sleep(5)
    work()

def work():
    print("Working...")
    print(f"pid : {os.getpid()}")
    time.sleep(5)

def finish():
    print("Finished!")
    print(f"pid : {os.getpid()}")
    time.sleep(5)

if __name__ == '__main__':
    main()













