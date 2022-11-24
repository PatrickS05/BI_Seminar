import node


class Tree:
    def __init__(self):
        self.functionalSymbols = ["ADD", "SUB", "MUL", "DIV"]
        self.terminalSymbols = ["X", "Y", "Z"]
        self.nodeList = []
        self.createList = []
    def getRootNode(self):
        return self.root

    def addNodeToTree(self, node):
        self.nodeList.append(node)

    def getTree(self):
        if self.nodeList is not None:
            return self.nodeList

    def __len__(self):
        return len(self.nodeList)

    def createTree(self, stringAsTree):
        self.root = node.Node(stringAsTree[:4])
        self.root.setToRootNode()
        self.nodeList.append(self.root)
        self.createList.append(self.root)
        for i in range(3, len(stringAsTree), 3):
            string = stringAsTree[i:i+3]
            if str(string).__contains__("("):
                pos = string.find("(")
                print(stringAsTree[i:i+3])
            else:
                print(string)

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

