class ListSchedulingHandler():
    def __int__(self):
        return

    def getMakeSpan(self, array, rule):
        self.makeSpan = 0
        if rule == "SPT":
            for i in range(len(array)):
                for item in array:
                    minimum = min(item)
                    item.remove(minimum)
                    print("Minimum: " + str(minimum))
            print("-----")
        print(array)

    def getProcessingTime(self):
        operation = {"ADD": lambda x,y: x+y,
                     "SUB": lambda x,y: x-y,
                     "MUL": lambda x,y: x*y,
                     "DIV": lambda x,y: x/y}
        print(operation["ADD"](50,60))

    def getVariance(self):
        return

    def getRange(self, zahl1, zahl2):
        return abs(zahl1 - zahl2)
