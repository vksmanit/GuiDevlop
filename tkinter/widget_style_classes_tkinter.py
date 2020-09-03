#! /usr/bin/python3
import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)


name = ttk.Label(root, text = "Hello, World")
entry = ttk.Entry(root, width = 15)
name.pack()

## NOTE :: ttk widget are configurable NOT tk widget

## 1. TO know which style is using name widget -- just enable below code 
#print (name["style"])  ## no print --- default
## 2. to know default style -- TLabel
#print (name.winfo_class() ## Tlabel)


style.configure("TLabel", font = ("Segoe UI", 20)) ## this will change TLabel --- use font specified 



root.mainloop()
