import tkinter as tk
import ttkbootstrap as ttk


class App(tk.Tk):
	def __init__(self, title="Default"):
		super().__init__()

		self.title(title)
		self.geometry("300x400")
		self.resizable(0,0)

		self.top_expression = ""
		self.expression = ""

		self.display = Display(self)
		self.buttons = Buttons(self)

		self.mainloop()

	def set_expr(self, word: str) -> None:
		self.expression += word
		self.top_expression = self.expression
		self.display.display_expr(self.expression, self.top_expression)

	def set_operator(self, operator: str) -> None:
		self.expression += operator
		self.top_expression = self.expression
		self.display.display_expr(self.expression, self.top_expression)


	def calculate(self, after: str="") -> float:
		try:
			res = eval(self.expression)
			if res-int(res)==0:
				self.expression = str(int(res))
			else:
				self.expression = str(res)
				self.expression = "%.10f"%float(self.expression)
			self.expression += after
			self.display.display_expr(self.expression)
		except SyntaxError:
			self.display.display_expr("Enter a valid expression!")
		except ZeroDivisionError:
			self.display.display_expr("Don't divide by zero!")


	def erase(self) -> None:
		self.expression = ""
		self.top_expression = ""
		self.display.display_expr("---", "-")
	
	def backspace(self) -> None:
		self.expression = self.expression[:-1]
		self.top_expression = self.expression
		self.display.display_expr(self.expression, self.top_expression)


class Display(ttk.Frame):
	def __init__(self, container):
		super().__init__(container)

		self.top_string = ttk.Label(self, text="-", font="14")
		self.main_label = ttk.Label(self, text="---", font="Calibri 20")

		self.top_string.pack(fill="x")
		self.main_label.pack(fill="x")

		self.pack(fill="both", pady=20)
	
	def display_expr(self, expr: str, top_expr: str="-") -> None:
		self.top_string.config(text=top_expr)
		self.main_label.config(text=expr)


class Buttons(ttk.Frame):
	def __init__(self, container):
		super().__init__(container)

		s = ttk.Style()
		s.configure("TFrame", background="lightgreen")

		self.config(padding=2)
		options = {"padx": 1, "pady": 1}


		for i in range(4): self.columnconfigure(index=i, weight=1)
		for i in range(5): self.rowconfigure(index=i, weight=1)

		ttk.Button(self, text="C", command=lambda: container.erase(),
		).grid(column=0, row=0, sticky="nswe", **options)
		ttk.Button(self, text="<-", command=lambda: container.backspace(),
		).grid(column=1, row=0, sticky="nswe", **options)

		ttk.Button(self, text="0", command=lambda: container.set_expr("0"),
		).grid(column=0, row=4, sticky="nswe", **options)

		ttk.Button(self, text="1", command=lambda: container.set_expr("1"),
		).grid(column=0, row=1, sticky="nswe", **options)
		ttk.Button(self, text="2", command=lambda: container.set_expr("2"),
		).grid(column=1, row=1, sticky="nswe", **options)
		ttk.Button(self, text="3", command=lambda: container.set_expr("3"),
		).grid(column=2, row=1, sticky="nswe", **options)

		ttk.Button(self, text="4", command=lambda: container.set_expr("4"),
		).grid(column=0, row=2, sticky="nswe", **options)
		ttk.Button(self, text="5", command=lambda: container.set_expr("5"),
		).grid(column=1, row=2, sticky="nswe", **options)
		ttk.Button(self, text="6", command=lambda: container.set_expr("6"),
		).grid(column=2, row=2, sticky="nswe", **options)

		ttk.Button(self, text="7", command=lambda: container.set_expr("7"),
		).grid(column=0, row=3, sticky="nswe", **options)
		ttk.Button(self, text="8", command=lambda: container.set_expr("8"),
		).grid(column=1, row=3, sticky="nswe", **options)
		ttk.Button(self, text="9", command=lambda: container.set_expr("9"),
		).grid(column=2, row=3, sticky="nswe", **options)

		ttk.Button(self, text="^2", command=None,
		).grid(column=3, row=0, sticky="nswe", **options)
		ttk.Button(self, text="+", command=lambda: container.set_operator("+"),
		).grid(column=3, row=1, sticky="nswe", **options)
		ttk.Button(self, text="-", command=lambda: container.set_operator("-"),
		).grid(column=3, row=2, sticky="nswe", **options)
		ttk.Button(self, text="*", command=lambda: container.set_operator("*"),
		).grid(column=3, row=3, sticky="nswe", **options)
		ttk.Button(self, text="/", command=lambda: container.set_operator("/"),
		).grid(column=3, row=4, sticky="nswe", **options)

		ttk.Button(self, text="=", command=lambda: container.calculate(),
		).grid(column=2, row=4, sticky="nswe", **options)


		container.bind("c", lambda e: container.erase())
		container.bind("<BackSpace>", lambda e: container.backspace())

		container.bind("0", lambda e: container.set_expr("0"))

		container.bind("1", lambda e: container.set_expr("1"))
		container.bind("2", lambda e: container.set_expr("2"))
		container.bind("3", lambda e: container.set_expr("3"))

		container.bind("4", lambda e: container.set_expr("4"))
		container.bind("5", lambda e: container.set_expr("5"))
		container.bind("6", lambda e: container.set_expr("6"))

		container.bind("7", lambda e: container.set_expr("7"))
		container.bind("8", lambda e: container.set_expr("8"))
		container.bind("9", lambda e: container.set_expr("9"))

		container.bind("+", lambda e: container.set_operator("+"))
		container.bind("-", lambda e: container.set_operator("-"))
		container.bind("*", lambda e: container.set_operator("*"))
		container.bind("/", lambda e: container.set_operator("/"))

		container.bind("=", lambda e: container.calculate())
		container.bind("<Return>", lambda e: container.calculate())


		self.pack(expand=True, fill="both")


if __name__ == '__main__':
	app = App("Calculator")