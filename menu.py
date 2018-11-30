import os.path
from automatConstructor import *
import getch


#Create Automat object
automat = Automat()

#Choices display
def display():
    print(
'''

************************************************
*                    Choix:                      *
************************************************
* a) Écrire un mot                               *
* b) Afficher les mots récemment utilisés        *
* c) Afficher le compteur d'un mot               *
* d) Quitter                                     *
************************************************
'''
    )

#Choices display2
def display2():
    print(
'''

************************************************
*                   Options :                  *
************************************************
*           1 pour entrer le mot               *
*   2 pour retourner à l'arrière d'une lettre  *
*       3 pour retourner au menu principal     *
************************************************
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

#Option a: write
def write():
    display2()
    print("Veuillez entrer un mot: ")
    wordWritten = ""

    #Dynamic input of letters
    char = getch.getch()

    while char != '1' and char != '3':

        #If user choses 2 and the string is empty, refuse operation and restart function
        #Else if user choses 2, remove last letter of string
        #Else increment the letter to the string
        if char == '2' and not wordWritten:
            print("Opération refusée: aucune lettre entrée")
            write()
        elif char == '2' and wordWritten:
            wordWritten = wordWritten[:-1]
        else:
            wordWritten += char

        #Finds all possible words
        possibleWords = automat.findPossibleWords(wordWritten)
        
        #If there is no words with that combination, return error message
        #Else show all possibilties
        if possibleWords == None:
            print("Aucun mot possible!")
        else:
            print("\nMots possibles: ")
            for word in possibleWords:
                print(word.id + ", ")
        
        display2()
        print("\nMot entré: " + wordWritten)
        char = getch.getch()

    #If the word exists, update to recently used and its word counter
    if char == '1':
        if automat.isWord(wordWritten):
                automat.updateRecentlyUsedWords(wordWritten)
                automat.updateWordCounter(wordWritten)
                print("Le mot existe et est mis à jour!")
        else:
            print("Le mot n'existe pas! Veuillez recommencer.")
            write()
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