#!/usr/bin/python3
import tkinter as tk 
import tkinter.font as font
from tkinter import ttk 


class Distance_converter(tk.Tk):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.title ("Distance Converter")
        self.columnconfigure(0, weight = 1) 

        ## Adding an innner frame for better control of space 
        container = ttk.Frame (self)
        container.grid(padx = 60, pady = 30, sticky = "EW")

        #frame = Meter_to_feet_calc(container)
        frame = Feet_to_meters_calc(container)
        frame.grid(row = 0, column = 0, sticky = "NSEW")


        self.bind("<Return>", frame.calculate)   
        self.bind("<KP_Enter>", frame.calculate) 

    

class Meter_to_feet_calc (ttk.Frame): 
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.meters_value = tk.StringVar()
        self.feet_value   = tk.StringVar(value = "Feet shown here") 
        

        self.meters_label = ttk.Label(self, text = "Meters : ")
        self.meters_input = ttk.Entry(self, width = 10, textvariable = self.meters_value, font = ("", 15))
        self.feet_label   = ttk.Label(self, text = "Label : ") 
        self.feet_display = ttk.Label(self, textvariable = self.feet_value) 
        self.calc_button  = ttk.Button(self, text = "Calculate", command = self.calculate)  

        self.meters_label.grid(column = 0, row = 0, sticky = "W") 
        self.meters_input.grid(column = 1, row = 0, sticky = "EW")
        self.meters_input.focus()
        self.feet_label.grid(column = 0, row = 1, sticky = "W")
        self.feet_display.grid(column = 1, row = 1, sticky = "EW")
        self.calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")


        for child in self.winfo_children(): 
            child.grid_configure(padx = 15, pady = 15)

    def calculate(self, *args, **kwargs): 
        try : 
            meters = float(self.meters_value.get())
            feet  = meters * 3.28084
            self.feet_value.set(feet)
        except ValueError : 
            pass 



class Feet_to_meters_calc (ttk.Frame): 
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.meters_value = tk.StringVar(value = "Meters shown here")
        self.feet_value   = tk.StringVar() 
        

        self.feet_label = ttk.Label(self, text = "Meters : ")
        self.feet_input = ttk.Entry(self, width = 10, textvariable = self.feet_value, font = ("", 15))
        self.meters_label   = ttk.Label(self, text = "Label : ") 
        self.meters_display = ttk.Label(self, textvariable = self.meters_value) 
        self.calc_button  = ttk.Button(self, text = "Calculate", command = self.calculate)  

        self.feet_label.grid(column = 0, row = 0, sticky = "W") 
        self.feet_input.grid(column = 1, row = 0, sticky = "EW")
        self.feet_input.focus()
        self.meters_label.grid(column = 0, row = 1, sticky = "W")
        self.meters_display.grid(column = 1, row = 1, sticky = "EW")
        self.calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")


        for child in self.winfo_children(): 
            child.grid_configure(padx = 15, pady = 15)

    def calculate(self, *args, **kwargs): 
        try : 
            feet  = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(meters)
        except ValueError : 
            pass 





# 10. Change the font of root window 
#font.nametofont("TkDefaultFont").configure(size = 15)  # But this does not set for entry widget


root = Distance_converter()

root.mainloop()


