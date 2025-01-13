import cv2
import os

def resize_image():
    """
    Resize the input image to the target size and save the output.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        target_size (tuple): The desired size (width, height).
    """
    input_path = "./image/processed.png"
    output_path = "./image/processed.png"
    
    target_size = (287, 287)
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: {input_path} does not exist.")
        return
    
    # Read the input image
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Unable to read {input_path}.")
        return

    # Resize the image to the target size
    resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    
    # Save the resized image
    cv2.imwrite(output_path, resized_image)
    print(f"Image resized and saved to {output_path}.")

if __name__ == "__main__":
    # Paths and target size

    # Resize and save the image
    resize_image()

