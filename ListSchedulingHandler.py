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
        self.terminal = self.treeInstance.getTerminalSymbols()
        self.functional = self.treeInstance.getFunctionalSymbols()

    def setArrayOfValues(self, arrayOfValues):
        self.arrayOfValues = arrayOfValues

    def getValueFromTerminalsymbol(self, symbole, arrayValues, index):
        valueOfSymbol = 0
        if symbole == "R":
            valueOfSymbol = self.rangeValues[index]
        elif symbole == "V":
            valueOfSymbol = self.varianzValues[index]
        elif symbole == "S":
            valueOfSymbol = arrayValues[index]
        return valueOfSymbol

    def calculatePriorityLevel(self, indexOfMaschine, indexOfJob):

        # Lege die Variable an, um dir den Wert zu merken
        global currentNode
        value = 0

        # Erstelle eine Kopie des Baumes
        currentDict = copy.deepcopy(self.treeInstance.getTreeDictionary())

        # Definiere die Funktionen der Funktionalsymbole
        operations = {"ADD": lambda x, y: float(x if x is not None else 0) + float(y if y is not None else 0),
                      "SUB": lambda x, y: float(x if x is not None else 0) - float(y if y is not None else 0),
                      "MUL": lambda x, y: float(x if x is not None else 1) * float(y if y is not None else 1),
                      "DIV": lambda x, y: float(x if x is not None else 1) / (float(y if y is not None else 1) + 0.001)}

        # Gehe alle Ebenen des Baumes durch
        for level in range(len(currentDict)-2, -1, -1):

            # Gehe alle Knoten der Ebene durch
            for node in currentDict[level]:
                if node.getNodeValue() in self.functional:
                    currentNode = node
                    leftNode = node.getLeftNode()
                    rightNode = node.getRightNode()
                    if leftNode.getNodeValue() in self.functional and rightNode.getNodeValue() in self.functional:
                        node.setValue(operations[node.getNodeValue()](leftNode.getValue(), rightNode.getValue()))
                    elif leftNode.getNodeValue() in self.functional and rightNode.getNodeValue() in self.terminal:
                        node.setValue(operations[node.getNodeValue()](leftNode.getValue(),self.getValueFromTerminalsymbol(rightNode.getNodeValue(),self.arrayOfValues[indexOfMaschine],indexOfJob)))
                    elif leftNode.getNodeValue() in self.terminal and rightNode.getNodeValue() in self.functional:
                        node.setValue(operations[node.getNodeValue()](
                            self.getValueFromTerminalsymbol(leftNode.getNodeValue(),self.arrayOfValues[indexOfMaschine], indexOfJob),rightNode.getValue()))
                    elif leftNode.getNodeValue() in self.terminal and rightNode.getNodeValue() in self.terminal:
                        node.setValue(operations[node.getNodeValue()](self.getValueFromTerminalsymbol(leftNode.getNodeValue(),self.arrayOfValues[indexOfMaschine], indexOfJob),self.getValueFromTerminalsymbol(rightNode.getNodeValue(),self.arrayOfValues[indexOfMaschine], indexOfJob)))
            value = currentNode.getValue()

            # Setze alle Werte der Knoten auf None
            for item in self.treeInstance.getTree():
                item.setValue(None)
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
        if hasattr(self, "varianzValues"):
            print(f"Varianz: {str(self.varianzValues)}")
        if hasattr(self, "rangeValues"):
            print(f"Range: {str(self.rangeValues)}")
        valueString = ""
        for machine in range(len(self.arrayOfValues)):
            for job in range(len(self.arrayOfValues[0])):
                operationString = f"{str(job + 1)},{str(machine + 1)}"
                value = self.calculatePriorityLevel(machine, job)
                tempDict[operationString] = value
                valueString += f"{operationString}: {str(value)}; "
        #print(valueString)
        sortedValueDict = sorted(tempDict.values(), reverse=True)
        for value in sortedValueDict:
            self.priorityList.update({key: value for key, val in tempDict.items() if val == value})
        tempDict.clear()
        print(f"Priority List: {str(self.getPriorityList())}")

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
        print(f"----> Maschinen: {str(currentCount)}")
        self.priorityList = {}
        return max(currentCount)
