import aspose.pdf as ap

class PdfTools:
  def __init__(self) -> None:
    self.list_files = []
  
  def compress_files(self, output_directory):
    for i in range(len(self.list_files)):
      # Charger le fichier PDF
      compress_pdf_document = ap.Document(self.list_files[i])

      # Créer un objet de la classe OptimizationOptions
      pdfoptimize_options = ap.optimization.OptimizationOptions()

      # Activer la compression des images
      pdfoptimize_options.image_compression_options.compress_images = True

      # Définir la qualité de l'image
      pdfoptimize_options.image_compression_options.image_quality = 50

      # Compresser PDF
      compress_pdf_document.optimize_resources(pdfoptimize_options)

      if (len(self.list_files) > 1):
        tmp = output_directory.split("/")
        output_directory = ""
        filename = tmp[-1].split(".")[0].split("(")[0].strip() + " (" + str(i) + ").pdf"
        for i in range(len(tmp) - 1):
          output_directory += tmp[i]
          if (i != len(tmp) - 1):
            output_directory += "/"
        output_directory += filename

      # Enregistrez le PDF compressé
      compress_pdf_document.save(output_directory)

  def update_list_files(self, l):
    for f in l:
      self.list_files.append(f)
  
  def merge_files(self, dir_dest):
    pdf_file_editor = ap.facades.PdfFileEditor()
    pdf_file_editor.concatenate(self.list_files, dir_dest)