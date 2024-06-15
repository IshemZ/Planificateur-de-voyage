class Voyageur: #nom de la classe
    
    def __init__ (self, nom, age): #constructeur init avec les attributs de la classe
        self.nom = nom 
        self.age = age

    def afficher_info(self):
        print(f"Le nom du voyageur est {self.nom} et il a {self.age} ans.")


class Destination:

    def __init__(self, ville):
        self.ville = ville
        self.activite = []

    def ajout_activite(self, activite):
        self.activite.append(activite)

    def afficher_destination(self):
        activite_str = ", ".join(self.activite)            
        print(f"{self.ville} est la ville de destination ou vous pourrez {activite_str} ")


class Voyage:
    
    def __init__(self, budget):
        self.destinations = []
        self.budget = budget

    def ajouter_destination(self, destination):
        self.destinations.append(destination)

    def afficher_itinéraire(self):
        for destination in self.destinations:
            destination.afficher_itinéraire()

    def afficher_budget(self):
        print(f"Le budget Voyage est de {self.budget} €")

    def ajouter_fonds(self, montant):
        self.budget += montant

    def retirer_fonds(self, montant):
        if montant <= self.budget:
            self.budget -= montant
        else:
            print(f"Le solde budget est de : {self.budget} et ne peux donc pas être négatif")


Voyageur1 = Voyageur("Conrad", 24)
Voyageur1.afficher_info()


Destination1 = Destination("Paris")
Destination1.ajout_activite("Visiter la Tour-Eiffel")
Destination1.ajout_activite("Prendre un verre dans une terrasse")
Destination1.afficher_destination()

Voyage1 = Voyage(900)
Voyage1.afficher_budget()
Voyage1.afficher_itinéraire()
Voyage1.retirer_fonds(100)
Voyage1.afficher_budget()
Voyage1.ajouter_destination("Paris")
Voyage1.afficher_itinéraire()
