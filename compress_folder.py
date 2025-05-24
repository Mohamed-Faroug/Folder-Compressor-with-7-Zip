import os
import subprocess
import shutil
from datetime import datetime

# === Settings ===
FOLDER_TO_COMPRESS = os.getcwd()
PART_SIZE_MB = 1800
SEVEN_ZIP_PATH = r"C:\Program Files\7-Zip\7z.exe"  # Update if needed
DESTINATION_FOLDER = r"D:\Backup"

def compress_with_7zip(folder_path, part_size_mb, destination_folder):
    # Generate archive name from folder and timestamp
    folder_name = os.path.basename(os.path.abspath(folder_path))
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    archive_base = f"{folder_name}_{timestamp}.7z"
    archive_path = os.path.join(folder_path, archive_base)
    part_size = f"{part_size_mb}m"

    # Build 7z command
    command = [
        SEVEN_ZIP_PATH,
        'a',
        archive_path,
        '.',  # Include everything in the folder
        f'-v{part_size}',
        '-mx=9'
    ]

    print("Running:", " ".join(command))
    subprocess.run(command, cwd=folder_path)

    # Move .7z.* files to destination
    os.makedirs(destination_folder, exist_ok=True)
    part_prefix = archive_base + "."
    for file in os.listdir(folder_path):
        if file.startswith(part_prefix):
            src = os.path.join(folder_path, file)
            dst = os.path.join(destination_folder, file)
            shutil.move(src, dst)
            print(f"Moved {file} to {destination_folder}")

    print("\n✅ Done. Files saved to:", destination_folder)

if __name__ == "__main__":
    compress_with_7zip(FOLDER_TO_COMPRESS, PART_SIZE_MB, DESTINATION_FOLDER)
