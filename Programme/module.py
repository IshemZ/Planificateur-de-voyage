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
        print(f"{self.ville} est la ville de destination où vous pourrez {activite_str}.")

class Voyage:
    
    def __init__(self, budget):
        self.destinations = []
        self.budget = budget

    def ajouter_destination(self, destination):
        if isinstance(destination, Destination):
            self.destinations.append(destination)
        else:
            print("Erreur : La destination doit être une instance de la classe Destination")

    def afficher_itineraire(self):
        for destination in self.destinations:
            if isinstance(destination, Destination):
                destination.afficher_destination()
            else:
                print("Erreur : Un objet dans la liste des destinations n'est pas une instance de la classe Destination")

    def afficher_budget(self):
        print(f"Le budget Voyage est de {self.budget} €")

    def ajouter_fonds(self, montant):
        self.budget += montant

    def retirer_fonds(self, montant):
        if montant <= self.budget:
            self.budget = self.budget - montant
        else:
            print(f"Le solde du budget est de : {self.budget}€ et vous voulez retirez {montant}€, Le solde ne peux donc pas être négatif")



#Créer des instance de Voyageurs avec le nom et l'âge
voyageur1 = Voyageur("Luc", 43)



# Ajouter des destinations au voyage
destination1 = Destination("Paris")
destination1.ajout_activite("Visiter la Tour-Eiffel")
destination1.ajout_activite("Prendre un verre dans une terrasse")

destination2 = Destination("Londres")
destination2.ajout_activite("Visiter le British Museum")
destination2.ajout_activite("Faire un tour sur le London Eye")


# Créer une instance de Voyage avec un budget initial
voyage1 = Voyage(1000)
voyage1.afficher_budget()
voyage1.ajouter_fonds(200)
voyage1.afficher_budget()
voyage1.retirer_fonds(1000)
voyage1.afficher_budget()
voyage1.retirer_fonds(300)
voyage1.afficher_budget()

voyage1.ajouter_destination(destination1)
voyage1.ajouter_destination(destination2)
voyage1.afficher_itineraire()