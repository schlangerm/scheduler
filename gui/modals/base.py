from tkinter import Toplevel

class CreationModal(Toplevel):
    def __init__(self, parent, stage):
        super().__init__(parent)
        self.title(f'Create {stage}')
        self.transient(parent)      
        self.grab_set()

        # supposed to wait until the sub-class fills it with widgets
        self.after(0, self.center_window)

    # All modals should be center-screen and auto-fit to widgets
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")