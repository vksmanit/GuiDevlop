#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text widget example")

text = tk.Text(root, height=8)
text.pack()

text.insert("1.0","Please Enter Your Name : ") ## "1.0" means -- line 1 char 0 
text["state"] = "normal" #"disable"

text_content = text.get("1.0", "end")
print (text_content)

root.mainloop()
