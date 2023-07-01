from tkinterface.TkInterface import TkInterface
from pdftools.PdfTools import PdfTools

interface = TkInterface()
files_to_compress = interface.get_files_to_compress()
dir_dest = interface.get_destination_directory_name()

if (files_to_compress != "" and dir_dest != ""):
  pdftools = PdfTools()
  pdftools.compress_files(files_to_compress, dir_dest)
else:
  print("You must select files to compress AND the destination directory!")