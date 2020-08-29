#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk

def greet():
  print ("Hello Vipin")

root = tk.Tk()
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left",fill="y", expand = True)
#greet_button.pack(side="left")
# side --- left ---> reserved vertical strip 
# side --- top ----> reserved horizontal strip
# expand = true ---> will expand widget as we increase window propotionaly 
# fill = "both","x", "y" --> will fill the widget space

quit_button = ttk.Button(root, text="quit", command = root.destroy)
quit_button.pack(side="left")


root.mainloop()


