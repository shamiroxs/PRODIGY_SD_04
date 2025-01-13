import cv2
import os
import numpy as np

def segment_sudoku_image():
    # Input and output paths
    input_path = "./image/processed.png"
    output_dir = "./image/cells/"
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the processed image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read the image from {input_path}")
        return

    # Get the dimensions of the image
    height, width = img.shape
    
    # Ensure the image is square
    if height != width:
        print("Error: The input image is not square. Please provide a square sudoku image.")
        return

    # Calculate the size of each cell
    cell_size = height // 9  # Since it's a 9x9 grid
    padding = int(cell_size * 0.00)  # Adjust padding (5% of cell size)

    # Iterate through the grid and extract each cell
    for row in range(9):
        for col in range(9):
            # Calculate cell boundaries with padding adjustment
            start_row = row * cell_size + 7
            end_row = (row + 1) * cell_size + 3
            start_col = col * cell_size + 4
            end_col = (col + 1) * cell_size - padding
            
            # Crop the cell from the image
            cell = img[start_row:end_row, start_col:end_col]
            
            # Save the cell as an image
            cell_filename = f"cell_{row}_{col}.png"
            cell_path = os.path.join(output_dir, cell_filename)
            cv2.imwrite(cell_path, cell)
    
    print(f"Sudoku cells segmented and saved to {output_dir}")

# Execute the segmentation function
if __name__ == "__main__":
    segment_sudoku_image()

