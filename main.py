from logging import root
import tkinter as tk
from tkinter import messagebox
from db import MysqlDatabases
from indexPage import index

class mainPage():
    def __init__(self, master) -> None:
        self.root_window = tk.Tk()
        self.root_window.title('Items exchange system')
        self.root_window.geometry('400x300+300+200')

        self.page = tk.Frame(self.root_window)
        self.page.pack()

if __name__ == '__main__':
    root = tk.Tk()
    index(root)
    root.mainloop()


    