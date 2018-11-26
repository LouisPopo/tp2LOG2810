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
    OpenFile()
    #a = Automat()
    #a.createFiniteStateMachine('lexique1.txt')
    #print(a.wordDict)

     


main()