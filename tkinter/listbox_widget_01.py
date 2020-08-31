#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("widget example")

prog_langs = ("c", "c++", "java", "python", "perl")

# list box widget

langs = tk.StringVar(value = prog_langs)
langs_select = tk.Listbox(root, listvariable = langs, height = 5, selectmode = "extended")  # extended for multiple selection
#langs_select["selectmode"] = "extended"
langs_select.pack()

def handle_sel_change(event): 
  selected_indices = langs_select.curselection()
  for i in selected_indices : 
    print (langs_select.get(i))

langs_select.bind("<<ListboxSelect>>", handle_sel_change)




root.mainloop()

