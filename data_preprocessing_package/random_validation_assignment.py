import os
import random
import shutil

def move_and_delete_files(source_folder, target_folder, num_files):

    files = os.listdir(source_folder)
    random_files = random.sample(files, num_files)
    for filename in random_files:
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)
        shutil.move(source_path, target_path)
        print(f"Moved {filename} to {target_folder}")
    print(f"Moved {num_files} files from {source_folder} to {target_folder}")

folder_a = "/Users/egor/Desktop/images for upload Kopie"
folder_b = "/Users/egor/Desktop/masks for upload Kopie"
folder_c = "/Users/egor/Desktop/validation images for upload"
folder_d = "/Users/egor/Desktop/validation masks for upload"

move_and_delete_files(folder_a, folder_c, 100)

files_in_c = os.listdir(folder_c)
for filename in files_in_c:
    shutil.move(os.path.join(folder_b, filename), os.path.join(folder_d, filename))

print("Process completed successfully!")
