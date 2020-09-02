#!/usr/bin/python3
import tkinter as tk 
import tkinter.font as font
from tkinter import ttk 


class Distance_converter(tk.Tk):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.title ("Distance Converter")
        self.columnconfigure(0, weight = 1) 
        ## Switching between frame 
        self.frames = dict()

        ## Adding an innner frame for better control of space 
        container = ttk.Frame (self)
        container.grid(padx = 60, pady = 30, sticky = "EW")

        #frame = Meter_to_feet_calc(container)
        feet_to_meters = Feet_to_meters_calc(container, self) ## why self ?
        feet_to_meters.grid(row = 0, column = 0, sticky = "NSEW")

        meters_to_feet = Meter_to_feet_calc(container, self)  ## why self ?
        meters_to_feet.grid(row = 0, column = 0, sticky = "NSEW")
        
      #  self.frames[FeetToMeters] = feet_to_meters ## keys -- value binding
      #  self.frames[MetersToFeet] = meters_to_feet
        self.frames[Feet_to_meters_calc] = feet_to_meters ## keys -- value binding
        self.frames[Meter_to_feet_calc] = meters_to_feet
        
        #self.show_frame(Feet_to_meters_calc)
        #frame.tkraise()
#       self.bind("<Return>", frame.calculate)   
#       self.bind("<KP_Enter>", frame.calculate) 

    def show_frame (self, container) : 
        frame = self.frames[container]
        frame.tkraise()

    

class Meter_to_feet_calc (ttk.Frame): 
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.meters_value = tk.StringVar()
        self.feet_value   = tk.StringVar(value = "Feet shown here") 
        

        self.meters_label = ttk.Label(self, text = "Meters : ")
        self.meters_input = ttk.Entry(self, width = 10, textvariable = self.meters_value, font = ("", 15))
        self.feet_label   = ttk.Label(self, text = "Feet : ") 
        self.feet_display = ttk.Label(self, textvariable = self.feet_value) 
        self.calc_button  = ttk.Button(self, text = "Calculate", command = self.calculate)  
        switch_page_button = ttk.Button(self, 
                text = "Switch to Feet to Meters calulation", 
                command = lambda: controller.show_frame(Feet_to_meters_calc)
                )

        self.meters_label.grid(column = 0, row = 0, sticky = "W") 
        self.meters_input.grid(column = 1, row = 0, sticky = "EW")
        self.meters_input.focus()
        self.feet_label.grid(column = 0, row = 1, sticky = "W")
        self.feet_display.grid(column = 1, row = 1, sticky = "EW")
        self.calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")
        switch_page_button.grid(column = 0, row = 3, columnspan = 3, sticky = "EW")


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
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.meters_value = tk.StringVar(value = "Meters shown here")
        self.feet_value   = tk.StringVar() 
        

        self.feet_label = ttk.Label(self, text = "Feet : ")
        self.feet_input = ttk.Entry(self, width = 10, textvariable = self.feet_value, font = ("", 15))
        self.meters_label   = ttk.Label(self, text = "Meter : ") 
        self.meters_display = ttk.Label(self, textvariable = self.meters_value) 
        self.calc_button  = ttk.Button(self, text = "Calculate", command = self.calculate)  
        switch_page_button = ttk.Button(self, 
                text = "Switch to Meters to Feet  calulation", 
                command = lambda: controller.show_frame(Meter_to_feet_calc)
                )

        self.feet_label.grid(column = 0, row = 0, sticky = "W") 
        self.feet_input.grid(column = 1, row = 0, sticky = "EW")
        self.feet_input.focus()
        self.meters_label.grid(column = 0, row = 1, sticky = "W")
        self.meters_display.grid(column = 1, row = 1, sticky = "EW")
        self.calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")
        switch_page_button.grid(column = 0, row = 3, columnspan = 3, sticky = "EW")


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


