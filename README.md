
# File Organizer using Python

This is a simple Python script that organizes files in a folder based on their file type.

## What this project does

- Scans a given folder
- Creates folders like Images, PDFs, Documents, Videos, and Others
- Moves files into the correct folder based on their extension

## File types supported

- Images: .jpg, .jpeg, .png, .gif
- PDFs: .pdf
- Documents: .docx, .txt, .pptx, .xlsx
- Videos: .mp4, .mkv, .avi
- All other files go into the **Others** folder

## Requirements

- Python 3.x
- No external libraries required

## How to use

1. Open the script file
2. Change the folder path if needed:
   ```python
   folder_path = r"C:\test-files"
````

3. Run the script:

   ```bash
   python file_organizer.py
   ```
4. Files will be organized automatically

## Notes

* Existing folders are not affected
* Files with unknown extensions are moved to the **Others** folder

## Future improvements

* Add support for more file types
* Add a GUI
* Take folder path as user input


## Brutally honest feedback

- This is **not an advanced project**. It’s beginner level.
- Good for learning `os` and `shutil`, nothing more.
- If you put this on GitHub, **don’t call it “advanced” or “automation system.”**
- To improve it:
  - Add logging
  - Handle name conflicts
  - Accept folder path from command line
  - Add tests

If you want, I can **rewrite this README to sound more professional** or help you **level this project up** so it’s resume-worthy.
```
