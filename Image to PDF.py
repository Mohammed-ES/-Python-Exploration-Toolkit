import os
from fpdf import FPDF

# Chemin du dossier contenant les images
image_folder = "C:/Users/LENOVO/Desktop/CodePulse/Image"

# Chemin du dossier de sauvegarde du PDF
output_folder = "C:/Users/LENOVO/Desktop/CodePulse/PDF"

# Vérifier si le dossier de sortie existe, sinon le créer
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Créer un objet PDF
pdf = FPDF()

print("Entrez les noms des images à convertir en PDF. Tapez 'stop' pour terminer.")
while True:
    # Demander à l'utilisateur de saisir le nom du fichier image
    image_name = input("Nom de l'image : ").strip()
    
    # Vérifier si l'utilisateur souhaite arrêter
    if image_name.lower() == "stop":
        break
    
    # Chemin complet de l'image
    image_path = os.path.join(image_folder, image_name)
    
    # Vérifier si le fichier existe
    if os.path.exists(image_path):
        pdf.add_page()
        pdf.image(image_path, x=10, y=10, w=190)  
        print(f"L'image '{image_name}' a été ajoutée au PDF.")
    else:
        print(f"Erreur : Le fichier '{image_name}' n'existe pas. Veuillez réessayer.")

# Spécifier le chemin complet pour le fichier PDF de sortie
output_pdf = os.path.join(output_folder, "Images_to_PDF.pdf")

# Sauvegarder le fichier PDF
pdf.output(output_pdf, "F")
print(f"PDF créé avec succès : {output_pdf}")
