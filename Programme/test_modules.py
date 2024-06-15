import unittest
from module import Voyageur, Voyage, Destination
import io
import sys


class TestVoyageur(unittest.TestCase):

#test de vérification de l'initialisation de la classe Voyageur
    def Test_initialisation(self):
        #créé un voyageur
        voyageur = Voyageur("Mona", 26)
        
        #vérifier que les attributs sont corrects
        self.assertEqual(voyageur.nom, "Mona")
        self.assertEqual(voyageur.age, 26)

#test pour la méthode "afficher_info"
    def Test_afficher_info(self):
        #créer un voyageur
        voyageur = Voyageur("Bob", 29)
        
        #capturer la sortie de la méthode "afficher_info"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        voyageur.afficher_info()
        sys.stdout = sys.__stdout__
        
        #vérifier que la sortie est correct
        self.assertEqual(captured_output.getvalue().strip(), "Le nom du voyageur est Bob et il a 29 ans.")

class TestDestination(unittest.TestCase):
    
    pass


class TestVoyage(unittest.TestCase):
    
    pass

if __name__ == '__main__':
    unittest.main()