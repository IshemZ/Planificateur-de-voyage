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
    def test_initialisation(self):
        destination = Destination("Paris")
        self.assertEqual(destination.ville, "Paris")
        self.assertEqual(destination.activite, [])
    
    def test_ajout_activite(self):
        destination = Destination("Paris")
        destination.ajout_activite("Visiter la Tour-Eiffel")
        self.assertIn("Visiter la Tour-Eiffel", destination.activite)
    
    def test_afficher_destination(self):
        destination = Destination("Paris")
        destination.ajout_activite("Visiter la Tour-Eiffel")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        destination.afficher_destination()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Paris est la ville de destination où vous pourrez Visiter la Tour-Eiffel.")

class TestVoyage(unittest.TestCase):
    def test_initialisation(self):
        voyage = Voyage(1000)
        self.assertEqual(voyage.budget, 1000)
        self.assertEqual(voyage.destinations, [])
    
    def test_ajouter_destination(self):
        voyage = Voyage(1000)
        destination = Destination("Paris")
        voyage.ajouter_destination(destination)
        self.assertIn(destination, voyage.destinations)
    
    def test_afficher_itineraire(self):
        voyage = Voyage(1000)
        destination = Destination("Paris")
        destination.ajout_activite("Visiter la Tour-Eiffel")
        voyage.ajouter_destination(destination)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        voyage.afficher_itineraire()
        sys.stdout = sys.__stdout__
        self.assertIn("Paris est la ville de destination où vous pourrez Visiter la Tour-Eiffel.", captured_output.getvalue().strip())
    
    def test_ajouter_fonds(self):
        voyage = Voyage(1000)
        voyage.ajouter_fonds(200)
        self.assertEqual(voyage.budget, 1200)
    
    def test_retirer_fonds(self):
        voyage = Voyage(1000)
        voyage.retirer_fonds(500)
        self.assertEqual(voyage.budget, 500)
        voyage.retirer_fonds(600)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        voyage.retirer_fonds(600)
        sys.stdout = sys.__stdout__
        self.assertIn("Le solde du budget est de : 500 € et vous voulez retirer 600 €, Le solde ne peut donc pas être négatif", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()