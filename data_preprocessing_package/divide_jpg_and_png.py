import os
import shutil


def divide_files_by_extension(source_folder, jpg_folder, png_folder):
    # Create destination folders if they don't exist
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            # Determine file extension
            _, extension = os.path.splitext(filename)
            # Move files to the appropriate destination folder
            if extension.lower() == '.jpg':
                shutil.move(source_path, os.path.join(jpg_folder, filename))
                print(f"Moved {filename} to {jpg_folder}")
            elif extension.lower() == '.png':
                shutil.move(source_path, os.path.join(png_folder, filename))
                print(f"Moved {filename} to {png_folder}")
            else:
                print(f"Ignored {filename}: unsupported file format")


# Example usage
#source_folder = r"C:\Users\maria\Downloads\papka train\train_orig"
#jpg_folder = r"C:\Users\maria\Downloads\papka train\train_orig_images_jpg"
#png_folder = r"C:\Users\maria\Downloads\papka train\train_orig_masks_png"
#divide_files_by_extension(source_folder, jpg_folder, png_folder)