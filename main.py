from automatConstructor import Node, Automat
from menu import *

import os


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
    
    
    #a = Automat()
    #a.createFiniteStateMachine('lexique6.txt')

    '''
    a.updateWordCounter('bonjour')
    a.updateWordCounter('symbole')
    a.updateWordCounter('symbole')

    print(str(a.displayWordCounter('symbole')))
    '''
    OpenFile()

   
main()