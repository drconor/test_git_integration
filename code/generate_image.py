import numpy as np
from PIL import Image
import os
import argparse

def generate_random_image(output_path, size_mb, width=1024, height=1024):
    """
    Generate a random image of approximately the specified size in MB.

    :param output_path: Path to save the generated image.
    :param size_mb: Desired file size in MB.
    :param width: Width of the image (default: 1024).
    :param height: Height of the image (default: 1024).
    """
    # Estimate the required number of bytes
    target_size = size_mb * 1024 * 1024  # Convert MB to bytes

    # Generate random pixel data
    channels = 3  # RGB
    img_array = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)

    # Create image from array
    img = Image.fromarray(img_array, 'RGB')

    # Save image and adjust compression to match target size
    quality = 95  # Start with high quality
    while True:
        img.save(output_path, format="PNG", optimize=True, quality=quality)
        actual_size = os.path.getsize(output_path)
        if abs(actual_size - target_size) < 0.05 * target_size or quality <= 10:
            break
        quality -= 5  # Decrease quality to reduce file size

    print(f"Image saved at {output_path}, Size: {actual_size / (1024 * 1024):.2f} MB")

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random image of a specified size (in MB).")
    parser.add_argument("output_path", type=str, help="Path to save the generated image (e.g., 'random.png').")
    parser.add_argument("size_mb", type=float, help="Desired image file size in MB.")
    parser.add_argument("--width", type=int, default=1024, help="Width of the image (default: 1024).")
    parser.add_argument("--height", type=int, default=1024, help="Height of the image (default: 1024).")

    args = parser.parse_args()

    generate_random_image(args.output_path, args.size_mb, args.width, args.height)
