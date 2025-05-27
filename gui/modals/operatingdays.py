import tkinter as tk
from gui.modals.base import CreationModal

class OperatingDaysModal(CreationModal):
    def __init__(self, parent, stage):
        super().__init__(parent, stage)

        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.day_vars = []

        self.label_slot = tk.Frame(self)
        self.label_slot.pack()
        tk.Label(self.label_slot, text="What days of the week is your organization operational?").pack()

        self.option_frame = tk.Frame(self)
        self.option_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        for i, day in enumerate(self.days):
            var = tk.BooleanVar(self, value=False)
            chk = tk.Checkbutton(self.option_frame, text=day, variable=var)
            chk.grid(row=i, column=0, sticky="w", padx=10, pady=2)
            self.day_vars.append(var)

        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack()
        tk.Button(self.btn_frame, text="Submit", command=self.submit).pack()

    def submit(self):
        self.operating_days = [var.get() for var in self.day_vars] # M-F would be like [True, True, True, True, True, False, False]
        self.destroy()
