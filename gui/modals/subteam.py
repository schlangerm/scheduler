import tkinter as tk
from tkinter import ttk
from gui.modals.base import CreationModal

class SubTeamModal(CreationModal):
    def __init__(self, parent, stage):
        super().__init__(parent, stage)

        self.entries = []
        self.subteam_name_list = []
        
        self.label_slot = tk.Frame(self)
        self.label_slot.pack()
        tk.Label(self.label_slot, text="Enter sub team names").pack()
        
        self.entry_frame = tk.Frame(self)
        self.entry_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.add_entry()

        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack(pady=10)
        tk.Button(self.btn_frame, text="Add Another Sub Team", command=self.add_entry).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Submit", command=self.submit).pack(side=tk.RIGHT, padx=5)
    
    def add_entry(self):
        row = len(self.entries)
        entry = tk.Entry(self.entry_frame, width=40)
        entry.grid(row=row, column=0, pady=2, sticky="w")
        self.entries.append(entry)
        self.update_idletasks()
        self.geometry("")
    
    def submit(self):
        self.subteam_name_list = [entry.get().strip() for entry in self.entries if entry.get().strip()]
        self.destroy()