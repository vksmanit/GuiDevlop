#! /usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 
from collections import deque
from frames import Timer

class PromodoroTimer (tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title ("Promodoro Timer")
        self.columnconfigure (0, weight = 1)
        self.rowconfigure (1, weight = 1)

        ## variable inserted to control from setting
        self.pomodoro = tk.StringVar (value = 25)
        self.long_break = tk.StringVar (value = 15)
        self.short_break = tk.StringVar (value = 5)

        #############################################
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight = 1)

        
        timer_frame = Timer(container, self)
        timer_frame.grid(row = 0, column = 0, sticky = "NESW")

app = PromodoroTimer()
app.mainloop()

