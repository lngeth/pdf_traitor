import tkinter as tk
from tkinter import filedialog
from pdftools.PdfTools import PdfTools

class TkInterface:
    def __init__(self) -> None:
        self.dir_dest = ""
        self.root = tk.Tk()
        self.pdftools = PdfTools()

        self.root.title("Pdf Tools")
        self.root.configure(width=1000, height=800, bg="lightgray")

        add_files_btn = tk.Button(self.root, text="Ajouter fichier(s)", command=self.activate_add_files_btn)
        add_files_btn.pack()

        compress_btn = tk.Button(self.root, text="Compresser", command=self.compress_files)
        compress_btn.pack()

        delete_all_files_btn = tk.Button(self.root, text="Supprimer tout", command=self.delete_all_files)
        delete_all_files_btn.pack()

        merge_files_btn = tk.Button(self.root, text="Fusionner", command=self.merge_files)
        merge_files_btn.pack()

        self.files_list = tk.Listbox(self.root, selectmode="MULTIPLE")
        self.files_list.pack()

    
    def run(self):
        self.root.mainloop()

    def activate_add_files_btn(self):
        new_files = self.get_files_to_compress()
        self.pdftools.update_list_files(new_files)
        
        for f in new_files:
            self.files_list.insert(self.files_list.size(), f)

    def delete_all_files(self):
        if (self.files_list.size() != 0):
            self.files_list.delete(0, last=self.files_list.size())
        self.pdftools.list_files = []

    def compress_files(self):
        self.dir_dest = self.get_destination_directory_name()
        
        if (self.files_list.size() != 0 and self.dir_dest != ""):
            self.pdftools.compress_files(self.dir_dest)
        else:
            print("You must select files to compress AND the destination directory!")

    def merge_files(self):
        if (self.files_list.size() != 0):
            self.dir_dest = self.get_destination_directory_name()

            if (self.dir_dest != ""):
                print("Error: You have to select a destination repo!")
            else:
                self.pdftools.merge_files(self.dir_dest)
        else:
            print("Error: No files to merge!")

    # Pop Windows to select all files to compress
    def get_files_to_compress(self) -> str:
        return filedialog.askopenfilenames()
    
    # Pop Windows, select the directory destionation and return the repo's name
    def get_destination_directory_name(self) -> str:
        return filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")], defaultextension="pdf")