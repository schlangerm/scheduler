import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.modals.teamname import TeamNameModal
from gui.modals.subteam import SubTeamModal
from gui.modals.shift import ShiftModal
from gui.modals.operatingdays import OperatingDaysModal
from gui.helpers.treecrud import update_or_insert_tree_row
from gui.helpers.cleaning import format_days

class Base_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #CREATE WINDOW CONFIG
        self.title("Scheduler 0.0.1")
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()-100}+0+0')

        #TOP-LEVEL CONTAINER
        self.table_frame = tk.Frame(self)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        #OVERVIEW
        self.overview_tree = ttk.Treeview(self.table_frame, columns=('Team Name', 'Sub-Teams', 'Shifts', 'Operating Days'), show="headings")
        self.overview_tree.heading("Team Name", text="Team Name")
        self.overview_tree.heading("Sub-Teams", text="Sub-Teams")
        self.overview_tree.heading("Shifts", text="Shifts")
        self.overview_tree.heading("Operating Days", text="Operating Days")
        self.overview_tree.pack(expand=True, fill=tk.BOTH)

        self.overview_row_ids = []

        #SUB-TEAM TREE
        self.subteam_tree = ttk.Treeview(self.table_frame, columns=('Name', 'Member Count', 'Minimum Coverage'), show="headings")
        self.subteam_tree.heading("Name", text="Name")
        self.subteam_tree.heading("Member Count", text="Member Count")
        self.subteam_tree.heading("Minimum Coverage", text="Minimum Coverage")
        self.subteam_tree.pack(expand=True, fill=tk.BOTH)

        self.subteam_row_ids = []

        #DISPLAY OF TEAM MEMBERS
        self.member_tree = ttk.Treeview(self.table_frame, columns=('Name','Team', 'Available for Shifts', 'Required Days Off', 'Preferred Days Off'), show="headings")
        self.member_tree.heading("Name", text="Name")
        self.member_tree.heading("Team", text="Team")
        self.member_tree.heading("Available for Shifts", text="Available for Shifts")
        self.member_tree.heading("Required Days Off", text="Required Days Off")
        self.member_tree.heading("Preferred Days Off", text="Preferred Days Off")
        self.member_tree.pack(expand=True, fill=tk.BOTH)

        self.member_row_ids = []

    def user_prompt_update_team_name(self):
        team_name = None
        while not team_name:
            team_name_modal = TeamNameModal(self, "Team Name")
            self.wait_window(team_name_modal)
            team_name = team_name_modal.user_input.strip()
            if not team_name:
                messagebox.showinfo("!!!", "Please enter your team name, try again")
                continue
            else:
                update_or_insert_tree_row(
                    tree=self.overview_tree,
                    row_list=self.overview_row_ids,
                    value=team_name,
                    row_index=0,
                    col_index=0,
                    insert_values_func=lambda val: (val, '', '', '')
                    )
           
    def user_prompt_update_subteam_name(self):
        subteam_count = -1
        while subteam_count < 0:
            subteam_modal = SubTeamModal(self, "Sub-Teams")
            self.wait_window(subteam_modal)
            subteam_name_list = subteam_modal.subteam_name_list
            subteam_count = len(subteam_name_list)

            if not subteam_name_list:
                messagebox.showinfo("!!!", "No sub-teams entered, no changes made")
                return
            self.subteam_name_list = subteam_name_list
            for i, subteam_name in enumerate(self.subteam_name_list):
                update_or_insert_tree_row(
                    tree=self.overview_tree,
                    row_list=self.overview_row_ids,
                    value=subteam_name,
                    row_index=i,
                    col_index=1,
                    insert_values_func=lambda val: ('', val, '', '')
                )

                update_or_insert_tree_row(
                    tree=self.subteam_tree,
                    row_list=self.subteam_row_ids,
                    value=subteam_name,
                    row_index=i,
                    col_index=0,
                    insert_values_func=lambda val: (val, '', '')
                )
    
    def user_prompt_update_shift(self):
        shift_count = 0
        while shift_count < 1:
            shift_modal = ShiftModal(self, "Shifts")
            self.wait_window(shift_modal)
            shift_list = shift_modal.valid_shifts
            shift_count = len(shift_list)

            if not shift_list:
                messagebox.showinfo("!!!", "No shifts entered, you can't make a schedule without shifts!")
                continue

            self.shift_list = shift_list
            for i, shift in enumerate(self.shift_list):
                update_or_insert_tree_row(
                    tree=self.overview_tree,
                    row_list=self.overview_row_ids,
                    value=shift,
                    row_index=i,
                    col_index=2,
                    insert_values_func=lambda val: ('', '', val, '')
                )
    
    def user_prompt_update_operating_days(self):
        operating_days_count = 0
        while operating_days_count < 1:
            operating_days_modal = OperatingDaysModal(self, "Operating Days")
            self.wait_window(operating_days_modal)
            self.operating_days = operating_days_modal.operating_days
            formatted_operating_days = format_days(self.operating_days)
            operating_days_count = len(self.operating_days)

            if not self.operating_days:
                messagebox.showinfo("!!!", "No operating days entered, try again")
                continue
            else:
                update_or_insert_tree_row(
                    tree=self.overview_tree,
                    row_list=self.overview_row_ids,
                    value=formatted_operating_days,
                    row_index=0,
                    col_index=3,
                    insert_values_func=lambda val: ('', '', '', val)
                )

    #TODO: Next is 
            