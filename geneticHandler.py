import evolutionOperationClass

class geneticHandler():
    def __init__(self, anzahl, anzahlOperation):
        self.op = evolutionOperationClass.evolutionOperations()
        self.individuums = {}
        self.childs = {}

        self.initialIndividuums(anzahl, anzahlOperation)
        self.crossoverIndividuums()
        self.mutationIndividuum()
        self.selectionIndividuum()

    def initialIndividuums(self, anzahl, anzahlOperation):
        for _ in range(anzahl):
            indi = individuum.individuumClass()
            indi.createOperations(anzahlOperation)
            print(indi)
            self.individuums[indi] = self.op.getFitnessValue(indi.getOperation())
        print(str(self.individuums) + "\n")
        print(f"{list(self.individuums.keys())[0]} -> {list(self.individuums.keys())[0].getOperation()}")
        print(f"{list(self.individuums.keys())[1]} -> {list(self.individuums.keys())[1].getOperation()}")

    def crossoverIndividuums(self):
        for i in range(0, len(self.individuums), 2):
            child = self.op.crossover(list(self.individuums.keys())[i].getOperation(), list(self.individuums.keys())[i+1].getOperation())
            print(f"{str(i)}. Kind:{str(child)}")
            childIndi1 = individuum.individuumClass()
            childIndi2 = individuum.individuumClass()
            childIndi1.setOperation(list(child[0]))
            childIndi2.setOperation(list(child[1]))
            self.childs[childIndi1] = self.op.getFitnessValue(child[0])
            self.childs[childIndi2] = self.op.getFitnessValue(child[1])
        print("\nKinder: " + str(self.childs))

    def mutationIndividuum(self):
        for i, item in enumerate(list(self.childs.keys())):
            self.op.mutation(item.getOperation(), i)

    def selectionIndividuum(self):
        self.op.selection(self.individuums, self.childs)
    def getIndividuums(self):
        return self.individuums
