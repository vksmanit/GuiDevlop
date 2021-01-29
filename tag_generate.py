import tkinter as tk
from tkinter import ttk
import os 


class GuiTagGenerate (tk.Tk): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Generate Tag File")
        self.columnconfigure(0, weight = 1) 

        container = ttk.Frame (self)
        container.grid(padx = 60, pady = 30, sticky = "EW")

        Generate_tag_frame = Generate_tag(container)
        Generate_tag_frame.pack()




class Generate_tag (ttk.Frame): 
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.project = tk.StringVar();
        self.project_var = tk.StringVar();
        self.complete_status = tk.StringVar();
        self.project_root = (os.environ['PWD']); 
        self.complete_indication = 0;
        

        self.btu0_button = ttk.Radiobutton(self, text = "btu0", variable = self.project_var, value = "btu0", command = self.seleceted_test_project)#, command = self.sel_project)#, value = "btu0")
        self.robin4_button = ttk.Radiobutton (self, text = "robin4", variable = self.project_var, value = "robin4", command =  self.seleceted_test_project)#, command = self.sel_project)#, value = 
        self.project_label    = ttk.Label(self, textvariable = self.project_var)
        #self.text_label     = ttk.Label(self, textvariable = self.project_root)
        self.generate_tag_button       = ttk.Button(self, text = "Generate Tags", command = self.generate_tags)
        self.completion_label = ttk.Label(self, textvariable = self.complete_status)

        self.btu0_button.grid(column = 0, row = 0, sticky = "EW")
        self.robin4_button.grid(column = 0, row = 1, sticky = "EW")
        self.project_label.grid(column = 2, row = 1, sticky = "EW")
        self.generate_tag_button.grid(column = 0, row = 2, sticky = "EW")
        self.completion_label.grid(column = 0, row = 3, sticky = "EW")
        #self.text_label.grid(column = 0, row = 3, sticky = "EW")

    def seleceted_test_project(self, *args, **kwargs):
        try :
            if self.project_var.get() == "btu0" : 
                self.test_project = "btu0"
            elif self.project_var.get() == "robin4" : 
                self.test_project = "robin4" 
            # TODO : exit else : 
        except ValueError : 
            pass 


    def generate_tags(self, *args, **kwargs):
        try : 
            if (os.path.exists("./tags")):
                print("Remove existing tag file")
                os.remove("./tags")
            else: 
                print("The ./tags file not found in " + self.project_root)


            # Open a file to write the dir path needed for tag generation 
            f = open("./generate_tag_file.input","w"); 
            f.write (self.project_root + "/uvm/ble3/\n")
            f.write (self.project_root + "/uvm/ahb2/\n")
            f.write (self.project_root + "/ip_core_ahb/btu2/hdl/\n")
            f.write (self.project_root + "/ip_core_ahb/btu2/sim/\n")
            f.write (self.project_root + "/ip_core_ahb/ffu/\n")
            f.write (self.project_root + "/top_" + self.test_project + "/dpi/\n")
            f.write (self.project_root + "/top_" + self.test_project + "/tbvlib/\n")
            f.write (self.project_root + "/top_" + self.test_project + "/uvm/bench/\n")
            f.write (self.project_root + "/top_" + self.test_project + "/sim/\n")
            f.write (self.project_root + "/top_" + self.test_project + "/hdl/\n")


            # Close and remove the file 
            f.close()
            # Run Ctags command to get tag file
            os.system("/usr/bin/ctags -R -L ./generate_tag_file.input")
            os.remove("./generate_tag_file.input")
            self.complete_indication = 1; 
            self.generate_tag_button['state'] = "disable";

            if (self.complete_indication == 1) : 
                self.complete_status.set("Finish Tag Generation, Please close GUI");
                self.generate_tag_button['state'] = "enable"; 
        except ValueError : 
            pass
            #os.system("./generate_tag_files.sh self.project_var")
        except NameError : 
            pass




root = GuiTagGenerate()
root.mainloop()
