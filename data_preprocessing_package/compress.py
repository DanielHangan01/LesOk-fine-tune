import subprocess
import os


def compress_and_replace_images(input_folder, max_width=1024):

    n = 0
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            subprocess.run(["convert", input_path, "-resize", str(max_width), input_path])

            subprocess.run(["pngquant", "--force", "--ext", ".png", "--quality", "20-80", input_path])

            print(n)
            n += 1
    print("finished")

input_folder = "/Users/egor/Desktop/test for upload"

compress_and_replace_images(input_folder)






