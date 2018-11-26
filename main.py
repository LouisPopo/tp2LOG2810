from automatConstructor import Node, Automat
from menu import *
import os


def creerDict(nomFichier):
    fichier = open(nomFichier, "r").read()
    mots = fichier.split("\n")
    return mots


def main():
    """
    a = Automat()
    mot = "salut"
    a.addWord(mot)
    a.addWord("sale")
    print(a.initNode.nextNodes)
    print(a.initNode.nextNodes['s'].nextNodes['a'].id)
    print(a.initNode.nextNodes['s'].nextNodes['a'].nextNodes['l'].id)
    print(a.initNode.nextNodes['s'].nextNodes['a'].nextNodes['l'].nextNodes['u'].id)
    

    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    """


    # 1. creer un automate a laide dun fichier
    # 2. creer un wordsAlgos a laide de lautomate
    # 3. caller les fonctions sur wordsAlgos
    #OpenFile()
    a = Automat()
    a.createFiniteStateMachine('lexique6.txt')
    print(a.initNode.nextNodes['a'].nextNodes['b'].nextNodes['s'].id)

     


main()