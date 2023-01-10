import random, ListSchedulingHandler,copy

class evolutionOperations():
    def __init__(self):
        self.trees = []
    def makeEvolution(self, trees, ArraysOfValues):
        print("Starte Evolution")
        for i in range(5):
            print(f"{str(i)}. Generation")
            print("--------------------------------------------------")
            if i < 1: self.trees = trees
            random.shuffle(self.trees)
            print("-------------------------")
            print("CROSSOVER:")
            print("-------------------------")
            for j in range(len(self.trees) // 2):
                treeInstance1 = self.trees[j]
                treeInstance2 = self.trees[j + 1]
                self.crossover(treeInstance1, treeInstance2)
            print("-------------------------")
            print("MUTATION:")
            print("-------------------------")
            for tree in self.trees:
                self.mutation(tree)
            print("-------------------------")
            print("SELEKTION:")
            print("-------------------------")
            fitnessValues = self.selection(ArraysOfValues)
            print(f"Fitness Values: {str(fitnessValues)}")
            print("--------------------------------------------------")
        print("--------------------------------------------------")


    def crossover(self, treeInstance1, treeInstance2):
        """
            Führt einen Crossover-Algorithmus auf den gegebenen `treeInstance`-Objekten aus. Benutzt hierbei die insert-Methode der `Tree`-Klasse.

            Args:
              treeInstance1 (tree.Tree): Ein Baumobjekt, auf dem der Crossover-Algorithmus ausgeführt werden soll.
              treeInstance2 (tree.Tree): Ein Baumobjekt, auf dem der Crossover-Algorithmus ausgeführt werden soll.

            Returns: None
            """
        #self.trees.append(treeInstance1)
        #self.trees.append(treeInstance2)
        treeInstances = [copy.deepcopy(treeInstance1), copy.deepcopy(treeInstance2)]
        randomPosTree = [random.randint(1, len(treeInstances[0]) - 1), random.randint(1, len(treeInstances[1]) - 1)]
        subtrees = []
        for i in range(2):
            subtree = [treeInstances[i].getTree()[randomPosTree[i]]]
            j = 0
            while j < len(subtree):
                if subtree[j].existsLeftNode():
                    subtree.append(subtree[j].getLeftNode())
                if subtree[j].existsRightNode():
                    subtree.append(subtree[j].getRightNode())
                j += 1
            subtrees.append(subtree)
        treeInstances[0].insertSubtree(copy.deepcopy(subtrees[1]), copy.deepcopy(subtrees[0]), randomPosTree[0])
        self.trees.append(treeInstances[0])
        treeInstances[1].insertSubtree(copy.deepcopy(subtrees[0]), copy.deepcopy(subtrees[1]), randomPosTree[1])
        self.trees.append(treeInstances[1])
        print(f"Position der Subtrees: {randomPosTree}\n")
        print(f"Tree 1: {str(treeInstances[0])}")
        print(f"Tree 2: {str(treeInstances[1])}")
        print(f"Trees: {str(self.trees)}")

    def mutation(self, treeInstance):
        enable = random.random()
        string = "keine Mutation"
        if enable < 0.5:
            pos = random.randint(1, len(treeInstance) - 1)
            node = treeInstance.getTree()[pos]
            if not node.existsLeftNode() or not node.existsRightNode():
                symbol = random.choice(treeInstance.getTerminalSymbols())
            else:
                symbol = random.choice(treeInstance.getFunctionalSymbols())
            node.setNodeValue(symbol)
            print(f"Mutation an Position {pos} mit dem Symbol {str(symbol)}:")
        print(string)

    def selection(self, ArraysOfValues):
        fitnessValues = {}
        makespan = ListSchedulingHandler.ListSchedulingHandler()
        for tree in self.trees:
            makespan.setTreeInstance(tree)
            makespan.setArrayOfValues(ArraysOfValues)
            makespan.fillPriorityList()
            fitnessValues[tree] = makespan.calculateMakeSpan()
        if len(fitnessValues) > 6:
            for i in range(2):
                if i == 0:
                    self.trees = [min(fitnessValues, key=lambda fitness: fitnessValues[fitness])]
                else:
                    self.trees.append(max(fitnessValues, key=lambda fitness: fitnessValues[fitness]))
                del fitnessValues[self.trees[i]]
            for _ in range(len(fitnessValues)//2):
                choise1 = random.choice(fitnessValues.keys())
                choise2 = random.choice(fitnessValues.keys())
                self.trees.append(max(fitnessValues[choise1], fitnessValues[choise2]))

