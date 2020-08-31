#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text widget example")


storage_variable = tk.StringVar()


def print_var() : 
    print (storage_variable.get())



option_one = ttk.Radiobutton (
	root, 
	text = "option 1",
	variable = storage_variable, ## NOTE  - same 
	value = "first option",
	command = print_var
)


option_two = ttk.Radiobutton (
	root, 
	text = "option 2",
	variable = storage_variable,  # NOTE - same  
	value = "second option",
	command = print_var
)


option_three = ttk.Radiobutton (
	root, 
	text = "option 3",
	variable = storage_variable,  # NOTE - same 
	value = "third option",
	command = print_var
)
option_one.pack()
option_two.pack()
option_three.pack()


root.mainloop()

