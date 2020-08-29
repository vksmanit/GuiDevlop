#!/usr/bin/python3
import tkinter as tk

root = tk.Tk()
root.geometry ("600x400")
# How to pack word (below) in 600x400 window 
rectangle_1 = tk.Label(root, text= "Rectangle 1", bg = "green", fg = "white")
rectangle_1.pack(ipadx=10, ipady=10, fill="both", side="left", expand = True) 
# NOTE : default side="top" hence rectangle_1 is in top
# also rectangle_1 has entire width of the label <x patti pura isi ka hoga>
# fill ==> means fill 
# expand ==> means expand (upto the limit possible)
# side value 
# side = "top"/"bottom" -- widget take up all the horizontal space  and similarly for "right"/"left"


rectangle_2 = tk.Label(root, text= "Rectangle 2", bg = "red", fg = "white")
rectangle_2.pack(ipadx=10, ipady=10, fill="both", expand = True)
root.mainloop()
