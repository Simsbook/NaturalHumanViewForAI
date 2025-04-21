import pytest
from src.preprocessing.rgb_to_hsv import convert_rgb_to_hsv

def test_rgb_to_hsv():
    # Test with a sample image
    sample_image = "tests/sample_images/sample_image.jpg"
    hsv_image = convert_rgb_to_hsv(sample_image)
    assert hsv_image is not None
