import tkinter as tk
import tkinter.ttk as ttk


class MainMenu(tk.Menu):
    def __init__(self, container):
        super().__init__(container)

        self.container = container

        self.hot_keys_menu = tk.Menu(self)
        self.add_cascade(label="Hot Keys", menu=self.hot_keys_menu)

        # or here we can use self.place_window
        self.hot_keys_menu.add_command(label="key bindings", command=self.place_frame)

    def place_frame(self):
        self.information_frame()
        self.menu_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def place_window(self):
        self.new_window = tk.Tk()
        self.new_window.geometry("300x400")
        self.new_window.resizable(0,0)
        
        self.information_frame(self.new_window)
        self.menu_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.top_close_button.pack_forget()

        self.new_window.mainloop()


    def information_frame(self, wrapper=None):
        self.menu_frame = ttk.Frame(wrapper if wrapper is not None else self.container)


        self.top_label = ttk.Frame(self.menu_frame)
        self.top_label_text = ttk.Label(self.top_label,
            text="Key Bindings for this app.")
        self.top_close_button = ttk.Button(self.top_label,
            text="X", command=self.menu_frame.place_forget)
        
        self.top_close_button.pack(side="right")
        self.top_label_text.pack(expand=True, fill="both", side="right")
        self.top_label.pack(fill="x")


        self.main_text = ttk.Frame(self.menu_frame, width=300)
        self.main_text_label = ttk.Label(self.main_text,
            text="You can type numbers from keyboard, by pressing 0-9 buttons. \
            It works for operations either. \
            BackSpace removes 1 symbol from the latest calculation first and \
            then if that value is empty it starts removing the entire \
            expression. When you got caught an expression you can use it to \
            get back to the expression you typed right before it.", wraplength=200)
        
        self.main_text_label.pack(fill="both")
        self.main_text.pack(fill="both", pady=10)


        self.row1 = ttk.Frame(self.menu_frame)
        self.row1_key = ttk.Label(self.row1, text="To exit, press")
        self.row1_val = ttk.Label(self.row1, text="q, or Esc")
        
        self.row1_val.pack(side="right")
        self.row1_key.pack(expand=True, fill="both", side="right")
        self.row1.pack(fill="both")


        self.row2 = ttk.Frame(self.menu_frame)
        self.row2_key = ttk.Label(self.row2, text="Numbers 0-9")
        self.row2_val = ttk.Label(self.row2, text="0-9")
        
        self.row2_val.pack(side="right")
        self.row2_key.pack(expand=True, fill="both", side="right")
        self.row2.pack(fill="both")


        self.row3 = ttk.Frame(self.menu_frame)
        self.row3_key = ttk.Label(self.row3, text="Operations")
        self.row3_val = ttk.Label(self.row3, text="+, -, *, / ; ^ to square the value")
        
        self.row3_val.pack(side="right")
        self.row3_key.pack(expand=True, fill="both", side="right")
        self.row3.pack(fill="both")


        self.row4 = ttk.Frame(self.menu_frame)
        self.row4_key = ttk.Label(self.row4, text="To calculate the expression")
        self.row4_val = ttk.Label(self.row4, text="=, or Enter")
        
        self.row4_val.pack(side="right")
        self.row4_key.pack(expand=True, fill="both", side="right")
        self.row4.pack(fill="both")


        self.row5 = ttk.Frame(self.menu_frame)
        self.row5_key = ttk.Label(self.row5, text="To clear the screen and start from scratch")
        self.row5_val = ttk.Label(self.row5, text="c")
        
        self.row5_val.pack(side="right")
        self.row5_key.pack(expand=True, fill="both", side="right")
        self.row5.pack(fill="both")


        self.row6 = ttk.Frame(self.menu_frame)
        self.row6_key = ttk.Label(self.row6, text="To remove 1 character")
        self.row6_val = ttk.Label(self.row6, text=" <- BackSpace")
        
        self.row6_val.pack(side="right")
        self.row6_key.pack(expand=True, fill="both", side="right")
        self.row6.pack(fill="both")