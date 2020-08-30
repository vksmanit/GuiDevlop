#!/usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 

# For Images 
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Example")





label = ttk.Label(root, text = "Hello, World", padding = 20)
label.config(font=("Courier",20))
label.pack()


image = Image.open("logo.png").resize((64,64))
photo = ImageTk.PhotoImage(image)
#label = ttk.Label(root, image = photo, padding = 5)
#label = ttk.Label(root,text = "xyz", image = photo, padding = 5)  # text won't appears 
label = ttk.Label(root,text = "xyz", image = photo, padding = 5, compound = "right")  # other option of compund are left/top/bottom -- will show both text as well as image
label.pack()


root.mainloop()
