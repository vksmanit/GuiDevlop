#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello World")
        UserInputFrame(self).pack()
        
class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text = "Enter your name :")
        entry = ttk.Entry(self, width = 15, textvariable = self.user_input)
        button = ttk.Button(self, text = "Enter", command = self.greet)
         
        label.pack(side = "left")
        entry.pack(side = "left")
        button.pack(side = "left")
    
    def greet(self): 
        print ("Hello", self.user_input.get())


root = HelloWorld()

#label = ttk.Label(frame, text = "Enter your name : ")
#label.pack()

root.mainloop()

