import statistics
class ListSchedulingHandler():
    def __init__(self):
        self.priorityList = {}
    def getPriorityList(self):
        return self.priorityList

    def getValueFromTerminalsymbol(self, symbole, arrayOfValues, index):
        value = 0
        if symbole == "R":
            value = self.rangeValues[index]
        elif symbole == "V":
            value = self.varianzValues[index]
        elif symbole == "S":
            value = arrayOfValues[index]
        return value



    def calculatePriorityLevel(self, treeInstance, arrayOfValues, index):
        value = 0
        operations = {"ADD": lambda x, y: int(x) + int(y),
                           "SUB": lambda x, y: int(x) - int(y),
                           "MUL": lambda x, y: int(x) * int(y),
                           "DIV": lambda x, y: int(x) / int(y)}
        currentlevel = len(treeInstance.getTreeDictionary())-1
        currentlevelArray = treeInstance.getTreeDictionary()[currentlevel]
        rightNode = None
        leftNode = None
        while len(currentlevelArray) > 0:
            node = currentlevelArray[0].getPreviosNode()
            if node.hasRightNode: rightNode = node.getRightNode()
            if node.hasLeftNode: leftNode = node.getLeftNode()
            if rightNode != None and leftNode != None and node.getNodeValue() in treeInstance.getFunctionalSymbols():
                if rightNode.getNodeValue() in treeInstance.getFunctionalSymbols() and leftNode.getNodeValue() in treeInstance.getFunctionalSymbols():
                    tempValue = operations[node.getNodeValue()](rightNode.getValue(), leftNode.getValue())
                    node.setValue(operations[node.getNodeValue()](rightNode.getValue(), leftNode.getValue()))
                elif rightNode.getNodeValue() in treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in treeInstance.getFunctionalSymbols():
                    tempValue = operations[node.getNodeValue()](self.getValueFromTerminalsymbol(rightNode.getNodeValue(), arrayOfValues, index), leftNode.getValue())
                    node.setValue(operations[node.getNodeValue()](self.getValueFromTerminalsymbol(rightNode.getNodeValue(), arrayOfValues, index), leftNode.getValue()))
                elif rightNode.getNodeValue() in treeInstance.getFunctionalSymbols() and leftNode.getNodeValue() in treeInstance.getTerminalSymbols():
                    tempValue = operations[node.getNodeValue()](rightNode.getValue(), self.getValueFromTerminalsymbol(leftNode.getNodeValue(), arrayOfValues, index))
                    node.setValue(operations[node.getNodeValue()](rightNode.getValue(), self.getValueFromTerminalsymbol(leftNode.getNodeValue(), arrayOfValues, index)))
                elif rightNode.getNodeValue() in treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in treeInstance.getTerminalSymbols():
                    tempValue = operations[node.getNodeValue()](self.getValueFromTerminalsymbol(rightNode.getNodeValue(), arrayOfValues, index), self.getValueFromTerminalsymbol(leftNode.getNodeValue(), arrayOfValues, index))
                    node.setValue(operations[node.getNodeValue()](self.getValueFromTerminalsymbol(rightNode.getNodeValue(), arrayOfValues, index), self.getValueFromTerminalsymbol(leftNode.getNodeValue(), arrayOfValues, index)))
                if rightNode != None: currentlevelArray.remove(rightNode)
                if leftNode != None: currentlevelArray.remove(leftNode)
                if len(currentlevelArray) <= 0 and currentlevel >= 0:
                    currentlevel -= 1
                    currentlevelArray = treeInstance.getTreeDictionary()[currentlevel]
            else:
                print("Error")
                break
            if node.isRootNode():
                print(f"Root node value: {str(node.getValue())}")
                self.priorityList[treeInstance] = node.getValue()
                value = node.getValue()
                for node in treeInstance.getTree():
                    node.setValue(None)
                break
        return value

    def calculateRange(self, arrayOfValues):
        rangeValues = []
        for i in range(len(arrayOfValues[0])):
            tempRange = []
            for j in range(len(arrayOfValues)):
                tempRange.append(arrayOfValues[j][i])
            rangeValues.append(max(tempRange) - min(tempRange))
        return rangeValues

    def calculateVarianz(self, arrayOfValues):
        variationValues = []
        for i in range(len(arrayOfValues[0])):
            tempVariation = []
            for j in range(len(arrayOfValues)):
                tempVariation.append(arrayOfValues[j][i])
            variationValues.append(statistics.variance(tempVariation))
        return variationValues

    def fillPriorityList(self, treeInstance, arrayOfValues):
        operations = []
        for node in treeInstance.getTree():
            if node.getNodeValue() in treeInstance.getTerminalSymbols() and node.getNodeValue() not in operations:
                operations.append(node.getNodeValue())
        if "R" in operations:
            self.rangeValues = self.calculateRange(arrayOfValues)
        if "V" in operations:
            self.varianzValues = self.calculateVarianz(arrayOfValues)
        print("Operations: " + str(operations))
        for i in range(len(arrayOfValues)):
            for j in range(len(arrayOfValues[0])):
                string = str(j+1) + "," + str(i+1)
                value = self.calculatePriorityLevel(treeInstance, arrayOfValues[i], j)
                self.priorityList.update({string: value})


