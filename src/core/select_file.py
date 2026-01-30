import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"),
            ("All files", "*.*")
        ]
    )
    return file_path