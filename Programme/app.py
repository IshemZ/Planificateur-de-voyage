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

## Onglet Voyageurs

#Fonction pour ajouter un voyageur
def ajouter_voyageurs():
    nom = entry_nom_voyageur.get()
    age = entry_age_voyageur.get()
    if nom and age:
        print(f"Ajout du voyageur : Nom - {nom}, Age - {age}")
    else:
        print("Les deux champs doivent être remplies pour integrer un nouveau voyageur.")

label_nom_voyageur = Tk.Label(frame_voyageurs, text="Nom du voyageur")
label_nom_voyageur.pack(pady=5)
entry_nom_voyageur = Tk.Entry(frame_voyageurs)
entry_nom_voyageur.pack(pady=5)

label_age_voyageur = Tk.Label(frame_voyageurs, text="Age du voyageur")
label_age_voyageur.pack(pady=5)
entry_age_voyageur = Tk.Entry(frame_voyageurs)
entry_age_voyageur.pack(pady=5)

button_ajouter_voyageur = Tk.Button(frame_voyageurs, text="Ajouter Voyageur", command=ajouter_voyageurs)
button_ajouter_voyageur.pack(pady=5)

## Onglet Voyageurs

#Fonction
def ajouter_destination():
    ville = entry_ville_destination.get()
    activite = entry_activite_destination.get()
    if ville and activite:
        print(f"Ajout de la desination : Ville - {ville}, Activite - {activite}")
    else:
        print("Tout les champs doivent être remplis pour integrer une nouvelle destination")

label_ville_destination = Tk.Label(frame_destinations, text="Ville de destination")
label_ville_destination.pack(pady=5)
entry_ville_destination = Tk.Entry(frame_destinations)
entry_ville_destination.pack(pady=5)

label_activite_destination = Tk.Label(frame_destinations, text="Activite de la destination")
label_activite_destination.pack(pady=5)
entry_activite_destination = Tk.Entry(frame_destinations)
entry_activite_destination.pack(pady=5)

button_ajouter_destination = Tk.Button(frame_destinations, text="Ajouter destination", command=ajouter_destination)
button_ajouter_destination.pack(pady=5)

## Onglet Voyage

def ajouter_voyage():
    budget = entry_budget_voyage.get()
    if budget:
        print(f"Ajout du budget voyage : Budget - {budget}")
    else:
        print("Tout les champs doivent être remplis pour integrer un nouveau budget")

label_budget_voyage = Tk.Label(frame_voyages, text="Budget de voyage")
label_budget_voyage.pack(pady=5)
entry_budget_voyage = Tk.Entry(frame_voyages)
entry_budget_voyage.pack(pady=5)

button_ajouter_voyage = Tk.Button(frame_voyages, text="Ajouter Voyage", command=ajouter_voyage)
button_ajouter_voyage.pack(pady=20)






#Lancer la fenêtre
root.mainloop()
