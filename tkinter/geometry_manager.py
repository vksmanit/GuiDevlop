#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

def greet(): 
    name = user_name.get()
    print (name)

root = tk.Tk()
root.title ("Greet")

root.columnconfigure(0,weight=1) # weight : are relative number 
#root.rowconfigure(

user_name = tk.StringVar()

input_frame1 = ttk.Frame(root, padding =(20, 10, 20, 0)) ## padding values are - (left, top , right, bottom)
input_frame1.grid(row = 0, column = 0)


name_label = ttk.Label(input_frame1, text="Name :")
name_label.grid(row = 0, column = 0, padx=(0,10))
# NOTE : when we call grid with no arg the element is going to place in First Row and First column

name_entry = ttk.Entry(input_frame1, width=15, textvariable=user_name)
name_entry.grid(row = 0, column = 1)
name_entry.focus()

button_frame1 = ttk.Frame(root, padding = (20,10))
#button_frame1.grid(row = 1, column = 0)
button_frame1.grid(sticky="EW")
button_frame1.columnconfigure(0, weight=1) # configure column 0 with weight 1 of button_frame1
button_frame1.columnconfigure(1, weight=1)

greet_button = ttk.Button(button_frame1, text="Greet", command=greet)
greet_button.grid(row = 0, column = 0, sticky = "EW")
#greet_button.grid(row = 0, column = 0)
quit_button = ttk.Button(button_frame1, text="quit", command = root.destroy)
quit_button.grid(row = 0, column = 1, sticky = "EW")

root.mainloop()
