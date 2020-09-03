#! /usr/bin/python3
import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)


name = ttk.Label(root, text = "Hello, World")
name.pack()

# 1. Get style of TLabel (default style of label widget) first -- what structure it is using 
# 
# [('Label.border', {'sticky': 'nswe', 'border': '1', 'children': [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': [('Label.label'
# , {'sticky': 'nswe'})]})]})]
# 
#  border -- padding -- label 
#
print (style.layout("TLabel"))


# these lines will print available options 
print (style.element_options("Label.border"))
print (style.element_options("Label.padding"))
print (style.element_options("Label.label"))

# these lines will print what is current font is
print (style.lookup("TLabel", "font"))
print (style.lookup("TLabel", "foreground"))
print (style.lookup("TLabel", "compound"))


#####################################################33
# change the theme 
style.theme_use("clam")

# these lines will print available options 
print (style.element_options("Label.border"))
print (style.element_options("Label.padding"))
print (style.element_options("Label.label"))

# these lines will print what is current font is
print (style.lookup("TLabel", "font"))
print (style.lookup("TLabel", "foreground"))
print (style.lookup("TLabel", "compound"))

## this show that we are having more configurable parameter for clam theme

## giving bordercolor and borderwidth -- NOTE - we need to configure relief 
style.configure("TLabel", bordercolor = "#f00")
style.configure("TLabel", borderwidth = 20)
style.configure("TLabel", relief = "solid")



root.mainloop()
