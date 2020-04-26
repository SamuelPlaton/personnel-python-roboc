# -*-coding:Utf-8 -*
# ROBOC SAMUEL PLATON POUR OPENCLASSROOM

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import sys
from carte import Carte
from labyrinthe import Labyrinthe


# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            carte = Carte(nom_fichier, contenu)
            cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# On demande à l'utilisateur de choisir une carte parmi celles disponibles puis on récupère son nom
#Traitement des exceptions si une mauvaise valeur est entrée
labyrinthe_choisi = 0
while labyrinthe_choisi < 1 or labyrinthe_choisi > len(cartes):
    try:  # Vérifie qu'un chiffre est entré
        labyrinthe_choisi = input("\n Sélectionnez une carte : ")
        labyrinthe_choisi = int(labyrinthe_choisi)
    except ValueError:
        print("La valeur rentrée n'est pas valide, un chiffre est demandé")

if labyrinthe_choisi == 1:  # Attribution de la carte
    nom_fichier = "cartes/facile.txt"
elif labyrinthe_choisi == 2:
    nom_fichier = "cartes/prison.txt"
elif labyrinthe_choisi == 3:
    nom_fichier = "cartes/samuel_carte.txt"

# On affiche le labyrinthe pour la première fois
with open(nom_fichier, "r") as fichier:
    contenu = fichier.read()
    print("\n Voici le labyrinthe : \n")
    print(contenu)

# On récupère chaque ligne du labyrinthe dans une liste afin de créer l'objet labyrinthe
lignes_labyrinthe = cartes[labyrinthe_choisi-1].creer_labyrinthe_depuis_chaine(contenu)
labyrinthe = Labyrinthe(lignes_labyrinthe, nom_fichier)

porte_avant = False
commande = input("\nQuelle commande choisissez-vous : ")
#S'assure que la commande entrée est bien une direction
while commande[0].lower() != "n" and commande[0].lower() != "s" and commande[0].lower() != "e" and commande[0].lower() != "o" and commande[0].lower() != "q":
    print("Les commandes autorisées sont n e s o q")
    commande = input("\nQuelle commande choisissez-vous : ")
resultat, porte_avant, quitter = labyrinthe.commande(commande, porte_avant)
if quitter == True: # Stopper le programme
    sys.exit()

while resultat == False: #Demande de jouer tant que le robot n'est pas à l'arrivée
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        print(contenu)
    commande = input("\nQuelle commande choisissez-vous : ")
    # S'assure que la commande entrée est bien une direction
    while commande[0].lower() != "n" and commande[0].lower() != "s" and commande[0].lower() != "e" and commande[
        0].lower() != "o" and commande[0].lower() != "q":
        print("Les commandes autorisées sont n e s o q")
        commande = input("\nQuelle commande choisissez-vous : ")
    resultat, porte_avant, quitter = labyrinthe.commande(commande, porte_avant)
    if quitter == True:  # Stopper le programme
        sys.exit()

if resultat == True: # Affiche le labyrinthe une fois gagné
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        print(contenu)

