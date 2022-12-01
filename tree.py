import node


class Tree:
    def __init__(self):
        self.functionalSymbols = ["ADD", "SUB", "MUL", "DIV"]
        self.terminalSymbols = ["X", "Y", "Z"]
        self.nodeList = []
        self.createList = []
    def getRootNode(self):
        return self.root

    def getTree(self):
        if self.nodeList is not None:
            return self.nodeList

    def __len__(self):
        return len(self.nodeList)

    # SUB(ADD(Y,X),MUL(X,Z))
    def createTree(self, stringAsTree):
        self.root = node.Node(stringAsTree[:3])
        self.root.setToRootNode()
        self.nodeList.append(self.root)
        self.createList.append(self.root)
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
                else:
                    nodeValue = stringAsTree[i + 1]
                    currentNode = node.Node(str(nodeValue))
                    currentNode.addRightNode(self.createList[len(self.createList) - 1])
                    currentNode.setPreviousNode(self.createList[len(self.createList) - 1])
                    print("Node erstellt: " + str(
                        currentNode.getNodeValue()) + " | Vorgängerknoten: " + currentNode.getPreviosNode().getNodeValue())
                    self.nodeList.append(currentNode)
            elif char == ")":
                self.createList.pop()
            print(str(i) + ": Creation List: " + str(self.createList))

    def getDepth(self):
        depth = 0
        node = self.nodeList[0]
        for i in range(len(self.nodeList)):
            if node.existsLeftNode():
                node = node.getLeftNode()
                depth += 1
            else:
                break
        return depth

    def __str__(self):
        if len(self.nodeList) <= 0:
            return "Der Baum ist leer!"
        treeComplete = False
        node = self.nodeList[0]
        i = 0
        while not treeComplete:
            print(f"{str(i)}. -> {str(node.getNodeValue())}")
            if node.existsLeftNode():
                i += 1
                left = node.getLeftNode()
                string = f"{i}. -> {str(left.getNodeValue())}"
            if node.existsRightNode():
                right = node.getRightNode()
                string = f" | {str(right.getNodeValue())}"
            if not node.existsRightNode() and i >= len(self.nodeList):
                treeComplete = True
        return string

