import os

# change this to any folder you want to explore
folder_path = "C:/Users"

for root, dirs, files in os.walk(folder_path):
    print(f"\nCurrent folder: {root}")
    print(f"Subfolders: {dirs}")
    print(f"Files: {files}")