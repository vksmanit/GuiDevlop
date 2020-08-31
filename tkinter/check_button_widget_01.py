#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text widget example")

# root.grid_columnconfigure(0, weight = 1)
# root.grid_rowconfigure(0, weight = 1)

# check button widget 
check_button = ttk.Checkbutton(root, text = "check me! ")
check_button.pack ()

root.mainloop()


