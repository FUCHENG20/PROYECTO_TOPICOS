import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']  # options
cb1 = ttk.Combobox(my_w, values=months, width=7)  # Combobox
cb1.grid(row=1, column=1, padx=10, pady=20)  # adding to grid

cb1.set('Apr')  # default selected option
my_w.mainloop()  # Keep the window open
