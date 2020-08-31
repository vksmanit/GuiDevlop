#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("widget example")

initial_value = tk.IntVar(value = 20) 

spin_box = tk.Spinbox (
        root, 
        values = (0, 5, 10, 15, 20, 25, 30),
       #  from_ = 0, 
       #  to = 30, 
        textvariable = initial_value, 
        wrap = False
        )

spin_box.pack()

print (spin_box.get())

root.mainloop()


