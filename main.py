import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="black")
        self.current_frame = None
        self.data = {}  # Shared data between phases

        # Start with the upload phase
        self.switch_frame("upload.UploadPhase")
    
    def switch_frame(self, module_class_path):
        """Destroy current frame and load the new one."""
        if self.current_frame:
            self.current_frame.pack_forget()
            self.current_frame.destroy()

        module_name, class_name = module_class_path.rsplit(".", 1)
        module = __import__(module_name, fromlist=[class_name])
        phase_class = getattr(module, class_name)
        
        self.current_frame = phase_class(self)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()

