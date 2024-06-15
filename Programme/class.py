class Voyageur: #nom de la classe
    
    def __init__ (self, nom, age): #constructeur init avec les attributs de la classe
        self.nom = nom 
        self.age = age

    def afficher_info(self):
        print(f"Le nom du voyageur est {self.nom} et il a {self.age} ans.")
        

Voyageur1 = Voyageur("Conrad", 24)

Voyageur1.afficher_info()



class Destination:

    def __init__(self, ville):
        self.ville = ville
        self.activite = []

    def ajout_activite(self, activite):
        self.activite.append(activite)

    def afficher_destination(self):
        activite_str = ", ".join(self.activite)            
        print(f"{self.ville} est la ville de destination ou vous pourrez {activite_str} ")


Destination1 = Destination("Paris")
Destination1.ajout_activite("Visiter la Tour-Eiffel")
Destination1.ajout_activite("Prendre un verre dans une terrasse")
Destination1.afficher_destination()



