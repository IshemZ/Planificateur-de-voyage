import tkinter as tk
from tkinterweb import HtmlFrame
import folium
import os

# Créer une carte centrée sur Paris
carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
# Ajouter un marqueur pour une destination
folium.Marker([48.8566, 2.3522], popup="Paris").add_to(carte)
# Sauvegarder la carte en HTML
carte.save("carte.html")

# Créer la fenêtre principale Tkinter
root = tk.Tk()
root.title("Carte Interactive avec Folium et tkinterweb")
root.geometry("800x600")

# Créer un cadre pour afficher la carte
frame = HtmlFrame(root)
frame.pack(fill="both", expand=True)

# Charger le fichier HTML de la carte
file_path = os.path.abspath("carte.html")
frame.load_file(file_path)

# Démarrer la boucle principale de l'application Tkinter
root.mainloop()
