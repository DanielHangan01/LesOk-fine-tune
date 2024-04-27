from PIL import Image
import os


def convert_images_to_rgb(folder_path):

    n = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)

            with Image.open(image_path) as img:
                rgb_image = img.convert("RGB")
                rgb_image.save(image_path)
            print(n)
            n += 1
folder_path = "/Users/egor/Desktop/test"
convert_images_to_rgb(folder_path)