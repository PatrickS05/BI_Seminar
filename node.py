import uuid

class Node():
    def __init__(self, value):
        self.nodeValue = value
        self.leftNode = None
        self.rightNode = None
        self.hasRightNode = False
        self.hasLeftNode = False
        self.isRoot = False
        self.previousNode = None
        self.rang = -1
        self.value = None
        self.UUID = uuid.uuid1()

    def setValue(self, value):
        self.value = value

    def setNodeValue(self, value):
        self.nodeValue = value

    def getValue(self):
        return self.value

    def getLeftNode(self):
        return self.leftNode

    def isRootNode(self):
        return self.isRoot

    def getRightNode(self):
        return self.rightNode

    def getNodeValue(self):
        return self.nodeValue

    def existsRightNode(self):
        return self.hasRightNode

    def existsLeftNode(self):
        return self.hasLeftNode

    def getPreviosNode(self):
        return self.previousNode

    def setLeftNode(self, node):
        self.leftNode = node
        self.hasLeftNode = True

    def setRightNode(self, node):
        self.rightNode = node
        self.hasRightNode = True

    def deleteLeftNode(self):
        self.leftNode = None

    def deleteRightNode(self):
        self.rightNode = None

    def setToRootNode(self):
        self.isRoot = True

    def setPreviousNode(self, node):
        self.previousNode = node

    def getRang(self):
        return self.rang

    def setRang(self, rang):
        self.rang = rang

    def getUUID(self):
        return self.UUID

    def generateUUID(self):
        self.UUID = uuid.uuid1()
