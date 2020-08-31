#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)


curr_val = tk.DoubleVar()

def handle_sel_change(event): 
    print (scale.get())


# scale 
scale = ttk.Scale(
        root,
        orient = "horizontal",
        from_ = 0,
        to = 10,
        command = handle_sel_change)

#scale["state"] = "disable" #"normal"

scale.pack(fill="x")



root.mainloop()


print (curr_val.get())
