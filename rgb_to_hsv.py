import cv2

def convert_rgb_to_hsv(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found at the specified path.")
    
    # Convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image
