import tkinter as tk
from gui.modals.base import CreationModal

class TeamNameModal(CreationModal):
    def __init__(self, parent, stage):
        super().__init__(parent, stage)
        self.user_input = None

        tk.Label(self, text="What is the name of your team?").grid(row=1)

        self.entry = tk.Entry(self, width=80)
        self.entry.grid(row=2, padx=10)

        tk.Button(self, text="Submit", command=self.submit).grid(row=3)

    def submit(self):
        self.user_input = self.entry.get().strip()
        self.destroy()
        




