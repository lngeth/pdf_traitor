import aspose.pdf as ap
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Fichier à compresser
file_path = filedialog.askopenfilename()

# répertoire de destination
dir_dest = filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")], defaultextension="pdf")

# Charger le fichier PDF
# file_path = "C:\\Users\\lngeth\\Downloads\\retraite\\cotisation_assurance_maladie.pdf"
compressPdfDocument = ap.Document(file_path)

# Créer un objet de la classe OptimizationOptions
pdfoptimizeOptions = ap.optimization.OptimizationOptions()

# Activer la compression des images
pdfoptimizeOptions.image_compression_options.compress_images = True

# Définir la qualité de l'image
pdfoptimizeOptions.image_compression_options.image_quality = 50

# Compresser PDF
compressPdfDocument.optimize_resources(pdfoptimizeOptions)

# Enregistrez le PDF compressé
compressPdfDocument.save(dir_dest)