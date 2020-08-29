#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk

### MAIN WINDOW 
root = tk.Tk()

## Label 
# Syntax : ttk.Label (parent, "String", padding=(xpad,ypad)).pack()
# .pack() <-- put into parent window
ttk.Label(root, text="Hello World!", padding=(30,40)).pack()
root.mainloop()
