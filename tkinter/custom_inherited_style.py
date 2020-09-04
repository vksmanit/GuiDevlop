#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
style = ttk.Style(root)

## creating our CustomEntryStyle 
style.configure("CustomEntryStyle.TEntry", padding = 20)
# we can have so many styles like -- we can use number of style configuration for number of widgets
style.configure("Emergency.CustomEntryStyle.TEntry", padding = 50)

name = ttk.Label (root, text = "Hello, World!")
entry = ttk.Entry (root, width = 10)
# one way is 
# inherited style 
entry["style"] = "CustomEntryStyle.TEntry"
name.pack()
entry.pack()




entry1 = ttk.Entry (root, width = 10)
entry1.pack()
root.mainloop()

