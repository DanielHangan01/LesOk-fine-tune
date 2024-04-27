import os
from PIL import Image
from tqdm import tqdm

def get_unique_rgb_codes(png_folder):
    """
    Get a list of unique RGB color codes used in all PNG images in a folder.

    :param png_folder: Path to the folder containing PNG files.
    :return: Dictionary mapping file names to lists of unique RGB color codes.
    """
    rgb_codes_dict = {}  # Dictionary to store unique RGB color codes for each image

    # Variables to track criteria fulfillment
    rgb_range_fulfilled = True
    alpha_255_fulfilled = True
    all_zero_or_255_fulfilled = True

    # Iterate through each PNG file in the folder
    for filename in tqdm(os.listdir(png_folder)):
        if filename.endswith('.png'):
            png_file_path = os.path.join(png_folder, filename)
            rgb_codes = set()  # Use a set to store unique RGB color codes

            # Open the image
            with Image.open(png_file_path) as img:
                # Convert the image to RGB mode to ensure we're working with RGB colors
                img_rgb = img.convert("RGBA")
                # Get the width and height of the image
                width, height = img_rgb.size
                # Iterate through each pixel in the image
                for x in range(width):
                    for y in range(height):
                        # Get the RGB color of the pixel
                        rgba = img_rgb.getpixel((x, y))
                        # Add the RGB color to the set
                        rgb_codes.add(rgba)

                        # Check if the first three parameters in the pixel tuple are between 0 and 255
                        r, g, b, _ = rgba
                        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                            rgb_range_fulfilled = False

                        # Check if the last parameter in the pixel tuple is equal to 255
                        if rgba[3] != 255:
                            alpha_255_fulfilled = False

                        # Check if all three parameters in the pixel tuple are either 0 or 255
                        if not all(x in (0, 255) for x in rgba[:3]):
                            all_zero_or_255_fulfilled = False

            # Store the list of unique RGB color codes in the dictionary
            rgb_codes_dict[filename] = list(rgb_codes)

    # Print the results of criteria fulfillment
    print("1) Whether the first three parameters in each image tuple take values between 0 and 255 (both inclusively):",
          rgb_range_fulfilled)
    print("2) Whether the last parameter in every tuple (for each picture in the package) is equal to 255:",
          alpha_255_fulfilled)
    print("3) Whether all three parameters in each tuple for every picture in the package are either all equal to zero or all equal to 255:",
          all_zero_or_255_fulfilled)

    return rgb_codes_dict

# Example usage:
#png_folder = r"C:\Users\maria\Downloads\papka train\am_test_png_images"
#rgb_codes_dict = get_unique_rgb_codes(png_folder)