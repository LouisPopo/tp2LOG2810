

class Node:

    isFinal = None 

    id = ""

    nextNodes = None

    def __init__(self, isFinal, id):
        self.isFinal = isFinal
        self.id = id
        self.nextNodes = dict()

    def addNode(self, letter, isFinal): 
        self.nextNodes[letter] = Node(isFinal, letter)

class Automat:
    
    initNode = None
    
    def __init__(self):
        self.initNode = Node(False, "")


    def addWord(self, word):

        currentNode = self.initNode

        for letter in word:
            
            if letter not in currentNode.nextNodes:
                
                isFinal = False
                if letter == word[-1]:
                    isFinal = True
                
                currentWord = currentNode.id + letter
                currentNode.nextNodes[letter] = Node(isFinal, currentWord)

            currentNode = currentNode.nextNodes[letter]


    def createFiniteStateMachine(self, fileName):

        with open(fileName, 'r') as f:
            for word in f.readlines():
                self.addWord(word)


    