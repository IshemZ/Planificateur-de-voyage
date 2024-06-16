# Simulateur de Planification de Voyage

## Objectif
Créer un programme qui aide un utilisateur à planifier un voyage. Le programme permettra de :

- Ajouter des destinations avec des activités.
- Calculer le budget nécessaire pour chaque destination.
- Afficher l'itinéraire complet.
- Ajouter et retirer des fonds du budget de voyage.
- Gérer les informations sur les voyageurs.

## Étapes du Projet
Définir les classes principales :

- Voyageur: contient les informations de base d'un voyageur.
- Destination: représente une destination avec un nom, des activités et des coûts associés.
- Voyage: gère les destinations, le budget et les voyageurs.

Créer les méthodes principales pour chaque classe :

- Pour Voyageur: méthodes pour afficher les informations du voyageur.
- Pour Destination: méthodes pour ajouter des activités et calculer les coûts.
- Pour Voyage: méthodes pour ajouter des destinations, gérer le budget et afficher l'itinéraire.
Utiliser des boucles et des conditions pour l'interaction utilisateur :

Menu principal pour naviguer entre les différentes fonctionnalités.
Demander à l'utilisateur d'ajouter ou de retirer des destinations et des activités.

------------------------------------------------------
Étape 1 : Définir les classes
1.1. Définir la classe Voyageur

Question : Comment définir une classe en Python et quelles informations de base un Voyageur devrait-il avoir ?

Indice : Une classe en Python se définit avec le mot-clé class. Un Voyageur pourrait avoir des attributs comme nom et age.

À faire :

Définir une classe Voyageur.
Ajouter un constructeur (__init__) qui initialise les attributs nom et age.

1.2. Définir la classe Destination

Question : Quels attributs et méthodes une classe Destination pourrait-elle avoir ?

Indice : Pense aux informations et actions nécessaires pour une destination de voyage. Par exemple, elle pourrait avoir un nom, une liste d'activités et une méthode pour ajouter des activités.

À faire :

Définir une classe Destination.
Ajouter un constructeur qui initialise le nom et une liste vide pour les activités.
Ajouter une méthode pour ajouter une activité.

1.3. Définir la classe Voyage

Question : Quels attributs et méthodes une classe Voyage devrait-elle avoir pour gérer plusieurs destinations et un budget ?

Indice : Pense aux fonctionnalités que nous avons décrites. La classe pourrait avoir une liste de destinations, un budget et des méthodes pour ajouter des destinations et gérer le budget.

À faire :

Définir une classe Voyage.
Ajouter un constructeur qui initialise une liste de destinations et un budget.
Ajouter une méthode pour ajouter une destination.

Une fois que tu as terminé ces trois classes, nous passerons à la prochaine étape qui consiste à ajouter des fonctionnalités à ces classes. N'hésite pas à poser des questions si tu es bloqué ou si tu veux des indices supplémentaires !

---------------------------------------------------------------

Concepts Utilisés
Classes et Objets :

Création de classes (Voyageur, Destination, Voyage).
Initialisation des objets avec des attributs.
Méthodes :

Définition et utilisation de méthodes pour manipuler les attributs des objets (ajout_activite, afficher_destination, etc.).

Listes :
Utilisation des listes pour stocker plusieurs objets (activite dans Destination, destinations dans Voyage).

Conditions :
Vérification des types d'objets avec isinstance pour s'assurer que seules les bonnes instances sont ajoutées.

Gestion du Budget :
Ajout et retrait de fonds avec vérification des conditions pour éviter les soldes négatifs.


# Suggestions pour Aller Plus Loin

Ajouter des Voyageurs :
Étendre la classe Voyage pour inclure une liste de voyageurs et gérer leurs informations.

Enrichir les Détails des Activités :
Permettre à chaque activité d'avoir un coût associé et de calculer le coût total des activités pour une destination.

Interactivité :
Créer une interface utilisateur simple pour ajouter des destinations, des activités et des voyageurs via des entrées utilisateur.


Sauvegarde et Chargement :
Implémenter des fonctionnalités pour sauvegarder l'état du voyage dans un fichier et le charger plus tard.

Tests Unitaires :   
Écrire des tests unitaires pour vérifier le bon fonctionnement de chaque méthode de manière isolée.