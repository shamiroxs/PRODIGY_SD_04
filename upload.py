from tkinter import filedialog, Frame, Label, Button
from PIL import Image

class UploadPhase(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        Label(self, text="Upload Sudoku Image", font=("Arial", 30), bg="black", fg="white").pack(pady=50)
        
        Button(
            self, text="Upload Image", font=("Arial", 20), bg="grey", fg="white",
            command=self.upload_file
        ).pack(pady=20)
        
        Button(
            self, text="Solve", font=("Arial", 20), bg="cyan", fg="black",
            command=self.solve_sudoku
        ).pack(pady=20)
        
        self.message_label = Label(self, text="", font=("Arial", 16), bg="black", fg="yellow")
        self.message_label.pack(pady=30)

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Sudoku Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if file_path:
            image = Image.open(file_path)
            image.save("./image/input.png")
            self.display_message("Image uploaded successfully!")
            self.parent.data['input_image'] = "./image/input.png"
        else:
            self.display_message("No file selected.")

    def display_message(self, message):
        self.message_label.config(text=message)
        self.after(3000, lambda: self.message_label.config(text=""))

    def solve_sudoku(self):
        if 'input_image' in self.parent.data:
            self.parent.switch_frame("loading.LoadingPhase")
        else:
            self.display_message("No image uploaded!")

