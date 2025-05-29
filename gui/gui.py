import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from gui.basewindow import Base_Window 



'''
Intro Window
'''
class Intro_Window(tk.Tk):
    def __init__(self):
        super().__init__()

        #INTRO CONFIG
        self.title("Scheduler 0.0.1")
        self.geometry("400x100")

        #CREATE TEAM BUTTON
        self.create_team_button = tk.Button(self, text = 'Create Team', width = 50, command = self.create_team)
        self.create_team_button.grid(row=1)

        #LOAD TEAM BUTTON
        self.load_team_button = tk.Button(self, text = 'Load Team', width = 50, command = self.load_team)

        #ABOUT BUTTON
        aboutbutton = tk.Button(self, text = 'About...', width = 50, command = self.about_app)
        aboutbutton.grid(row=3)

        #CLOSE BUTTON 
        closebutton = tk.Button(self, text = 'Close', width = 50, command = self.destroy)
        closebutton.grid(row=4)
        

    def create_team(self):
        create_team_window = Create_Team_Window()
        self.destroy()
        create_team_window.mainloop()
        

    def load_team(self):
        team_filename = askopenfilename() 
        # TODO: DO SOMETHING WITH THIS FILE TO CREATE THE MEMBERS INFO THAT MAIN WINDOW NEEDS
        main_window = Main_Window(team_info)
        self.destroy()
        main_window.mainloop()
        

    def about_app(self): 
        messagebox.showinfo('About...', "An application to create a schedule by Matthew Schlanger")



'''
Main Window
'''
class Main_Window(Base_Window):
    def __init__(self, team_info):
        super().__init__()


        

'''
Create Team Window
'''
class Create_Team_Window(Base_Window):
    def __init__(self):
        super().__init__()

        self.after(100, self.start_modals)

        # TODO  grab the parameters - shifts, subteams, days of the week operating, min coverage
    
    def start_modals(self): # BUG: There's another window that sometimes pops up after each of these but I have no idea why
        # Grab team name
        self.user_prompt_update_team_name()
        
        # Grab sub teams
        self.user_prompt_update_subteam_name()
        
        # Grab shifts
        self.user_prompt_update_shift()

        # Grab operating days
        self.user_prompt_update_operating_days()

        #TODO: Grab min coverage
