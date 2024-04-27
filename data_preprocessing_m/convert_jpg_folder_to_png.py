from PIL import Image
import os


def convert_jpg_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            # Open JPG image
            jpg_path = os.path.join(input_folder, filename)
            jpg_image = Image.open(jpg_path)

            # Construct output file path with PNG extension
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(output_folder, png_filename)

            # Convert and save as PNG
            jpg_image.save(png_path, format='PNG')
            print(f"Converted {filename} to PNG and saved as {png_path}")


# Example usage
#input_folder = r"C:\Users\maria\Downloads\papka train\train_orig_images_jpg"
#output_folder = r"C:\Users\maria\Downloads\papka train\train_orrig_images_png"
#convert_jpg_to_png(input_folder, output_folder)