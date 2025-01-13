import tkinter as tk
from PIL import Image, ImageTk

class PrintPhase(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        solved_image_path = self.parent.data.get('solved_image', './output/output.png')

        try:
            img = Image.open(solved_image_path)
            img = img.resize((500, 500), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(self, image=img, bg="black")
            img_label.image = img
            img_label.pack(pady=20)

            solve_more_button = tk.Button(
                self, text="Solve Another", font=("Arial", 16), bg="cyan", fg="black",
                command=self.solve_more
            )
            solve_more_button.pack(pady=10)
        except Exception:
            tk.Label(self, text="Solved Sudoku image not found!",
                     font=("Arial", 16), bg="black", fg="white").pack(pady=20)

    def solve_more(self):
        self.parent.switch_frame("upload.UploadPhase")

