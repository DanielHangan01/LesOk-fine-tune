import os
import tifffile
from PIL import Image
import numpy as np

def process_tiff_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each TIFF file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.tif') or filename.endswith('.tiff'):
            # Load TIFF file into a NumPy array
            tif_file_path = os.path.join(input_folder, filename)
            tif_data = tifffile.imread(tif_file_path)

            # Normalize TIFF data to the range [0, 255]
            max_val = np.max(tif_data)
            min_val = np.min(tif_data)
            tif_data_normalized = ((tif_data - min_val) / (max_val - min_val)) * 255
            tif_data_normalized = np.uint8(tif_data_normalized)

            # Convert TIFF data to a Pillow image
            tif_image = Image.fromarray(tif_data_normalized)

            # Convert to RGB mode (remove alpha channel)
            tif_image = tif_image.convert("RGB")

            # Construct the output PNG file path
            png_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

            # Save the image as PNG with 0-255 color range
            tif_image.save(png_file_path, format="PNG")

            print(f"{filename} converted and saved as {png_file_path}")

# Example usage:
#input_folder = r"C:\Users\maria\Downloads\papka train\am_test_orig_masks"
#output_folder = r"C:\Users\maria\Downloads\papka train\am_test_png_masks"
#process_tiff_to_png(input_folder, output_folder)