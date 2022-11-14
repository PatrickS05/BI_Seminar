import random


class individuumClass():
    def __init__(self):
        self.operationsList = ["ADD", "SUB", "DIV", "MULT"]
        self.operation = []

    def createOperations(self, anzahl):
        for _ in range(0, anzahl):
            self.operation.append(random.choice(self.operationsList))
        return 'Erfolgreich erschaffen!'

    def getOperation(self):
        return self.operation

    def setOperation(self, array):
        self.operation = array

    def addOperation(self, item):
        self.operation.append(item)

    def __len__(self):
        return len(self.operation)

    def __str__(self):
        return str(self.operation)
