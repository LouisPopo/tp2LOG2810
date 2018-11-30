import os.path
from automatConstructor import *


#Create Automat object
automat = Automat()

#Choices display
def display():
    print(
'''

**************************************************
*                    Choix:                      *
**************************************************
* a) Écrire un mot                               *
* b) Afficher les mots récemment utilisés        *
* c) Afficher le compteur d'un mot               *
* d) Quitter                                     *
**************************************************
'''
    )

#Choices display2
def display2():
    print(
'''

**************************************************
*                    Choix:                      *
**************************************************
* a) Ajouter une lettre au mot                   *
* b) Entrer le mot                               *
**************************************************
'''
    )


#Returns true if file exists
def fileExists(fileName):
    return os.path.isfile(fileName)

#First and only function called from main
#Allows the use of a file for the program
def OpenFile():

    updatedFile = -1

    #Error control: create file only if it exists
    while not fileExists(updatedFile):
        updatedFile = input("Veuillez entrer un fichier contenant des mots (avec l'extension .txt): ")
        if not fileExists(updatedFile):
            print ("Le nom de fichier n'existe pas")

    #Create language with correct file
    automat.createFiniteStateMachine(updatedFile)
    print("Fichier recu!")

    #Go to menu
    menu()

#TODO
#Option a: write
def write():
    wordWritten = ""
    done = False
    while not done:

        #Display the options to the user 
        display2()
        print("Mot présent: " + str(wordWritten))
        choice2 = input("Veuillez choisir un option (a ou b): ")

        #The user choses to add a letter
        if choice2 == 'a':
            letterToAdd = input("Veuillez ajouter une lettre à votre mot: ")
            wordWritten += letterToAdd
            node = automat.findWordState(wordWritten)
            possibleWords = node.findPossibleWords()
            if not possibleWords:
                print("Aucun mot possible!")
            else:
                print("\nMots possibles: ")
                for word in possibleWords:
                    print(word.id + ", ")

        #The user choses to confirm his word
        elif choice2 == 'b':
            if automat.isWord(wordWritten):
                automat.updateRecentlyUsedWords(wordWritten)
                automat.updateWordCounter(wordWritten)
                done = True
                print("Le mot existe et est mis à jour!")
            else:
                choice3 = input("Ceci n'est pas un mot! Voulez-Vous recommencer? Si oui, tapez OUI: ")
                wordWritten = ""
                if choice3 != "OUI":
                    menu()

        else:
            print("Veuillez choisir un option valide!")
    menu()

#Option b: Display 5 recently used words
def recentlyUsedWords():
    print("Mots récemment utilisés: " + str(automat.displayRecentlyUsedWords()))
    menu()

#Option c: Display how many times a word is used
def wordCounter():
    wordToBeCounted = input("Veuillez entrer un mot: ")
    if automat.isWord(wordToBeCounted):
        print("Le mot a été écrit " + str(automat.displayWordCounter(wordToBeCounted)) + " fois!")
    else:
        print("Le mot n'est pas dans le lexique!")
    menu()

#Option d: quit
#Display end of program and return 0
def quitProgram():
    print("Fin du programme")
    return 0


#Option menu
#Allows centralisation of functions
def menu():

    #Dictionnary of possible options for user
    options = { 'a' : write,
                'b' : recentlyUsedWords,
                'c' : wordCounter,
                'd' : quitProgram,
    }

    #Display choices and ask user to choose from one of them
    display()
    choice = input("Veuillez entrer un option (a, b, c, d): ")

    #If the choice is within options, go to option, else display error message and
    #call menu
    if choice in options:
        print("Vous avez entré: " + choice)
        options[choice]()
    else:
        print("Cette option n'existe pas. Veuillez choisir l'une des option possible: ")
        menu()