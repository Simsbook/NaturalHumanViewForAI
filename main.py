from src.preprocessing.rgb_to_hsv import convert_rgb_to_hsv
from src.perception.object_recognition import recognize_objects

def main(image_path):
    # Step 1: Preprocess the image
    hsv_image = convert_rgb_to_hsv(image_path)
    print("Image converted to HSV format.")
    
    # Step 2: Recognize objects
    objects = recognize_objects(hsv_image)
    print(f"Recognized objects: {objects}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Human Natural View for AI")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image")
    args = parser.parse_args()
    main(args.image)
