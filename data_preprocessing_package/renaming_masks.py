import os

folder_path = '/Users/egor/Desktop/train Kopie'

for filename in os.listdir(folder_path):
    if filename.lower().endswith('_mask.png'):
        number = filename.split('_')[0]

        new_filename = f"{number}.png"

        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"Renamed {filename} to {new_filename}")

    elif filename.lower().endswith('.jpg'):
        os.remove(os.path.join(folder_path, filename))
        print(f"Deleted {filename}")

print("Renaming and deletion completed.")
