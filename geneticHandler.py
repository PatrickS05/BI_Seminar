import individuum
import operationClass


class geneticHandler():
    def __init__(self):
        self.operation = operationClass.operations("test")
        self.individuum1 = individuum.individuumClass()
        self.individuum1.createOperations(7)
        print(self.individuum1)
        self.individuum1.addOperation("SUB")
        print(self.individuum1)
