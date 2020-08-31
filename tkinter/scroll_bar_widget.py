#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Scroll bar widget example")
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

text = tk.Text(root, height=8)
text.grid(row = 0, column = 0, sticky = "ew")
#text.pack()

text.insert("1.0","Please Enter Your Name : ") ## "1.0" means -- line 1 char 0 
#text["state"] = "normal" #"disable"
#
#text_content = text.get("1.0", "end")
#print (text_content)

### scroll bar widget 
text_scroll = ttk.Scrollbar(root, orient = "vertical", command = text.yview) # text widget y position 
text_scroll.grid (row = 0, column = 1, sticky = "ns")
text["yscrollcommand"] = text_scroll.set

root.mainloop()
