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

    def insertSubtree(self, subtreeForInsert, subtreeForDeletion, oldNodeIndex, oldNodeCopy=None, secoundTree=False):

        # Merke dir den alten Knoten in diesem Baum
        oldNode = self.getTree()[oldNodeIndex]

        # Erstelle eine Kopie des neuen Knotens der in diesen Baum eingefügt werden soll
        newNodeCopy = copy.deepcopy(subtreeForInsert[0])

        # Erzeuge eine neue UUID für den neuen Knoten
        newNodeCopy.generateUUID()

        # Merke dir den Vorgänger des alten Knotens
        previousNode = oldNode.getPreviosNode()

        # Bestimme die Richtung, in der dieser neue Knoten eingefügt werden soll vom Vorgänger ausgegangen
        direction = "left" if previousNode.getLeftNode().getUUID() == oldNode.getUUID() else "right"

        # Lösche den alten Teilbaum aus diesem Baum
        self.deleteSubtree(subtreeForDeletion)

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
        subtreeForInsert.remove(subtreeForInsert[0].getTreeNodeByUUID(newNodeCopy.getUUID()))

        # Iteriere über alle übrigen Knoten des Subtrees
        for i, item in enumerate(subtreeForInsert, start=1):

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
        print("Subtree inserted")
        print("---------------")
        print(self)
        print("---------------")

    def deleteSubtree(self, subtree):
        currentNode = subtree[0]
        # Wenn der Knoten die Wurzel ist, wird der Baum gelöscht
        if currentNode.isRootNode():
            self.nodeList = []
            self.root = None
            self.treeDictionary = {}
            self.depth = 0
            del(self)

        # Wenn der Knoten nicht die Wurzel ist, wird der Teilbaum gelöscht
        else:
            # Lösche die Verknüpfung des Vorgängers mit dem alten Knoten
            previousNode = currentNode.getPreviosNode()

            # Ermittle ob der Knoten der linke oder rechte Knoten des Vorgängers ist und lösche die Verknüpfung
            if previousNode.getLeftNode().getUUID() == currentNode.getUUID():
                previousNode.setLeftNode(None)
            elif previousNode.getRightNode().getUUID() == currentNode.getUUID():
                previousNode.setRightNode(None)

            # Lösche den ersten Knoten des Subtrees aus dem Baum
            self.delNodeFromTree(currentNode)

            # Lösche den ersten Knoten aus der Knotenmenge die gelöscht werden soll
            subtree.remove(currentNode)

            # Iteriere so lang über die Knotenmenge, bis alle Knoten gelöscht wurden
            while len(subtree) > 0:

                # Lösche den Knoten der gelöscht werden soll aus Subtree und speichere ihn in currentNode
                currentNode = subtree.pop(0)

                # Lösche den Knoten aus dem Baum
                self.delNodeFromTree(currentNode)
            print("Subtree deleted")
            print("---------------")
            print(self)
            print("---------------")

    def delNodeFromTree(self, node):
        self.getTree().remove(node)
        self.treeDictionary[node.getRang()].remove(node)
        if len(self.treeDictionary[node.getRang()]) == 0:
            del (self.treeDictionary[node.getRang()])

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
                rang += 1
                nodeValue = stringAsTree[i + 1:i + 4]
                if nodeValue in self.functionalSymbols:
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList)-1]
                    previousNode.setLeftNode(currentNode)
                    currentNode.setPreviousNode(self.createList[len(self.createList)-1])
                    self.createList.append(currentNode)
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList) - 1]
                    previousNode.setLeftNode(currentNode)
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                self.updateRang(currentNode, rang)
                self.depth += 1
            elif char == ")":
                self.createList.pop()
                rang -= 1
            elif char == ",":
                nodeValue = stringAsTree[i + 1:i + 4]
                previousNode = self.createList[len(self.createList) - 1]
                if nodeValue in self.functionalSymbols:
                    currentNode = node.Node(str(nodeValue))
                    previousNode.setRightNode(currentNode)
                    currentNode.setRightNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    self.createList.append(currentNode)
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    previousNode.setRightNode(currentNode)
                self.updateRang(currentNode, rang)
            print(f"{str(i)}: Creation List: {str(self.createList)}")
        print("--------------------------------------------------")

    def updateRang(self, currentNode, rang):
        print(
            f"Node erstellt: {str(currentNode.getNodeValue())} | Vorgängerknoten: {currentNode.getPreviosNode().getNodeValue()}"
        )
        self.nodeList.append(currentNode)
        currentNode.setRang(rang)
        if rang in self.treeDictionary:
            self.treeDictionary[rang].append(currentNode)
        else:
            self.treeDictionary[rang] = [currentNode]

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
