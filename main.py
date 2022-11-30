import ListSchedulingHandler
import geneticHandler
import node
import tree

# SUB(ADD(Y,X),MUL(X,Z))
#

def out():
    treeInstance = tree.Tree()
    treeInstance.createTree("SUB(ADD(ADD(X,Y),Z))")
    #makespan = ListSchedulingHandler.ListSchedulingHandler()
    #makespan.getMakeSpan([[500,250,300],[75,62,30],[145,750,951]], "SPT")


if __name__ == '__main__':
    out()
