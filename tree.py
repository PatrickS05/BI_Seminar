class Tree:
    def __init__(self, root):
        self.functionalSymbols = ["ADD", "SUB", "MUL", "DIV"]
        self.terminalSymbols = ["X", "Y", "Z"]
        self.nodeList = []

        if str(root.getNodeValue()) in self.functionalSymbols:
            self.createNode(root)
            print("Funktionalsymbol")
        elif str(root.getNodeValue()) in self.terminalSymbols:
            self.createNode(root)
            print("Terminalsymbol")
        else:
            print("Node konnte nicht erstellt werden. Der Knotenwert ist kein Funktional- oder Terminalsymbol!")

    def getRootNode(self):
        return self.root

    def addNodeToTree(self, node):
        self.nodeList.append(node)

    def getTree(self):
        if self.nodeList is not None:
            return self.nodeList

    def __len__(self):
        return int(len(self.nodeList))

    def createNode(self, root):
        self.root = root
        root.setToRootNode()
        self.nodeList.append(root)

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
        if len(self.nodeList) > 0:
            treeComplete = False
            node = self.nodeList[0]
            i = 0
            while not treeComplete:
                print(str(i) + ". -> " + str(node.getNodeValue()))
                if node.existsLeftNode():
                    i += 1
                    left = node.getLeftNode()
                    string = str(i) + ". -> " + str(left.getNodeValue())
                if node.existsRightNode():
                    right = node.getRightNode()
                    string = " | " + str(right.getNodeValue())
                if not node.existsRightNode() and i >= len(self.nodeList):
                    treeComplete = True
            return string
        else:
            return "Der Baum ist leer!"

