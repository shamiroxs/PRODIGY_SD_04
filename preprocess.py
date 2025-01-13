import cv2
import numpy as np
import os

def preprocess_image(input_path="./image/input.png", output_path="./image/cropped.png"):
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Read the image
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Cannot load image from {input_path}")
        return False

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve thresholding
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Iterate over the contours to find the largest quadrilateral
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.021 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the polygon has 4 corners (quadrilateral)
        if len(approx) == 4:
            # Reorder the points for perspective transform
            points = approx.reshape(4, 2)
            rect = reorder_points(points)

            # Perform a perspective transformation
            warped = four_point_transform(gray, rect)

            # Save the processed image
            cv2.imwrite(output_path, warped)
            print(f"Processed image saved to {output_path}")
            return True

    print("Error: Sudoku grid not detected")
    return False

def reorder_points(points):
    # Reorder points to top-left, top-right, bottom-right, bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]  # Top-left
    rect[2] = points[np.argmax(s)]  # Bottom-right

    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]  # Top-right
    rect[3] = points[np.argmax(diff)]  # Bottom-left

    return rect

def four_point_transform(image, rect):
    # Unpack points
    (tl, tr, br, bl) = rect

    # Compute the width and height of the new image
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    # Destination points for a top-down view of the Sudoku grid
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    # Compute the perspective transform matrix and apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

if __name__ == "__main__":
    preprocess_image()

