import os
import shutil

# ⚠️ CHANGE THIS PATH
# This should be the folder you want to ORGANIZE
# DO NOT set this to the folder where organizer.py is stored
folder_path = r"C:\test-files"

# File type mapping
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

# Create folders if they don't exist
for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Create Others folder
os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if not os.path.isfile(file_path):
        continue

    moved = False

    for folder, extensions in file_types.items():
        if file.lower().endswith(tuple(extensions)):
            shutil.move(file_path, os.path.join(folder_path, folder, file))
            moved = True
            break

    if not moved:
        shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("Files organized successfully!")
