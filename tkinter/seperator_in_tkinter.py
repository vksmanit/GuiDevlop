#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text widget example")

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

ttk.Label(root, text = "Hello Vipin", padding = 20 ).pack()

## separator widget 
separator1 = ttk.Separator(root, orient = "horizontal")
separator1.pack(fill = "x")

ttk.Label(root, text = "Hello Rani", padding = 20 ).pack()

root.mainloop()
