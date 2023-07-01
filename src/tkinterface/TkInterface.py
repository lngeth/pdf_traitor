import tkinter as tk
from tkinter import filedialog

class TkInterface:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()
    
    # Pop Windows to select all files to compress
    def get_files_to_compress(self) -> str:
        return filedialog.askopenfilenames()
    
    # Pop Windows, select the directory destionation and return the repo's name
    def get_destination_directory_name(self) -> str:
        return filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")], defaultextension="pdf")