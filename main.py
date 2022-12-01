import ListSchedulingHandler
import geneticHandler
import node
import tree

# SUB(ADD(Y,X),MUL(X,Z))
#

def out():
    treeInstance = tree.Tree()
    treeInstance.createTree("SUB(ADD(ADD(Z,Y),X),MUL(X,Z))")
    print("-------------------------")
    #node1 = treeInstance.getRootNode().getLeftNode()
    #print(node1.getNodeValue() + ": " + node1.getRightNode().getNodeValue())
    print(treeInstance.getTree())
    for item in treeInstance.getTree():
        print(item.getNodeValue())
    #makespan = ListSchedulingHandler.ListSchedulingHandler()
    #makespan.getMakeSpan([[500,250,300],[75,62,30],[145,750,951]], "SPT")
    #makespan.getProcessingTime()


if __name__ == '__main__':
    out()
