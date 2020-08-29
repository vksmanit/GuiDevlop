#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk

def greet(): 
    name = user_name.get()
    #print(f"Hello, {user_name.get()} ");
    print(name)

root = tk.Tk()
user_name = tk.StringVar()

input_frame1 = ttk.Frame(root, padding =(20, 10, 20, 0)) ## padding values are - (left, top , right, bottom)
input_frame1.pack(fill="both")


name_label = ttk.Label(input_frame1, text="Name :")
name_label.pack(side="left", padx=(0,10))

name_entry = ttk.Entry(input_frame1, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

button_frame1 = ttk.Frame(root, padding = (20,10))
button_frame1.pack(fill="both")

# NOTE : frame does not have 
# 1. side : default top 
# 2. expand : only going to take as much as vertical space they need and they take all of the horizontal space

greet_button = ttk.Button(button_frame1, text="Greet", command=greet)
greet_button.pack(side="left", fill = "x", expand = True)

quit_button = ttk.Button(button_frame1, text="quit", command = root.destroy)
quit_button.pack(side="left", fill = "x", expand = True )

root.mainloop()
