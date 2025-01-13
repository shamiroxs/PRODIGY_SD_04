import cv2
import numpy as np

def preprocess_image(input_path, output_path):
    # Load the input image
    #output_path = "./image/processed.png"
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Input image not found!")
        return

    # Step 1: Binarization
    binary = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Step 2: Remove Gridlines
    # Detect horizontal lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    binary_without_horizontal = cv2.subtract(binary, detected_lines)

    # Detect vertical lines
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
    detected_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    binary_without_gridlines = cv2.subtract(binary_without_horizontal, detected_lines)

    # Step 3: Clean up and Enhance Digits
    # Apply dilation to make the digits thicker if needed
    kernel = np.ones((2, 2), np.uint8)
    cleaned_binary = cv2.dilate(binary_without_gridlines, kernel, iterations=1)

    # Step 4: Save the processed image
    cv2.imwrite(output_path, cleaned_binary)
    print(f"Processed image saved at {output_path}")

if __name__ == "__main__":
    input_path = "./image/cropped.png"
    preprocess_image(input_path)

