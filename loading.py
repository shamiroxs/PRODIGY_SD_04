import tkinter as tk
import threading
from process import preprocess_image
from resize import resize_image
from segment import segment_sudoku_image
from recognize import recognize_sudoku
from solver import solve_sudoku, create_sudoku_image

class LoadingPhase(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        self.parent = parent
        self.init_ui()
        threading.Thread(target=self.run_background_tasks, daemon=True).start()

    def init_ui(self):
        self.label = tk.Label(self, text="Loading...", font=("Arial", 24), bg="black", fg="white")
        self.label.pack(expand=True)

    def run_background_tasks(self):
        try:
            preprocess_image(self.parent.data['input_image'], "./image/processed.png")
            resize_image()
            segment_sudoku_image()
            unsolved_matrix = recognize_sudoku()
            if solve_sudoku(unsolved_matrix):
                create_sudoku_image(unsolved_matrix)
                self.parent.data['solved_image'] = "./output/output.png"
            else:
                print("No solution exists.")
        except Exception as e:
            print(f"Error: {e}")

        self.parent.switch_frame("prints.PrintPhase")

