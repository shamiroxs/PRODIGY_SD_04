import cv2
import numpy as np

def clear_gridlines(input_path, output_path):
    # Load the processed image
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Ensure the image is binary
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Define kernels for detecting horizontal and vertical lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))  # Adjust width as needed
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))  # Adjust height as needed

    # Detect horizontal lines
    horizontal_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)

    # Detect vertical lines
    vertical_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=1)

    # Combine detected lines
    grid_lines = cv2.add(horizontal_lines, vertical_lines)

    # Subtract grid lines from the original image
    cleaned_image = cv2.subtract(binary, grid_lines)

    # Optional: Apply slight dilation to clean up noise caused by grid removal
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cleaned_image = cv2.dilate(cleaned_image, kernel, iterations=1)

    # Save the cleaned image
    cv2.imwrite(output_path, cleaned_image)
    print(f"Gridlines removed and saved as {output_path}")

# Example usage
clear_gridlines('./image/processed.png', './image/processed.png')

