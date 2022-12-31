import random, ListSchedulingHandler,copy
from tqdm import tqdm

class evolutionOperations():
    def __init__(self):
        self.trees = []
    def makeEvolution(self, trees, ArraysOfValues):
        print("Starte Evolution")
        for i in tqdm(range(3)):
            print(f"{str(i)}. Generation")
            print("--------------------------------------------------")
            self.trees = trees
            availableTrees = self.trees
            while len(availableTrees) > 1:
                treeInstance1 = random.choice(availableTrees)
                availableTrees.remove(treeInstance1)
                treeInstance2 = random.choice(availableTrees)
                availableTrees.remove(treeInstance2)
                self.crossover(treeInstance1, treeInstance2)
                print(f"Avialable Trees: {str(availableTrees)}")
            for tree in self.trees:
                self.mutation(tree)
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
        self.trees.append(treeInstance1)
        self.trees.append(treeInstance2)
        treeInstances = [copy.deepcopy(treeInstance1), copy.deepcopy(treeInstance2)]
        randomPosTree = [random.randint(1, len(treeInstances[0]) - 1), random.randint(1, len(treeInstances[1]) - 1)]
        subtrees = []
        for i in range(2):
            subtree = [treeInstances[i].getTree()[randomPosTree[i]]]
            j = 0
            while j < len(subtree):
                if subtree[j].getLeftNode() is not None and subtree[j].existsLeftNode():
                    subtree.append(subtree[j].getLeftNode())
                if subtree[j].existsRightNode() and subtree[j].getLeftNode() is not None:
                    subtree.append(subtree[j].getRightNode())
                j += 1
            subtrees.append(subtree)
        oldNodeCopy2 = copy.deepcopy(treeInstances[1].getTree()[randomPosTree[1]])
        treeInstances[0].insertSubtree(subtrees[1], subtrees[1][0], randomPosTree[0])
        treeInstances[1].insertSubtree(subtrees[0], subtrees[0][0], randomPosTree[1], oldNodeCopy2, secoundTree=True)
        self.trees.append(treeInstances[0])
        self.trees.append(treeInstances[1])
        print(f"Position der Subtrees: {str(randomPosTree)}\n")
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
            string = f"Mutation an Position {pos} mit dem Symbol {str(symbol)}"
            print(treeInstance)
        print(string)

    def selection(self, ArraysOfValues):
        fitnessValues = {}
        makespan = ListSchedulingHandler.ListSchedulingHandler()
        for tree in self.trees:
            makespan.setTreeInstance(tree)
            makespan.setArrayOfValues(ArraysOfValues)
            makespan.fillPriorityList()
            fitnessValues[tree] = makespan.calculateMakeSpan()
        return fitnessValues

    def getFitnessValue(self, treeInstance, arraysOfValues):
        makeSpan = ListSchedulingHandler.ListSchedulingHandler()
        makeSpan.setTreeInstance(treeInstance)
        makeSpan.setArrayOfValues(arraysOfValues)
        makeSpan.fillPriorityList()
        print(f"Priority List: {str(makeSpan.getPriorityList())}")
        print("----------------------------------------------")
        print(f"Makespan: {str(makeSpan.calculateMakeSpan())}")
        print("----------------------------------------------")


