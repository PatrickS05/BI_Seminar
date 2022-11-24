import geneticHandler
import node
import tree

# SUB(ADD(Y,X),MUL(X,Z))
#

def out():
    treeInstance = tree.Tree()
    treeInstance.createTree("SUB(ADD(X,Y),MUL(Y,Z))")


if __name__ == '__main__':
    out()
