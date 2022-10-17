import tkinter as tk
from tkinter import ttk
from db import db
class ItemFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='items').pack()

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

        self.show_data_frame()
    
    def create_page(self):
        columns = ("id", "name")
        self.tree_view = ttk.Treeview(self, show="headings", columns = columns)
        self.tree_view.column('id', width = 80, anchor='center')
        self.tree_view.column('name', width = 80, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('name', text='name')
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        tk.Button(self, text='refresh', command=self.show_data_frame).pack(anchor=tk.E, pady = 5)

    def show_data_frame(self):
        # 删除旧的数据
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        items = db.all()
        items = items["items"]
        id = 1
        for item in items:
            self.tree_view.insert('', 1, values=(
                id, item
            ))
            id += 1

class AddFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='add').pack()

class DeleteFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='delete').pack()

class SearchFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='search').pack()