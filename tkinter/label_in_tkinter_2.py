#!/usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Example")

greeting = tk.StringVar()

label = ttk.Label(root, textvariable = greeting ,padding = 20)
#label.config(font=("Courier",20))
label.pack()


greeting.set("Hello, Vipin")

root.mainloop()
