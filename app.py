import tkinter as tk
import ttkbootstrap as ttk


# setup git

class App(tk.Tk):
	def __init__(self, title="Default"):
		super().__init__()

		self.title(title)
		self.geometry("300x400"); self.resizable(0,0)

		self.mainloop()


class Display(ttk.Frame):
	def __init__(self, container):
		super().__init__(container)

		pass


class Buttons(ttk.Frame):
	def __init__(self, container):
		super().__init__(container)

		pass


if __name__ == '__main__':
	app = App("Calculator")