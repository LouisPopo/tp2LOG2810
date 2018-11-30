from queue import Queue

class Node:

    isFinal = None 

    id = ""

    nextNodes = None

    def __init__(self, isFinal, id):
        self.isFinal = isFinal
        self.id = id
        self.nextNodes = dict()

    # Adds a next node to a current node
    def addNode(self, letter, isFinal): 
        self.nextNodes[letter] = Node(isFinal, letter)

    # Returns a word considering current semi-word entered
    def findPossibleWordsFromNode(self): 
        possibleWords = [] # Empty list of possible words

        if self.isFinal :
            possibleWords.append(self)

        if self.nextNodes : 
            for nextLetter in self.nextNodes:
                possibleWords = possibleWords + self.nextNodes[nextLetter].findPossibleWordsFromNode()


        return possibleWords


class Automat:
    
    initNode = None

    wordDict = None

    recentlyUsedWordsQueue = None

    possibleWords = None
    
    def __init__(self):
        self.initNode = Node(False, "")
        self.wordDict = dict()
        self.recentlyUsedWordsQueue = Queue(5)

        self.possibleWords = list()

    # Adds a letter to a node
    # Used to create a tree
    def addWord(self, word):

        currentNode = self.initNode

        letterCounter = 1

        for letter in word:
            
            if letter not in currentNode.nextNodes:
                
                isFinal = False
                if letterCounter == len(word):
                    isFinal = True
                
                currentWord = currentNode.id + letter
                currentNode.nextNodes[letter] = Node(isFinal, currentWord)

            currentNode = currentNode.nextNodes[letter]

            letterCounter = letterCounter + 1

    # Creates a tree with all the possible words of the file entered
    def createFiniteStateMachine(self, fileName):
        
        # Fist label is the word counter, second is the recently used boolean
        listLabels = []
        listLabels.append(0)
        listLabels.append(0)

        with open(fileName, 'r') as f:
            for word in f.readlines():
                self.addWord(word.rstrip())

                # Secondary dictionnary containing all words
                # Used to acces labels and quick search a complete word
                self.wordDict[word.rstrip()] = listLabels.copy()

    # Takes in a word or semi-word and returns the list of possible Words
    # Returns None if semi-word doesnt exist
    def findPossibleWords(self, word):  
                                    
        currentNode = self.initNode

        for letter in word:
            if letter in currentNode.nextNodes:
                # We change node to the next one
                currentNode = currentNode.nextNodes[letter] 
            else :
                return None

        return currentNode.findPossibleWordsFromNode()

    def updateWordCounter(self, word):
        self.wordDict[word][0] += 1
    
    # Updates the labels dicitonnary and adds the word to the recently used queue
    # If the queue is full, pop the earliest word entered and add the new one
    def updateRecentlyUsedWords(self, word):
        if self.recentlyUsedWordsQueue.full():
            poppedBack = self.recentlyUsedWordsQueue.get()
            self.wordDict[poppedBack][1] = 0
        self.recentlyUsedWordsQueue.put(word)
        self.wordDict[word][1] = 1

    def displayRecentlyUsedWords(self):

        # Queue to list for printing
        printingList = list(self.recentlyUsedWordsQueue.queue)
        return printingList

    def displayWordCounter(self, word):
        return self.wordDict[word][0]

    #Checks if the word is in the file
    def isWord(self, word):
        if word in self.wordDict:
            return True
        return False


    