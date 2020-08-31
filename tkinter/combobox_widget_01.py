#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("widget example")

# combo box widget 
selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable = selected_weekday)
weekday["values"] = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
weekday["state"] = "readonly" #"normal" # "readonly"
weekday.pack()

def handle_sel(event):
    print ("Today is", selected_weekday.get())
    print ("But we are going to change it to Friday")
    selected_weekday.set("Fri")
    print (weekday.current()) # get # set # current -- are other method


weekday.bind("<<ComboboxSelected>>", handle_sel) ## bind handle_sel with weekday combobox 

root.mainloop()

print (selected_weekday.get(), "was selected")


