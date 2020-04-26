# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        """ Crée une première liste de <str> représentant chaque ligne du labyrinthe,
        Puis crée et retourne une liste (labyrinthe) de liste(lignes) de caractères(Ce qui forme le labyrinthe"""
        ligne_liste1 = chaine.split("\n")
        ligne_liste2 = []
        i = 0
        while i < len(ligne_liste1):
            ligne = list(ligne_liste1[i])
            ligne_liste2.append(ligne)
            i += 1
        return ligne_liste2
