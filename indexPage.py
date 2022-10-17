import tkinter as tk
from view import ItemFrame, AddFrame, DeleteFrame, SearchFrame
class index():
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.geometry('600x400')
        self.root.title('items exchange system')
        self.create_page()

    def create_page(self):
        self.item_frame = ItemFrame(self.root)
        self.add_frame = AddFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.search_frame = SearchFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label = 'item', command = self.show_item)
        menubar.add_command(label = 'add', command = self.show_add)
        menubar.add_command(label = 'delete', command = self.show_delete)
        menubar.add_command(label = 'search', command = self.show_search)
        
        self.root['menu'] = menubar

    def show_item(self):
        self.item_frame.pack()
        self.add_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_add(self):
        self.item_frame.pack_forget()
        self.add_frame.pack()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()
    
    def show_delete(self):
        self.item_frame.pack_forget()
        self.add_frame.pack_forget()
        self.delete_frame.pack()
        self.search_frame.pack_forget()

    def show_search(self):
        self.item_frame.pack_forget()
        self.add_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack()

if __name__ == '__main__':
    root = tk.Tk()
    index(root)
    root.mainloop()
