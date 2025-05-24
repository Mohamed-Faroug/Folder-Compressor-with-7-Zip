## 📦 Folder Compressor with 7-Zip (Auto Split + Archive Naming)

This Python script compresses a folder (including subfolders) using **7-Zip**, automatically:

- Names the archive based on the current folder and timestamp
- Splits the archive into **1800MB** parts (`.7z.001`, `.7z.002`, ...)
- Moves the output files to a specific backup directory (`D:\Backup` by default)

---

## 🛠 Requirements

- [Python 3.6+](https://www.python.org/downloads/)
- [7-Zip](https://www.7-zip.org/) installed
- Ensure `7z.exe` path is correct in the script (default: `C:\Program Files\7-Zip\7z.exe`)

---

## 🚀 How to Use

1. Place the script inside the folder you want to compress.
2. Run the script:

```bash
python compress_folder.py
```
## The script will:

- Create a compressed archive with a timestamped name

- Split the archive into parts (max 1800MB each)

- Move all parts to D:\Backup

## 🧰 Example Output
If compressing a folder named MyVideos, the output will be saved to:
  ```bash  D:\Backup\
      ├── MyVideos_2025-05-25_21-15.7z.001
      ├── MyVideos_2025-05-25_21-15.7z.002
      └── ...
  ```
## 🔧 Configuration
  You can edit these in the script:
  ```bash
  SEVEN_ZIP_PATH = r"C:\Program Files\7-Zip\7z.exe"
  PART_SIZE_MB = 1800
  DESTINATION_FOLDER = r"D:\Backup"
 ```
## Features
* ✅ Supports nested folders

* ✅ Works in the current directory

* ✅ Archive split for large files (better for upload)

* ✅ Auto-folder naming and timestamp

* ✅ Backup destination auto-created if missing

## 🧪 Tested On

* Windows 10 / 11

* Python 3.12

* 7-Zip 23.01
## 📄 License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

