#!/usr/bin/python3
import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.title("Distance Converter")

# 5. take a stringVar which can store meter input value 
meters_value = tk.StringVar()

# 6 . Calculate Function value 
def calculate_feet (*args):
    try : 
        meters = float(meters_value.get())
        feet = meters * 3.28084
        #print(feet)
        print (meters, "meters is equal to", feet)
    except ValueError : 
        pass


# 1. We will start with a frame to put the component in it. 
main = ttk.Frame(root, padding = (30,15))
main.grid() # by default main is going to place in column 0 and row 0

# 2. After creating a frame, put widget into it

meters_label = ttk.Label(main, text = "Meters : ")
meters_input = ttk.Entry(main, width = 10, textvariable = meters_value)
feet_label   = ttk.Label(main, text = "Label : ") 
feet_display = ttk.Label(main, text = "Feet shown here")
calc_button  = ttk.Button(main, text = "Calculate", command = calculate_feet)  # NOTE : do not call calculate_feet() just call calculate_feet

# 3. Place all the into the main Frame using grid 
meters_label.grid(column = 0, row = 0, sticky = "W" , padx = 5, pady = 5)
meters_input.grid(column = 1, row = 0, sticky = "EW", padx = 5, pady = 5)
meters_input.focus()

feet_label.grid(column = 0, row = 1, sticky = "W", padx = 5, pady = 5) 
feet_display.grid(column = 1, row = 1, sticky = "EW", padx = 5, pady = 5) 

calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")

# 3. If we expand the code till now, we did main Frame did not expands as it takes enough space what is required to place widget not more than that 
root.columnconfigure(0, weight = 1) ## this tells when expnad the column 0 of "root" must takes 100% of expands in the middle 



root.mainloop()

