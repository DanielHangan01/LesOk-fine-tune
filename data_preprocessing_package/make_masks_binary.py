import os
import cv2
import numpy as np

def process_image(file_path):
    image = cv2.imread(file_path)

    if image is None:
        print(f"Error: Could not read image {file_path}")
        return

    mask = np.all(image == [0, 255, 0], axis=-1)

    mask = mask.astype(np.uint8) * 255

    mask = cv2.bitwise_not(mask)

    black_background = np.zeros_like(image)

    black_background[mask == 0] = [255, 255, 255]

    cv2.imwrite(file_path, black_background)

folder_path = '/Users/egor/Desktop/train'

for filename in os.listdir(folder_path):
    if filename.lower().endswith('.png'):
        file_path = os.path.join(folder_path, filename)
        process_image(file_path)
        print(f"Processed: {file_path}")

print("Processing completed.")
