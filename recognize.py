import os
import cv2
import pytesseract
import numpy as np

def recognize_sudoku():
    cell_dir = "./image/cells/"
    if not os.path.exists(cell_dir):
        print(f"Error: Directory {cell_dir} does not exist. Run segment.py first.")
        return

    sudoku_matrix = [[0 for _ in range(9)] for _ in range(9)]
    
    for row in range(9):
        for col in range(9):
            cell_filename = f"cell_{row}_{col}.png"
            cell_path = os.path.join(cell_dir, cell_filename)

            cell_img = cv2.imread(cell_path, cv2.IMREAD_GRAYSCALE)
            if cell_img is None:
                print(f"Warning: Could not read {cell_path}. Skipping this cell.")
                continue

            # Preprocess the image for OCR
            inverted_img = cv2.bitwise_not(cell_img)

            ocr_result = pytesseract.image_to_string(
                inverted_img,
                config='--psm 10 digits'
            )

            # Extract the recognized digit
            try:
                digit = int(ocr_result.strip())
                sudoku_matrix[row][col] = digit
            except ValueError:
                sudoku_matrix[row][col] = 0

    print("Sudoku Matrix:")
    for row in sudoku_matrix:
        print(" ".join(map(str, row)))

    return sudoku_matrix

if __name__ == "__main__":
    recognize_sudoku()

