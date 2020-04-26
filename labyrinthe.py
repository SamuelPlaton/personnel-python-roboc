# -*-coding:Utf-8 -*
import pickle
"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, lignes_labyrinthe, nom_fichier):
        """ Constructeur de la classe Labyrinthe"""
        self.nom_fichier = nom_fichier
        self.robot = "X"
        self.sortie = "U"
        self.porte = "."
        self.mur = "O"
        self.passage = " "
        self.lignes_labyrinthe = lignes_labyrinthe # Liste de liste de String (Labyrinthe découpé en lignes puis en caractères)

    def position_robot(self):
        """ Méthode qui sert à récupérer la position du robot en x et y"""
        x = 0
        y = 0
        while y < len(self.lignes_labyrinthe):
            if self.robot in self.lignes_labyrinthe[y]:
                while x < len(self.lignes_labyrinthe[y]):
                    if self.robot in self.lignes_labyrinthe[y][x]:
                        return y, x
                    x += 1
            y += 1

    def commande(self, commande, porte_avant):
        """ Méthode servant à faire déplacer le pion selon la commande choisie"""

        # Récupération de la position du robot
        robotY, robotX = self.position_robot()

        # Transforme la commande en liste afin de récupérer l'orientation et le nombre de blocs
        commande = list(commande)

        # Traitement des possibilités selon si c'est la sortie, un mur, une porte ou une voie simple

        victoire = False # Etablit la victoire comme fausse
        quitter = False # Passe en true si le joueur appuie sur q

        try: # Mets la répétition à 1 si aucune info donnée ou si elle est erronée (ex : ee)
            répéteur = commande[1]
            répéteur = int(répéteur)
        except IndexError:
            répéteur = 1
        except ValueError:
            répéteur = 1

        i = 0
        while i < répéteur: # Boucle pour répéter le coup

            # Préparation des nouvelles coordonnées du robot selon le choix
            if commande[0].lower() == "n":
                newRobotY = robotY-1
                newRobotX = robotX
            if commande[0].lower() == "s":
                newRobotY = robotY+1
                newRobotX = robotX
            if commande[0].lower() == "e":
                newRobotY = robotY
                newRobotX = robotX+1
            if commande[0].lower() == "o":
                newRobotY = robotY
                newRobotX = robotX-1
            if commande[0].lower() == "q": # Si le joueur quitte la partie
                quitter = True
                print("Sauvegarde de la partie...")
                self.reecriture()
                return victoire, porte_avant, quitter

            # Vérification que la voie est libre, si non, le robot reprend ses anciennes coordonnées
            if self.lignes_labyrinthe[newRobotY][newRobotX] == "O":
                newRobotX = robotX
                newRobotY = robotY
                print("\n/!\ Impossible ! Il y a un mur /!\\")
                return victoire, porte_avant, quitter

            # Vérifie si le robot est passé par une porte ou un espace vide
            if porte_avant == False:
                self.lignes_labyrinthe[robotY][robotX] = " "
            elif porte_avant == True:
                self.lignes_labyrinthe[robotY][robotX] = "."

            # Scénario si le robot passe sur un espace vide
            if self.lignes_labyrinthe[newRobotY][newRobotX] == " ":
                porte_avant = False
                self.lignes_labyrinthe[newRobotY][newRobotX] = "X"
                robotY = newRobotY
                robotX = newRobotX
                self.reecriture()

            # Scénario si le robot passe par une porte
            elif self.lignes_labyrinthe[newRobotY][newRobotX] == ".":
                porte_avant = True
                self.lignes_labyrinthe[newRobotY][newRobotX] = "X"
                robotY = newRobotY
                robotX = newRobotX
                self.reecriture()
            # Scénario si le robot passe par l'arrivée
            elif self.lignes_labyrinthe[newRobotY][newRobotX] == "U":
                self.lignes_labyrinthe[newRobotY][newRobotX] = "X"
                robotY = newRobotY
                robotX = newRobotX
                self.reecriture()
                print("\n Bravo, t'as gagné !")
                victoire = True
                return victoire, porte_avant, quitter
            i += 1
        return victoire, porte_avant, quitter

    def reecriture(self):
        """ Retransforme la liste de liste en String
        Puis la réecrit dans le .txt à chaque coup"""
        y = 0
        x = 0
        nouvelle_chaine = ""
        while y < len(self.lignes_labyrinthe):
                while x < len(self.lignes_labyrinthe[y]):
                    nouvelle_chaine += self.lignes_labyrinthe[y][x]
                    x += 1
                x = 0
                y += 1
                if y == len(self.lignes_labyrinthe): # Correction d'un bug qui faisait disparaître une ligne si la première commande sélectionnée était S
                    break
                nouvelle_chaine += "\n"
        mon_fichier = open(self.nom_fichier, "w")
        mon_fichier.write(nouvelle_chaine)
        mon_fichier.close()



