
class node():
    def __int__(self):
        self.nodeValue = ""
        self.leftNode = node()
        self.rightNode = node()
        self.hasRightNode = False
        self.hasLeftNode = False
        self.isRootNode = False
        self.previousNode = node()

    def getLeftNode(self):
        return self.leftNode

    def getRightNode(self):
        return self.rightNode

    def getNodeValue(self):
        return self.nodeValue

    def hasRightNode(self):
        return self.hasRightNode

    def hasLeftNode(self):
        return self.hasLeftNode

    def getPreviosNode(self):
        return self.previousNode


