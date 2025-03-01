import cv2

def crop_to_square():
    input_path = "./image/input.png"
    output_path = "./image/cropped.png"

    image = cv2.imread(input_path)
    
    if image is None:
        print("Error: Input image not found!")
        return

    height, width = image.shape[:2]

    if width > height:
        diff = (width - height) // 2
        cropped_image = image[:, diff:diff + height]
    else:
        diff = (height - width) // 2
        cropped_image = image[diff:diff + width, :]

    # Save the cropped image
    cv2.imwrite(output_path, cropped_image)
    print(f"Cropped image saved at {output_path}")

if __name__ == "__main__":
    crop_to_square()

