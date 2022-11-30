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
        return

    def getVariance(self):
        return

    def getRange(self, zahl1, zahl2):
        return abs(zahl1 - zahl2)
