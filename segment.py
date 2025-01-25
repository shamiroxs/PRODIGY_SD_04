import cv2
import os
import numpy as np

def segment_sudoku_image():

    input_path = "./image/processed.png"
    output_dir = "./image/cells/"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the processed image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read the image from {input_path}")
        return

    height, width = img.shape
    
    if height != width:
        print("Error: The input image is not square. Please provide a square sudoku image.")
        return

    cell_size = height // 9  
    padding = int(cell_size * 0.00)  

    for row in range(9):
        for col in range(9):
            start_row = row * cell_size + 7
            end_row = (row + 1) * cell_size + 3
            start_col = col * cell_size + 4
            end_col = (col + 1) * cell_size - padding
            
            cell = img[start_row:end_row, start_col:end_col]

            cell_filename = f"cell_{row}_{col}.png"
            cell_path = os.path.join(output_dir, cell_filename)
            cv2.imwrite(cell_path, cell)
    
    print(f"Sudoku cells segmented and saved to {output_dir}")

if __name__ == "__main__":
    segment_sudoku_image()

