import node, copy


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

    def treeNodeHasUUID(self, uuid):
        return any(item.getUUID() == uuid for item in self.nodeList)

    def getTreeNodeByUUID(self, uuid):
        for item in self.nodeList:
            if item.getUUID() == uuid:
                return item

    def insertSubtree(self, subtree, newNode, oldNodeIndex, oldNodeCopy=None, secoundTree=False):

        # Merke dir den alten Knoten in diesem Baum
        oldNode = oldNodeCopy if secoundTree else self.getTree()[oldNodeIndex]

        # Erstelle eine Kopie des neuen Knotens der in diesen Baum eingefügt werden soll
        newNodeCopy = copy.deepcopy(newNode)

        # Erzeuge eine neue UUID für den neuen Knoten
        newNodeCopy.generateUUID()

        # Merke dir den Vorgänger des alten Knotens
        previousNode = oldNode.getPreviosNode()

        # Bestimme die Richtung, in der dieser neue Knoten eingefügt werden soll vom Vorgänger ausgegangen
        direction = "left" if previousNode.getLeftNode() == oldNode else "right"

        # Lösche den alten Teilbaum aus diesem Baum
        self.deleteSubtree(oldNodeIndex, oldNodeCopy, secoundTree)

        # Setze den Vorgänger des neuen Knotens auf den Vorgänger des alten Knotens
        newNodeCopy.setPreviousNode(previousNode)

        # Aktualisiere die Ebene des neuen Knotens
        newNodeCopy.setRang(oldNode.getRang())

        # Setze den neuen Knoten in die richtige Richtung vom Vorgänger aus
        if direction == "left":
            previousNode.setLeftNode(newNodeCopy)
        elif direction == "right":
            previousNode.setRightNode(newNodeCopy)

        # Füge den neuen Knoten in den Baum ein mit dem Index des alten Knotens, um die Baumstruktur zu erhalten
        self.nodeList.insert(oldNodeIndex, newNodeCopy)

        # Füge den neuen Knoten in das Baum Dictionary ein
        self.treeDictionary[newNodeCopy.getRang()].append(newNodeCopy)

        # Lösche den neuen Knoten aus der Menge der Knoten, die noch eingefügt werden müssen (Subtree)
        subtree.remove(newNodeCopy)

        # Iteriere über alle übrigen Knoten des Subtrees
        for i, item in enumerate(subtree, start=1):

            # Aktualisiere die Ebene von jedem Knoten des Subtrees
            item.setRang(item.getPreviosNode().getRang() + 1)

            # Füge den Knoten des Subtrees in den Baum ein nach dem neuen Knoten (Für die Darstellung wichtig)
            self.nodeList.insert(oldNodeIndex + i, item)

            # Wenn diese Ebene im Baum bereits existiert, füge den Knoten der Ebene hinzu
            if item.getRang() in self.treeDictionary:
                self.treeDictionary[item.getRang()].append(item)

            # Wenn diese Ebene im Baum noch nicht existiert, erstelle die Ebene und füge den Knoten der Ebene hinzu
            else:
                self.treeDictionary[item.getRang()] = [item]

    def deleteSubtree(self, subtree, tempDict=None):
        currentNode = subtree
        # Wenn der Knoten die Wurzel ist, wird der Baum gelöscht
        if currentNode.isRootNode():
            self.nodeList = []
            self.root = None
            self.treeDictionary = {}
            self.depth = 0
            del(self)

        # Wenn der Knoten nicht die Wurzel ist, wird der Teilbaum gelöscht
        else:

            # Wenn die Länge einer Ebene o ist, dann lösche die Ebene
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
                    previousNode.setLeftNode(currentNode)
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
                    previousNode.setLeftNode(currentNode)
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
                    previousNode.setRightNode(currentNode)
                    currentNode.setRightNode(self.createList[len(self.createList) - 1])
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
                    previousNode.setRightNode(currentNode)
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
            string = "".join(
                item.getNodeValue() + ".0: Root \n"
                if item.isRootNode()
                else f"{item.getNodeValue()}.{str(item.getRang())}: {item.getPreviosNode().getNodeValue()}.{str(item.getPreviosNode().getRang())}"
                + "\n"
                for item in self.nodeList
            )
        return string
