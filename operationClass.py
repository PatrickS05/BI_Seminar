import random


class operations():
    def __init__(self):
        self.operationsList = ["ADD", "SUB", "DIV", "MULT"]
    def crossover(self, indi1, indi2):
        childs = [[], []]

        for i in range(0,3):
            childs[0].append(indi1[i])
            childs[1].append(indi2[i])
        for i in range(3,6):
            childs[0].append(indi2[i])
            childs[1].append(indi1[i])
        return childs

    def mutation(self, indi, anzahl):
        enable = random.random()
        string = "keine Mutation"
        if enable < 0.5:
            string = str(indi) + " -> "
            pos = random.randint(0, len(indi) - 1)
            indi[pos] = random.choice(self.operationsList)
            string += str(indi)
        print(str(anzahl) + ". " + string)
        return indi

    def selection(self, individuums, childs):
        for child in range(len(childs)):        #bekommt keine child zurück
            pos = random.randint(0, len(childs))
            individuum = list(individuums.keys())[pos]
            print(individuum)
            #if (childs[child] < individuum.get)

    def getFitnessValue(self, indi):
        self.fitness = 0
        if "ADD" in indi:
            self.fitness += (indi.count("ADD")*10)
        if "SUB" in indi:
            self.fitness -= indi.count("SUB")
        if "MULT" in indi:
            for _ in range(indi.count("MULT")):
                self.fitness *= 2
        if "DIV" in indi:
            for _ in range(indi.count("MULT")):
                self.fitness /= 2
        return int(self.fitness)
