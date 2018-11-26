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
        print ("Le nom de fichier n'existe pas")

    #Create language with correct file
    automat.createFiniteStateMachine(updatedFile)
    print("Fichier recu!")

    #Go to menu
    menu()

#TODO
#Option a: write
def write():
    wordWritten = None
    wordWritten.clear
    done = False

    while not done:
        display2()
        print("Mot présent: " + wordWritten)
        choice2 = input("Veuillez choisir un option (a ou b): ")
        if choice2 == 'a':
            letterToAdd = input("Veuillez ajouter une lettre à votre mot: ")
            print("Mots possibles: " + automat.displayPossibleWords(letterToAdd))
        elif choice2 == 'b':
            if automat.isWord(wordWritten):
                automat.updateRecentlyUsedWords(wordWritten)
                automat.updateWordCounter(wordWritten)
                done = True
            else:
                wordWritten = None
                print("Ceci n'est pas un mot! Veuillez recommencer.")
        else:
            print("Veuillez choisir un option valide!")
    menu()

#Option b: Display 5 recently used words
def recentlyUsedWords():
    print("Mots récemment utilisés: " + automat.displayRecentlyUsedWords())
    menu()

#Option c: Display how many times a word is used
def wordCounter():
    wordToBeCounted = input("Veuillez entrer un mot: ")
    print("Le mot a été écrit " + automat.displayWordCounter(wordToBeCounted) + " fois!")
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