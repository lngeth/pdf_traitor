import tkinter as tk

class TkInterface:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()
        print("initialization")
    
    def print_coucou(self) -> None:
        print("coucou")