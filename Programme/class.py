class Voyageur: #nom de la classe
    
    def __init__ (self, nom, age): #constructeur init avec les attributs de la classe
        self.nom = nom 
        self.age = age

    def afficher_info(self):
        print(f"Le nom du voyageur est {self.nom} et il a {self.age} ans.")
        


    
    
    
class Destination:

    def __init__(self, ville, activite):
        self.ville = ville
        self.activite = activite
        
        
    def ajout_activite(self):
        self.activite
    
    
#Voyageur1 = Voyageur("Conrad", 24)