class ListSchedulingHandler():
    def __int__(self):
        self.priorityList = {}

    def calculatePriorityLevel(self, treeInstance):
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
                    value = operations[node.getNodeValue()](rightNode.getValue(), leftNode.getValue())
                    node.setValue(operations[node.getNodeValue()](rightNode.getValue(), leftNode.getValue()))
                elif rightNode.getNodeValue() in treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in treeInstance.getFunctionalSymbols():
                    value = operations[node.getNodeValue()](rightNode.getNodeValue(), leftNode.getValue())
                    node.setValue(operations[node.getNodeValue()](rightNode.getNodeValue(), leftNode.getValue()))
                elif rightNode.getNodeValue() in treeInstance.getFunctionalSymbols() and leftNode.getNodeValue() in treeInstance.getTerminalSymbols():
                    value = operations[node.getNodeValue()](rightNode.getValue(), leftNode.getNodeValue())
                    node.setValue(operations[node.getNodeValue()](rightNode.getValue(), leftNode.getNodeValue()))
                elif rightNode.getNodeValue() in treeInstance.getTerminalSymbols() and leftNode.getNodeValue() in treeInstance.getTerminalSymbols():
                    value = operations[node.getNodeValue()](rightNode.getNodeValue(), leftNode.getNodeValue())
                    node.setValue(operations[node.getNodeValue()](rightNode.getNodeValue(), leftNode.getNodeValue()))
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
                for node in treeInstance.getTree():
                    node.setValue(None)
                break

