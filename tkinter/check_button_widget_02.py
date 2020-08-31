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
selcted_options = tk.StringVar()

def print_current_option(): 
  print (selcted_options.get())


check = ttk.Checkbutton (
      root, 
      text = "Check example", 
      variable = selcted_options,
      command = print_current_option,
      onvalue = "on", 
      offvalue = "off"
      )
check.pack()

# NOTE : textvariable -- will change the label as well 
#        variable -- will just hold the onvalue and offvalue depends on checked/unchecked staus 


root.mainloop()



