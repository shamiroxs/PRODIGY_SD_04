import cv2
import numpy as np

def clear_gridlines(input_path, output_path):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))  # Adjust width as needed
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))  # Adjust height as needed

    horizontal_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
    vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=1)

    grid_lines = cv2.add(horizontal_lines, vertical_lines)

    cleaned_image = cv2.subtract(binary, grid_lines)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cleaned_image = cv2.dilate(cleaned_image, kernel, iterations=1)

    cv2.imwrite(output_path, cleaned_image)
    print(f"Gridlines removed and saved as {output_path}")

clear_gridlines('./image/processed.png', './image/processed.png')

