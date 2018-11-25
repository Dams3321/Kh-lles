#!/usr/bin/python 3 
#khôlles
#Damien
#28/11/18

import csv 

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=int, nargs="+", help="Ajoute une ou plusieurs valeurs au csv")
parser.add_argument("-c",  action="store_true", help="Supprime toutes les valeurs au csv")
parser.add_argument("-l", action="store_true", help="Affiche le contenu du csv")
parser.add_argument("-s", action="store_true", help="Affiche la valeur maximum contenue dans le csv")
parser.add_argument("--max", action="store_true", help="Affiche la valeur maximum contenue dans le csv")
parser.add_argument("--min", action="store_true", help="Affiche la valeur minimum contenue dans le csv")
parser.add_argument("--moy", action="store_true", help="Affiche la moyenne contenue dans le csv")
parser.add_argument("--sum", action="store_true", help="Affiche la somme des valeurs du csv")
parser.add_argument("-t", action="store_true", help="Trie la liste par ordre croissant")
parser.add_argument("--desc", action="store_true", help="Trie la liste par ordre décroissant")
args = parser.parse_args()

li = []

#ajout d'un nombre

def ajoutenombre(value):
    liste.append(value)

#affiche la val max

def MaxVal():
    readCsv()
    maxval = max(liste_max)
    print(maxval)

#affiche la val min 

def MinVal():
    readCsv()
    minval = max(liste_max)
    print(minval)

#affiche moyenne

def moyenne():
    readCsv()
    moyenne = mean(nombre)
    print(moyenne)