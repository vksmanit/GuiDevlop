#! /usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 
from collections import deque
from frames import Timer, Setting


####################### COLORS ######################
COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"

class PromodoroTimer (tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ############# styles ###############3
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Timer.TFrame", background = COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background = COLOUR_PRIMARY)
        style.configure("TimerText.TLabel", background = COLOUR_LIGHT_BACKGROUND, foreground = COLOUR_DARK_TEXT, font = "Courier 38")
        style.configure("LightText.TLabel", background = COLOUR_PRIMARY, foreground = COLOUR_LIGHT_TEXT)#, font = "Courier 38")
        style.configure("PomodoroButton.TButton", background = COLOUR_SECONDARY, foreground = COLOUR_LIGHT_TEXT)
        style.map("PomodoroButton.TButton", background = [("active", COLOUR_PRIMARY), ("disabled", COLOUR_SECONDARY)])
        self["background"] = COLOUR_PRIMARY
        ############# styles ###############3

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

