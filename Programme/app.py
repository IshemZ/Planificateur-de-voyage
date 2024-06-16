import tkinter as Tk
from tkinter import ttk

#Création de la fenêtre principale
root = Tk.Tk()
root.title("Gestionnaire de voyage")

#créer un widget notebook pour les onglets
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# créer les cadres pour les différents onglets
frame_voyageurs = ttk.Frame(notebook, width=400, height=280)
frame_destinations = ttk.Frame(notebook, width=400, height=280)
frame_voyages = ttk.Frame(notebook, width=400, height=280)

frame_voyageurs.pack(fill='both', expand=True)
frame_destinations.pack(fill='both', expand=True)
frame_voyages.pack(fill='both', expand=True)

#Ajouter les cadres comme onglets
notebook.add(frame_voyageurs, text="Voyageurs")
notebook.add(frame_destinations, text="Destinations")
notebook.add(frame_voyages, text="Voyages")

#Fonction pour ajouter un voyageur
def ajouter_voyageurs():
    nom = entry_nom_voyageur.get()
    age = entry_age_voyageur.get()
    if nom and age:
        print(f"Ajout du voyageur : Nom - {nom}, Age - {age}")
    else:
        print("Les deux champs doivent être remplies pour integrer un nouveau voyageur.")

#Onglet Voyageurs
label_nom_voyageur = Tk.Label(frame_voyageurs, text="Nom du voyageur")
label_nom_voyageur.pack(pady=5)
entry_nom_voyageur = Tk.Entry(frame_voyageurs)
entry_nom_voyageur.pack(pady=5)

label_age_voyageur = Tk.Label(frame_voyageurs, text="Age du voyageur")
label_age_voyageur.pack(pady=5)
entry_age_voyageur = Tk.Entry(frame_voyageurs)
entry_age_voyageur.pack(pady=5)


root.mainloop()
