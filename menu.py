import tkinter as tk
import ttkbootstrap as ttk


# needs to complete

class MainMenu(tk.Menu):
    def __init__(self, container):
        super().__init__()

        self.hot_keys_menu = tk.Menu(self)
        self.add_cascade(label="Hot Keys", menu=self.hot_keys_menu)

        self.hot_keys_menu.add_command(label="key bindings", command=self.place_frame)
    
    def place_frame(self):
        self.s = ttk.Style()
        self.s.configure("TFrame", background="gray")

        self.config(width=200, height=200, style="TFrame")
        self.place(0, 0)