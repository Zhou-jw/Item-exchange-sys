from logging import root
import tkinter as tk
from tkinter import messagebox
from db import MysqlDatabases
from indexPage import index

if __name__ == '__main__':
    root = tk.Tk()
    index(root)
    root.mainloop()


    