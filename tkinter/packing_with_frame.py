#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

# example1 : tk.Label(root, text = "Lebel top", bg = "red").pack(side = "top", expand = True, fill = "both")
# example1 : tk.Label(root, text = "Lebel top", bg = "red").pack(side = "top", expand = True, fill = "both")
# example1 : tk.Label(root, text = "Lebel left", bg = "green").pack(side = "left", expand = True, fill = "both")

main = ttk.Frame(root) # Frame is also a container`
main.pack(side="left", fill = "both", expand = True);
tk.Label(main, text = "Lebel top", bg = "red").pack(side = "top", expand = True, fill = "both")
tk.Label(main, text = "Lebel top", bg = "red").pack(side = "top", expand = True, fill = "both")
tk.Label(root, text = "Lebel left", bg = "green").pack(side = "left", expand = True, fill = "both")

root.mainloop()

