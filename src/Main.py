import aspose.pdf as ap
from tkinter import filedialog
from tkinterface.TkInterface import TkInterface

interface = TkInterface()

# Fichier à compresser
files_to_compress = filedialog.askopenfilenames()

# répertoire de destination
dir_dest = filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")], defaultextension="pdf")


for i in range(len(files_to_compress)):
  # Charger le fichier PDF
  compressPdfDocument = ap.Document(files_to_compress[i])

  # Créer un objet de la classe OptimizationOptions
  pdfoptimizeOptions = ap.optimization.OptimizationOptions()

  # Activer la compression des images
  pdfoptimizeOptions.image_compression_options.compress_images = True

  # Définir la qualité de l'image
  pdfoptimizeOptions.image_compression_options.image_quality = 50

  # Compresser PDF
  compressPdfDocument.optimize_resources(pdfoptimizeOptions)

  if (len(files_to_compress) > 1):
    tmp = dir_dest.split("/")
    dir_dest = ""
    filename = tmp[-1].split(".")[0].split("(")[0].strip() + " (" + str(i) + ").pdf"
    for i in range(len(tmp) - 1):
      dir_dest += tmp[i]
      if (i != len(tmp) - 1):
        dir_dest += "/"
    dir_dest += filename

  # Enregistrez le PDF compressé
  compressPdfDocument.save(dir_dest)