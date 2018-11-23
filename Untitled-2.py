def creerDict(nomFichier):
    fichier = open(nomFichier, "r").read()
    mots = fichier.split("\n")
    return mots

def main():
    mots = creerDict("lexique6.txt")
    print (mots)
    