#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

## changing all of the font in application  -- excet Entry 
# import tkinter.font as font 
# font.nametofont("TkDefaultFont").configure(size=15)
# font.nametofont("TkTextFont").configure(size = 15)
# tkmenufont and tkicon font etc are available here 

name = ttk.Label(root, text = "Hello, World!")
entry = ttk.Entry(root, width = 15) #, font = ("TkDefaultFont", 15))
button = ttk.Button(root, text = "Press Here", style = "CustomButton.TButton")

name.pack()
entry.pack()
button.pack()

root.mainloop()
