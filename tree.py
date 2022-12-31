import node


class Tree:
    def __init__(self):
        self.functionalSymbols = ["ADD", "SUB", "MUL", "DIV"]
        self.terminalSymbols = ["V", "R", "S"]
        self.nodeList = []
        self.createList = []
        self.depth = 0
        self.treeDictionary = {}

    def getFunctionalSymbols(self):
        return self.functionalSymbols

    def getTerminalSymbols(self):
        return self.terminalSymbols

    def getRootNode(self):
        return self.root

    def getTree(self):
        if self.nodeList is not None:
            return self.nodeList

    def insertSubtree(self, subtree, newNode, oldNodeIndex, oldNodeCopy=None, secoundTree=False):
        oldNode = oldNodeCopy if secoundTree else self.getTree()[oldNodeIndex]
        self.deleteSubtree(oldNodeIndex)
        previousNode = oldNode.getPreviosNode()
        newNode.setPreviousNode(previousNode)
        newNode.setRang(oldNode.getRang())
        if previousNode.getLeftNode() is None:
            previousNode.addLeftNode(newNode)
        elif previousNode.getRightNode() is None:
            previousNode.addRightNode(newNode)
        self.nodeList.insert(oldNodeIndex, newNode)
        self.treeDictionary[newNode.getRang()].append(newNode)
        subtree.remove(newNode)
        for i, item in enumerate(subtree, start=1):
            item.setRang(item.getPreviosNode().getRang() + 1)
            self.nodeList.insert(oldNodeIndex + i, item)
            if item.getRang() in self.treeDictionary:
                self.treeDictionary[item.getRang()].append(item)
            else:
                self.treeDictionary[item.getRang()] = [item]

    def deleteSubtree(self, node):
        currentNode = self.getTree()[node]
        if currentNode.isRootNode():
            self.nodeList = []
            self.root = None
            self.treeDictionary = {}
            self.depth = 0
        else:
            previousNode = currentNode.getPreviosNode()
            if previousNode.getLeftNode() == currentNode:
                previousNode.addLeftNode(None)
            elif previousNode.getRightNode() == currentNode:
                previousNode.addRightNode(None)
            else:
                print("Error: Node not found!")
            nodeList = [currentNode]
            while nodeList:
                if currentNode.existsLeftNode() and currentNode.getLeftNode() is not None:
                    nodeList.append(currentNode.getLeftNode())
                if currentNode.existsRightNode() and currentNode.getLeftNode() is not None:
                    nodeList.append(currentNode.getRightNode())
                if currentNode in self.getTree(): self.getTree().remove(currentNode)
                for array in self.treeDictionary.values():
                    if currentNode in array:
                        array.remove(currentNode)
                nodeList.remove(currentNode)
                if nodeList:
                    currentNode = nodeList[0]
            tempDict = self.treeDictionary.copy()
            for item in tempDict.keys():
                if len(tempDict[item]) == 0:
                    del self.treeDictionary[item]


    def __len__(self):
        return len(self.nodeList)

    def getTreeDictionary(self):
        return self.treeDictionary

    def createTree(self, stringAsTree):
        rang = 0
        self.root = node.Node(stringAsTree[:3])
        self.root.setToRootNode()
        self.nodeList.append(self.root)
        self.createList.append(self.root)
        self.root.setRang(0)
        self.treeDictionary[rang] = [self.root]
        stringAsTree = stringAsTree[3:]
        for i, char in enumerate(stringAsTree):
            if char == "(":
                nodeValue = stringAsTree[i + 1:i + 4]
                if nodeValue in self.functionalSymbols:
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList)-1]
                    previousNode.addLeftNode(currentNode)
                    currentNode.setPreviousNode(self.createList[len(self.createList)-1])
                    self.createList.append(currentNode)
                    print("Node erstellt: " + str(currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    rang += 1
                    self.depth += 1
                    currentNode.setRang(rang)
                    if rang in self.treeDictionary:
                        self.treeDictionary[rang].append(currentNode)
                    else:
                        self.treeDictionary[rang] = [currentNode]
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList) - 1]
                    previousNode.addLeftNode(currentNode)
                    #currentNode.addLeftNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    rang += 1
                    self.depth +=1
                    currentNode.setRang(rang)
                    if rang in self.treeDictionary:
                        self.treeDictionary[rang].append(currentNode)
                    else:
                        self.treeDictionary[rang] = [currentNode]
            elif char == ",":
                nodeValue = stringAsTree[i + 1:i + 4]
                previousNode = self.createList[len(self.createList) - 1]
                if nodeValue in self.functionalSymbols:
                    currentNode = node.Node(str(nodeValue))
                    previousNode.addRightNode(currentNode)
                    currentNode.addRightNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    self.createList.append(currentNode)
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    currentNode.setRang(rang)
                    if rang in self.treeDictionary:
                        self.treeDictionary[rang].append(currentNode)
                    else:
                        self.treeDictionary[rang] = [currentNode]
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    previousNode.addRightNode(currentNode)
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    currentNode.setRang(rang)
                    if rang in self.treeDictionary:
                        self.treeDictionary[rang].append(currentNode)
                    else:
                        self.treeDictionary[rang] = [currentNode]
            elif char == ")":
                self.createList.pop()
                rang -= 1
            print(str(i) + ": Creation List: " + str(self.createList))
        print("--------------------------------------------------")

    def getDepth(self):
        return self.depth

    def __str__(self):
        if len(self.nodeList) <= 0:
            return "Der Baum ist leer!"
        else:
            string = ""
            for item in self.nodeList:
                if item.isRootNode():
                    string += item.getNodeValue() + ".0: Root \n"
                else:
                    string += item.getNodeValue() + "." + str(item.getRang()) + ": " + item.getPreviosNode().getNodeValue() + "." + str(item.getPreviosNode().getRang()) + "\n"
        return string
