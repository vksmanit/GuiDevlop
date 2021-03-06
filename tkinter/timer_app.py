#! /usr/bin/python3 
import tkinter as tk 
from tkinter import ttk 
from collections import deque

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

class Timer(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.controller = controller
        pomodoro_time = int (controller.pomodoro.get())
        self.current_time = tk.StringVar(value = "%02d:00" % pomodoro_time)

        self.current_timer_label = tk.StringVar(value = controller.timer_schedule[0])
        timer_description = ttk.Label(self,  textvariable = self.current_timer_label)
        timer_description.grid(row = 0, column = 0, sticky = "W", padx = (10, 0), pady = (10, 0))
        self.timer_running = False 
        self._timer_decrement_job = None ## variable starting with _ --- is a private variable : NoBody outside the class can access it

        timer_frame = ttk.Frame (self, height = "100")
        timer_frame.grid(row = 1, column = 0, pady = (10,0), sticky = "NESW")
        timer_counter = ttk.Label (timer_frame, 
                textvariable = self.current_time
                )
        # to place center position absolute and relative 
        timer_counter.place (relx = 0.5, rely = 0.5, anchor = "center")
        # timer_counter.grid()
        #
        button_container = ttk.Frame(self, padding = 10)
        button_container.grid(row = 2, column = 0, sticky = "EW")
        button_container.columnconfigure((0, 1 ,2), weight = 1)

        self.start_button = ttk.Button(button_container, text = "Start", command = self.start_timer, cursor = "hand2")
        self.stop_button = ttk.Button(button_container, text = "Stop", command = self.stop_timer, state = "disable", cursor = "hand2")
        self.start_button.grid(row = 0, column = 0, sticky = "EW")
        self.stop_button.grid(row = 0, column = 1, sticky = "EW", padx = 5)
        self.reset_button = ttk.Button(button_container, text = "Reset", command = self.reset_timer, cursor = "hand1")
        self.reset_button.grid(row = 0, column = 2 , sticky = "EW")
        #self.decrement_timer()

    def start_timer(self):
        self.timer_running = True 
        self.start_button["state"] = "disable"
        self.stop_button["state"] = "enable"
        self.decrement_timer()
    
    def stop_timer (self):
        self.timer_running = False 
        self.start_button["state"] = "enable"
        self.stop_button["state"] = "disable"
        if self._timer_decrement_job : 
            self.after_cancel (self._timer_decrement_job)
            self._timer_decrement_job = None

    def reset_timer (self):
        self.stop_timer()
        pomodoro_time = int (self.controller.pomodoro.get())
        self.current_time.set("%02d:00" % pomodoro_time)
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_timer_label.set(self.controller.timer_schedule[0])


    def decrement_timer(self):
        current_time = self.current_time.get()

        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")
            if int(seconds)> 0: 
                seconds = int(seconds)-1
                minutes = int(minutes)
            else : 
                seconds = 59
                minutes = int(minutes) - 1
            self.current_time.set("%02d:%02d" % (minutes,seconds))
            self._timer_decrement_job = self.after(1000, self.decrement_timer)  ## () -- return value 
        elif self.timer_running and current_time == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]
            self.current_timer_label.set(next_up)
            
            if next_up == "Pomodoro":
                pomodoro_time = int(self.controller.pomodoro.get())
                self.current_time.set("%02d:00" % pomodoro_time)
            elif next_up == "Short Break":
                short_break_time = int(self.controller.short_break.get())
                self.current_time.set("%02d:00" % short_break_time)
            elif next_up == "Long Break":
                long_break_time = int(self.controller.long_break.get())
                self.current_time.set("%02d:00" % long_break_time)

            self._timer_decrement_job = self.after(1000, self.decrement_timer)  ## () -- return value 


app = PromodoroTimer()
app.mainloop()


