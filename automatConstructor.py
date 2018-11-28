import queue


class ToListQueue(queue.Queue):
    def to_list(self):
        with self.mutex:
            return list(self.queue)

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

    wordDict = None

    recentlyUsedWordsQueue = None

    possibleWords = None
    
    def __init__(self):
        self.initNode = Node(False, "")
        self.wordDict = dict()
        self.recentlyUsedWordsQueue = queue.Queue(5)
        self.possibleWords = list()

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
        
        listLabels = []
        listLabels.append(0)
        listLabels.append(0)

        with open(fileName, 'r') as f:
            for word in f.readlines():
                self.addWord(word.rstrip())
                self.wordDict[word.rstrip()] = listLabels


    def findWordState(self, word):  # prend le debut d'un mot, ou un mot, et retourne le noeud dans l'automate qui contient le semi-mot, ou 
                                    # le noeud initial s'il n'existe pas. 
        currentNode = self.initNode

        for letter in word:
            if letter in currentNode.nextNodes:
                currentNode = currentNode.nextNodes[letter] # on change de noeud on est rendu dans le suivant
            else :
                return currentNode
        return currentNode

    def findPossibleWords(self, node):
        possibleWords = [] # liste vide qui va contenir les mots finaux

        if node.isFinal :
            possibleWords.append(node)

        if node.nextNodes : # si le noeud contient des enfants
            for nextNode in node.nextNodes:
            possibleWords.append(self.possibleWords(nextNode))


    #TODO
    def displayPossibleWords(self, semiWord):
        """
        currentNode = self.initNode
        for letter in semiWord:
            if letter in currentNode.nextNodes:
                currentNode = currentNode.nextNodes[letter]

        if currentNode.isFinal:
            self.possibleWords.append(currentNode.id)

        for letter in currentNode.nextNodes:
            self.displayPossibleWords(currentNode.id)
        return self.possibleWords
        """

    def updateWordCounter(self, word):
        self.wordDict[word][0] += 1
    
    def updateRecentlyUsedWords(self, word):
        if self.recentlyUsedWordsQueue.full():
            poppedBack = self.recentlyUsedWordsQueue.get()
            self.wordDict[poppedBack][1] = 0
        self.recentlyUsedWordsQueue.put(word)
        self.wordDict[word][1] = 1

    def displayRecentlyUsedWords(self):
        listQueue = ToListQueue(self.recentlyUsedWordsQueue)
        return listQueue.to_list()

    def displayWordCounter(self, word):
        return self.wordDict[word][0]

    def isWord(self, word):
        if word in self.wordDict:
            return True
        return False


    