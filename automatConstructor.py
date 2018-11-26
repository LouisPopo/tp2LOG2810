import queue

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
    
    def __init__(self):
        self.initNode = Node(False, "")
        self.wordDict = dict()
        self.recentlyUsedWordsQueue = queue.Queue(5)


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
                self.addWord(word)
                self.wordDict[word] = listLabels


    def updateWordCounter(self, word):
        self.wordDict[word][0] += 1
    
    def updateRecentlyUsedWords(self, word):
        if self.recentlyUsedWordsQueue.full():
            self.recentlyUsedWordsQueue.get()
        self.recentlyUsedWordsQueue.put(word)




    