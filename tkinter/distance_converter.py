#!/usr/bin/python3
import tkinter as tk 
import tkinter.font as font
from tkinter import ttk 

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size = 15)  # But this does not set for entry widget

# 5. take a stringVar which can store meter input value 
meters_value = tk.StringVar()

# 7. take a stringVar which store feet output value 
# 8. We can initialize a value here also to display in feet_display widget
feet_value = tk.StringVar(value = "Feet shown here")

# 6 . Calculate Function value 
def calculate_feet (*args):
    try : 
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(feet) 
        #print(feet)
        #print (meters, "meters is equal to", feet)
    except ValueError : 
        pass


# 1. We will start with a frame to put the component in it. 
main = ttk.Frame(root, padding = (30,15))
main.grid() # by default main is going to place in column 0 and row 0

# 2. After creating a frame, put widget into it

meters_label = ttk.Label(main, text = "Meters : ")
meters_input = ttk.Entry(main, width = 10, textvariable = meters_value, font = ("Courier", 15))
feet_label   = ttk.Label(main, text = "Label : ") 
feet_display = ttk.Label(main, textvariable = feet_value) # NOTE : when we use textvariable it will overwrite text field 
calc_button  = ttk.Button(main, text = "Calculate", command = calculate_feet)  # NOTE : do not call calculate_feet() just call calculate_feet

# 3. Place all the into the main Frame using grid 
meters_label.grid(column = 0, row = 0, sticky = "W" , padx = 15, pady = 15)
meters_input.grid(column = 1, row = 0, sticky = "EW", padx = 15, pady = 15)
meters_input.focus()

feet_label.grid(column = 0, row = 1, sticky = "W", padx = 15, pady = 15) 
feet_display.grid(column = 1, row = 1, sticky = "EW", padx = 15, pady = 15) 

calc_button.grid (column = 0, row = 2, columnspan = 2, sticky = "EW")

# 3. If we expand the code till now, we did main Frame did not expands as it takes enough space what is required to place widget not more than that 
root.columnconfigure(0, weight = 1) ## this tells when expnad the column 0 of "root" must takes 100% of expands in the middle 

# 9 . Binding the shortcut keys on keyboard such as "Enter"
root.bind("<Return>", calculate_feet)   ## Middle enter
root.bind("<KP_Enter>", calculate_feet) ## Num pad enter


root.mainloop()

