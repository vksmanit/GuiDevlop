#!/usr/bin/python3
import tkinter as tk 
import tkinter.font as font
from tkinter import ttk 


class Distance_converter(tk.Tk):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.title ("Distance Converter")
        self.columnconfigure(0, weight = 1) 

        frame = Meter_to_feet_calc(self, padding = (30, 15))
        frame.grid()
        self.bind("<Return>", frame.calculate_feet)   
        self.bind("<KP_Enter>", frame.calculate_feet) 

    

class Meter_to_feet_calc (ttk.Frame): 
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.meters_value = tk.StringVar()
        self.feet_value   = tk.StringVar(value = "Feet shown here") 
        

        self.meters_label = ttk.Label(self, text = "Meters : ")
        self.meters_input = ttk.Entry(self, width = 10, textvariable = self.meters_value, font = ("", 15))
        self.feet_label   = ttk.Label(self, text = "Label : ") 
        self.feet_display = ttk.Label(self, textvariable = self.feet_value) 
        self.calc_button  = ttk.Button(self, text = "Calculate", command = self.calculate_feet)  

        self.meters_label.grid(column = 0, row = 0, sticky = "W") 
        self.meters_input.grid(column = 1, row = 0, sticky = "EW")
        self.meters_input.focus()
        self.feet_label.grid(column = 0, row = 1, sticky = "W")
        self.feet_display.grid(column = 1, row = 1, sticky = "EW")
        self.calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")


        for child in self.winfo_children(): 
            child.grid_configure(padx = 15, pady = 15)

    def calculate_feet(self, *args, **kwargs): 
        try : 
            meters = float(self.meters_value.get())
            feet  = meters * 3.28084
            self.feet_value.set(feet)
        except ValueError : 
            pass 






# 10. Change the font of root window 
#font.nametofont("TkDefaultFont").configure(size = 15)  # But this does not set for entry widget


root = Distance_converter()

root.mainloop()


