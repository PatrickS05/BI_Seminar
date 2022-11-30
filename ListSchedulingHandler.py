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

