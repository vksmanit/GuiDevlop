import tkinter as tk 
from tkinter import ttk 

class Setting(ttk.Frame):
    def __init__(self, parent, controller, show_timer, *args, **kwargs):
        super().__init__(parent)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)

        setting_container = ttk.Frame(
                self, 
                padding = "30 15 30 15",
                )

        setting_container.grid(row = 0, column = 0, sticky = "EW", padx = 10, pady = 10)

        setting_container.columnconfigure(0, weight = 1)
        setting_container.rowconfigure(1, weight = 1)

        ## Pomodoro Timer setting  
        pomodoro_label = ttk.Label(setting_container, text = "Promodoro :")
        pomodoro_label.grid(column = 0, row = 0, sticky = "W")
        pomodoro_input = tk.Spinbox(setting_container, from_ = 0, to = 120, increment = 1, justify = "center", textvariable = controller.pomodoro, width = 10)
        pomodoro_input.grid(row = 0, column = 1, sticky = "EW")
        pomodoro_input.focus()
        
        ## Long break 
        long_break_label = ttk.Label (setting_container, text = "Long Break time :")
        long_break_label.grid (row = 1, column = 0, sticky = "W")
        long_break_input = tk.Spinbox(setting_container, from_ = 0, to = 60, increment = 1, justify = "center", textvariable = controller.long_break, width = 10)
        long_break_input.grid(row = 1, column = 1, sticky = "EW")

        ## Short break 
        short_break_label = ttk.Label (setting_container, text = "Long Break time :")
        short_break_label.grid (row = 2, column = 0, sticky = "W")
        short_break_input = tk.Spinbox(setting_container, from_ = 0, to = 30, increment = 1, justify = "center", textvariable = controller.short_break, width = 10)
        short_break_input.grid(row = 2, column = 1, sticky = "EW")


        ## adding some padding 
        for child in setting_container.winfo_children():
            child.grid_configure(padx = 5, pady = 5)
        
        button_cotainer = ttk.Frame(self)
        button_cotainer.grid(sticky = "EW", padx = 10)
        button_cotainer.columnconfigure(0, weight = 1)

        timer_button = ttk.Button(button_cotainer, text = "<- Back", command = show_timer, cursor = "hand2")
        timer_button.grid(row = 0, column = 0, sticky = "EW", padx = 2)
