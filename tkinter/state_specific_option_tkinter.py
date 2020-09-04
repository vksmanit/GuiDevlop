#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

### NOTE : we just want to change property when button is in "pressed state"  --- then we can't use configure we have to use map
## Some theme --has some limitation
#style.configure("CustomButton.TButton")A
style.map (
        "CustomButton.TButton", 
        foreground = [("pressed", "red"), ("active", "white")],
        background = [("pressed", "!disabled", "black"), ("active", "black")]
        )

name = ttk.Label(root, text = "Hello, World!")
entry = ttk.Entry(root, width = 15)
button = ttk.Button(root, text = "Press Here", style = "CustomButton.TButton")

name.pack()
entry.pack()
button.pack()

root.mainloop()
