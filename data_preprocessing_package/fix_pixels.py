from PIL import Image, ImageDraw
import os
import math


def calculate_distance(color1, color2):
    """
    Calculate the Euclidean distance between two RGB colors.

    :param color1: RGB color tuple (r1, g1, b1).
    :param color2: RGB color tuple (r2, g2, b2).
    :return: Euclidean distance between the two colors.
    """
    return math.sqrt((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2)


def process_images(input_folder):

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            with Image.open(input_path) as img:
                img_rgb = img.convert("RGB")
                width, height = img_rgb.size
                processed_img = Image.new("RGB", (width, height))
                processed_img_draw = ImageDraw.Draw(processed_img)
                for x in range(width):
                    for y in range(height):
                        r, g, b = img_rgb.getpixel((x, y))
                        if (r, g, b) != (255, 255, 255) and (r, g, b) != (0, 0, 0):
                            distance_to_black = calculate_distance((r, g, b), (0, 0, 0))
                            distance_to_white = calculate_distance((r, g, b), (255, 255, 255))
                            if distance_to_black <= distance_to_white:
                                processed_img_draw.point((x, y), fill=(0, 0, 0))
                            else:
                                processed_img_draw.point((x, y), fill=(255, 255, 255))
                        else:
                            processed_img_draw.point((x, y), fill=(r, g, b))
                processed_img.save(input_path)
                print(f"Processed image saved to {input_path}")


input_folder = "/Users/egor/Desktop/masha"
process_images(input_folder)
