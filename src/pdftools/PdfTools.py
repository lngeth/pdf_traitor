import aspose.pdf as ap

class PdfTools:
    def __init__(self) -> None:
        pass
    
    def compress_files(self, files_list, output_directory):
        for i in range(len(files_list)):
          # Charger le fichier PDF
          compress_pdf_document = ap.Document(files_list[i])

          # Créer un objet de la classe OptimizationOptions
          pdfoptimize_options = ap.optimization.OptimizationOptions()

          # Activer la compression des images
          pdfoptimize_options.image_compression_options.compress_images = True

          # Définir la qualité de l'image
          pdfoptimize_options.image_compression_options.image_quality = 50

          # Compresser PDF
          compress_pdf_document.optimize_resources(pdfoptimize_options)

          if (len(files_list) > 1):
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