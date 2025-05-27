import tkinter as tk
from tkinter import ttk
from gui.modals.base import CreationModal
from tkinter import messagebox

class ShiftModal(CreationModal):
    def __init__(self, parent, stage):
        super().__init__(parent, stage)
        
        self.shifts = []
        self.valid_shifts = []

        self.label_slot = tk.Frame(self)
        self.label_slot.pack()
        tk.Label(self, text="Select shifts").pack()

        self.start_times = ["8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM"]
        self.end_times = ["4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM"]

        self.shift_frame = tk.Frame(self)
        self.shift_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.add_shift_selection()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Another Shift", command=self.add_shift_selection).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Submit", command=self.submit).pack(side=tk.RIGHT, padx=5)
        
    def add_shift_selection(self):
        row = len(self.shifts)

        start_var = tk.StringVar(self, value = "Start Time . . .")
        end_var = tk.StringVar(self, value = "End Time . . .")

        label = tk.Label(self.shift_frame, text=f'Shift {row + 1}')
        label.grid(row=row, column=0, pady=2)

        start_option = ttk.OptionMenu(self.shift_frame, start_var, start_var.get(), *self.start_times)
        start_option.grid(row=row,column=1,pady=2)

        spacer = tk.Label(self.shift_frame, text="-")
        spacer.grid(row=row, column=2, pady= 2)

        end_option = ttk.OptionMenu(self.shift_frame, end_var, end_var.get(), *self.end_times)
        end_option.grid(row=row, column=3, pady=2)

        self.shifts.append((start_var, end_var))
        self.update_idletasks()
        self.geometry("")

    def submit(self):

        for start_var, end_var in self.shifts:
            start = start_var.get()
            end = end_var.get()

            if start in self.start_times and end in self.end_times:
                self.valid_shifts.append(f'{start} - {end}')
        
        if not self.valid_shifts:
            messagebox.showinfo("!!!", "No valid shifts selected")

        self.destroy()
        # get lists from the user - should be like couple of ints representing 24 hr clock times maybe, down to the minute in code but 30 min in selection
        # should default to 9 - 5 :D
        
        