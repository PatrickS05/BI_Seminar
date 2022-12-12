import node


class Tree:
    def __init__(self):
        self.functionalSymbols = ["ADD", "SUB", "MUL", "DIV"]
        self.terminalSymbols = ["X", "Y", "Z"]
        self.nodeList = []
        self.createList = []
        self.depth = 0

    def getRootNode(self):
        return self.root

    def getTree(self):
        if self.nodeList is not None:
            return self.nodeList

    def __len__(self):
        return len(self.nodeList)

    def createTree(self, stringAsTree):
        rang = 0
        self.root = node.Node(stringAsTree[:3])
        self.root.setToRootNode()
        self.nodeList.append(self.root)
        self.createList.append(self.root)
        self.root.setRang(0)
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
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList) - 1]
                    previousNode.addLeftNode(currentNode)
                    currentNode.addLeftNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    rang += 1
                    self.depth +=1
                    currentNode.setRang(rang)
            elif char == ",":
                nodeValue = stringAsTree[i + 1:i + 4]
                if nodeValue in self.functionalSymbols:
                    currentNode = node.Node(str(nodeValue))
                    previousNode = self.createList[len(self.createList) - 1]
                    previousNode.addRightNode(currentNode)
                    currentNode.addRightNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    self.createList.append(currentNode)
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    currentNode.setRang(rang)
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    #currentNode.addRightNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
                    currentNode.setRang(rang)
            elif char == ")":
                self.createList.pop()
                rang -= 1
            print(str(i) + ": Creation List: " + str(self.createList))

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

