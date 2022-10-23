import tkinter as tk
from tkinter import ttk
from db import db
class ItemFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self).pack()

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

        self.show_data_frame()
    
    def create_page(self):
        columns = ("name")
        self.tree_view = ttk.Treeview(self, show="headings", columns = columns)
        # self.tree_view.column('id', width = 80, anchor='center')
        self.tree_view.column('name', width = 80, anchor='center')
        # self.tree_view.heading('id', text='id')
        self.tree_view.heading('name', text='item')
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        tk.Button(self, text='refresh', command=self.show_data_frame).pack(anchor=tk.E, pady = 5)

    def show_data_frame(self):
        # 删除旧的数据
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        items = db.all()
        items = items["items"]
        # id = 1
        for item in items:
            self.tree_view.insert('', 1, values=(
                item
            ))
            # id += 1

class AddFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        # tk.Label(self, text='add').pack()

        self.item = tk.StringVar()
        self.status = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='item').grid(row=1, column=0)
        tk.Entry(self, textvariable=self.item).grid(row=1, column=1, pady=10)

        tk.Button(self, text='输入', command=self.record_info).grid(row=2, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=3, column=2, pady=10, stick=tk.E)

    def record_info(self):
        item = self.item.get()
        self.item.set('')
        print(item)
        db.insert(item)
        
        self.status.set('添加成功！')


class DeleteFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='delete').pack()

        self.status = tk.StringVar()
        self.item = tk.StringVar()
        tk.Label(self, text='item name').pack()
        tk.Entry(self, textvariable=self.item).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()
    def delete(self):
        item_name = self.item.get()
        flag, msg = db.delete(item_name)
        self.status.set(msg)

class SearchFrame(tk.Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
        tk.Label(self, text='search').pack()

        self.status = tk.StringVar()
        self.item = tk.StringVar()
        tk.Label(self, text='item name').pack()
        tk.Entry(self, textvariable=self.item).pack()
        tk.Button(self, text='查找', command=self.search).pack()
        tk.Label(self, textvariable=self.status).pack()

    def search(self):
        item_name = self.item.get()
        flag, msg = db.search(item_name)
        self.status.set(msg)
