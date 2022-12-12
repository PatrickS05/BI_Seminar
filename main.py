import ListSchedulingHandler
import geneticHandler
import node
import tree

def out():
    treeInstance = tree.Tree()
    treeInstance.createTree("SUB(ADD(X,Y),MUL(ADD(X,Y),Z))")
    print("-------------------------")
    print(treeInstance)
    print("Anzahl Knoten: " + str(len(treeInstance)))
    print("Tiefe: " + str(treeInstance.getDepth()))
    print("-------------------------")
    #makespan = ListSchedulingHandler.ListSchedulingHandler()
    #makespan.getMakeSpan([[500,250,300],[75,62,30],[145,750,951]], "SPT")
    #makespan.getProcessingTime()


if __name__ == '__main__':
    out()
