#! /usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 
from collections import deque
from frames import Timer, Setting

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

        timer_frame = Timer(container, self, lambda: self.show_frame(Setting))
        timer_frame.grid(row = 0, column = 0, sticky = "NESW")

        setting_frame = Setting(container, self, lambda: self.show_frame(Timer))
        setting_frame.grid(row = 0, column = 0, sticky = "NESW")

        ## Switching b/w timer and setting frames 
        self.frames = dict()
        self.frames[Timer] = timer_frame
        self.frames[Setting] = setting_frame

        self.show_frame(Timer)

    def show_frame (self, container):
        frame = self.frames[container]
        frame.tkraise()



app = PromodoroTimer()
app.mainloop()

