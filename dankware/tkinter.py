from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

def folder_selector(title: str = "Select Folder", icon_path: str = "") -> str:

    """
    Opens folder selector and returns selected folder path
    - Allows custom title and icon
    """

    root = Tk()
    root.withdraw()
    if icon_path: root.iconbitmap(icon_path)
    folder_path = askdirectory(title=title)
    return folder_path.replace("/", "\\")

def file_selector(title: str = "Select File", icon_path: str = "") -> str:

    """
    Opens file selector and returns selected file path
    - Allows custom title and icon
    """

    root = Tk()
    root.withdraw()
    if icon_path: root.iconbitmap(icon_path)
    file_path = askopenfilename(title=title)
    return file_path.replace("/", "\\")
