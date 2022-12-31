import statistics, copy
class ListSchedulingHandler():
    def __init__(self):
        self.priorityList = {}
        self.rangeValues = []
        self.varianzValues = []
    def getPriorityList(self):
        return self.priorityList

    def setTreeInstance(self, treeInstance):
        self.treeInstance = treeInstance

    def setArrayOfValues(self, arrayOfValues):
        self.arrayOfValues = arrayOfValues

    def getValueFromTerminalsymbol(self, symbole, arrayValues, index):
        value = 0
        if symbole == "R":
            value = self.rangeValues[index]
        elif symbole == "V":
            value = self.varianzValues[index]
        elif symbole == "S":
            value = arrayValues[index]
        return value

    def calculatePriorityLevel(self, indexOfStartArray, index):
        value = 0
        currentLevelDict = copy.deepcopy(self.treeInstance.getTreeDictionary())
        operations = {"ADD": lambda x, y: float(x) + float(y),
                           "SUB": lambda x, y: float(x) - float(y),
                           "MUL": lambda x, y: float(x) * float(y),
                           "DIV": lambda x, y: float(x) / float(y)}
        currentlevel = len(self.treeInstance.getTreeDictionary())-1
        currentlevelArray = currentLevelDict[currentlevel]
        rightNode = None
        leftNode = None
        while len(currentlevelArray) > 0:
            node = currentlevelArray[0].getPreviosNode()
            if node.hasRightNode: rightNode = node.getRightNode()
            if node.hasLeftNode: leftNode = node.getLeftNode()
            if rightNode != None and leftNode != None and node.getNodeValue() in self.treeInstance.getFunctionalSymbols():
                if rightNode.getNodeValue() in self.treeInstance.getFunctionalSymbols() and leftNode.getNodeValue() in self.treeInstance.getFunctionalSymbols():
                    tempValue = operations[node.getNodeValue()](leftNode.getValue(),rightNode.getValue())
                    node.setValue(operations[node.getNodeValue()](leftNode.getValue(),rightNode.getValue()))
                elif rightNode.getNodeValue() in self.treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in self.treeInstance.getFunctionalSymbols():
                    tempValue = operations[node.getNodeValue()](leftNode.getValue(), self.getValueFromTerminalsymbol(rightNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index))
                    node.setValue(operations[node.getNodeValue()](leftNode.getValue(), self.getValueFromTerminalsymbol(rightNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index)))
                elif rightNode.getNodeValue() in self.treeInstance.getFunctionalSymbols() and leftNode.getNodeValue() in self.treeInstance.getTerminalSymbols():
                    tempValue = operations[node.getNodeValue()](self.getValueFromTerminalsymbol(leftNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index), rightNode.getValue())
                    node.setValue(operations[node.getNodeValue()](self.getValueFromTerminalsymbol(leftNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index), rightNode.getValue()))
                elif rightNode.getNodeValue() in self.treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in self.treeInstance.getTerminalSymbols():
                    valueRight = self.getValueFromTerminalsymbol(rightNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index)
                    valueLeft = self.getValueFromTerminalsymbol(leftNode.getNodeValue(), self.arrayOfValues[indexOfStartArray], index)
                    tempValue = operations[node.getNodeValue()](valueLeft, valueRight)
                    node.setValue(operations[node.getNodeValue()](valueLeft, valueRight))
                if rightNode != None: currentlevelArray.remove(rightNode)
                if leftNode != None: currentlevelArray.remove(leftNode)
                if len(currentlevelArray) <= 0 and currentlevel >= 0:
                    currentlevel -= 1
                    currentlevelArray = currentLevelDict[currentlevel]
            else:
                print("Error")
                break
            if node.isRootNode():
                print(f"Root node value: {str(node.getValue())}")
                value = node.getValue()
                for node in self.treeInstance.getTree():
                    node.setValue(None)
                break
        return value

    def calculateRange(self, arrayOfValues):
        rangeValues = []
        for i in range(len(arrayOfValues[0])):
            tempRange = [arrayOfValues[j][i] for j in range(len(arrayOfValues))]
            rangeValues.append(max(tempRange) - min(tempRange))
        return rangeValues

    def calculateVarianz(self, arrayOfValues):
        variationValues = []
        for i in range(len(arrayOfValues[0])):
            tempVariation = [arrayOfValues[j][i] for j in range(len(arrayOfValues))]
            variationValues.append(statistics.variance(tempVariation))
        return variationValues

    def fillPriorityList(self):
        operations = []
        tempDict = {}
        for node in self.treeInstance.getTree():
            if node.getNodeValue() in self.treeInstance.getTerminalSymbols() and node.getNodeValue() not in operations:
                operations.append(node.getNodeValue())
        if "R" in operations:
            self.rangeValues = self.calculateRange(self.arrayOfValues)
        if "V" in operations:
            self.varianzValues = self.calculateVarianz(self.arrayOfValues)
        print(f"Operations: {operations}")
        for i in range(len(self.arrayOfValues)):
            for j in range(len(self.arrayOfValues[0])):
                string = f"{str(j + 1)},{str(i + 1)}"
                value = self.calculatePriorityLevel(i, j)
                tempDict[string] = value
        sortedValueDict = sorted(tempDict.values(), reverse=True)
        for value in sortedValueDict:
            self.priorityList.update({key: value for key, val in tempDict.items() if val == value})
        if hasattr(self, "varianzValues"):
            print(f"Varianz: {str(self.varianzValues)}")
        if hasattr(self, "rangeValues"):
            print(f"Range: {str(self.rangeValues)}")

    # Calculate the makespan of n Jobs on m maschines
    def calculateMakeSpan(self):
        currentCount = [0] * len(self.arrayOfValues)
        jobsStart = {}
        jobsEnd = {}
        for operation in self.priorityList:
            job = int(operation.split(",")[0])
            machine = int(operation.split(",")[1])
            jobValue = self.arrayOfValues[machine-1][job-1]
            tempJobStart = currentCount[machine-1]
            tempJobEnd = tempJobStart + jobValue
            if job in jobsStart and (
                tempJobStart in range(jobsStart[job], jobsEnd[job])
                or tempJobEnd in range(jobsStart[job], jobsEnd[job])
            ):
                tempJobStart = jobsEnd[job]
                tempJobEnd = tempJobStart + jobValue
            currentCount[machine-1] = tempJobEnd
            jobsStart[job] = tempJobStart
            jobsEnd[job] = tempJobEnd
        print(f"Maschinen: {str(currentCount)}")
        print(f"Job Start: {jobsStart}")
        print(f"Job Ende: {jobsEnd}")
        return max(currentCount)
