import os.path
from automatConstructor import *


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
    #createLanguage(updatedFile)
    print("Fichier recu!")

    #Go to menu
    menu()

#Option a: write
def write():
    menu()

#Option b: Display 5 recently used words
def recentlyUsedWords():
    #displayRecentlyUsedWords()
    menu()

#Option c: Display how many times a word is used
def wordCounter():
    wordToBeCounted = input("Veuillez entrer un mot: ")
    #print("Le mot a été écrit " + displayWordCounter(wordToBeCounted) + " fois!")
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