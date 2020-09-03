#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk

def greet(): 
    print("Hello, ", user_name.get())


## Default theme is - default

root = tk.Tk()
user_name = tk.StringVar()

# for theme
style = ttk.Style(root)
style.theme_use("classic")

## Themes are much more than colors and all
# they interact with the widget differently -- hence we should always keep an eyes on themes


# to know available themes in your computer
#print (style.theme_names())

# for current theme 
#print (style.theme_use('calm'))

input_frame1 = ttk.Frame(root, padding =(20, 10, 20, 0)) ## padding values are - (left, top , right, bottom)
input_frame1.pack(fill="both")


name_label = ttk.Label(input_frame1, text="Name :")
name_label.pack(side="left", padx=(0,10))

name_entry = ttk.Entry(input_frame1, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

button_frame1 = ttk.Frame(root, padding = (20,10))
button_frame1.pack(fill="both")

greet_button = ttk.Button(button_frame1, text="Greet", command=greet)
greet_button.pack(side="left", fill = "x", expand = True)

quit_button = ttk.Button(button_frame1, text="quit", command = root.destroy)
quit_button.pack(side="left", fill = "x", expand = True )

root.mainloop()

