import os
import shutil
from PIL import Image

#also names check

def synchronize_folders(folder_a, folder_c):
    """
    Synchronize files between two folders by keeping only files with the same name as in folder C in folder A,
    and deleting both files if their dimensions differ.

    :param folder_a: Path to folder A.
    :param folder_c: Path to folder C.
    """
    # Get the list of filenames in folder C
    files_c = set(os.listdir(folder_c))

    # Iterate over files in folder A
    for filename in os.listdir(folder_a):
        file_a_path = os.path.join(folder_a, filename)
        # Check if the filename exists in folder C
        if filename not in files_c:
            # If the filename doesn't exist in folder C, delete the file from folder A
            os.remove(file_a_path)
            print(f"Deleted {filename} from folder A")
        else:
            # Get the corresponding file in folder C
            file_c_path = os.path.join(folder_c, filename)
            # Check if both files have the same dimensions
            if get_image_dimensions(file_a_path) != get_image_dimensions(file_c_path):
                # If dimensions differ, delete both files
                os.remove(file_a_path)
                os.remove(file_c_path)
                print(f"Deleted {filename} from both folders due to different dimensions")
            else:
                print(f"Kept {filename} in folder A")


def get_image_dimensions(image_path):
    """
    Get the dimensions (width and height) of an image.

    :param image_path: Path to the image file.
    :return: Tuple containing width and height of the image.
    """
    with Image.open(image_path) as img:
        return img.size

# Example usage:
#folder_a = r"C:\Users\maria\Downloads\papka train\am_test_png_images"
#folder_c = r"C:\Users\maria\Downloads\papka train\am_test_png_masks"
#synchronize_folders(folder_a, folder_c)