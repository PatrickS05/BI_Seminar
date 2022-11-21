import geneticHandler
import node
import tree

# SUB(ADD(Y,X),MUL(X,Z))
#

def out():
    funktionalArray = ["ADD", "SUB", "MUL", "DIV"]
    terminalArray = ["X", "Y", "Z"]
    treeAsString = "(SUB||ADD|Y||ADD|X,Z||MUL|X,Z)"
    if treeAsString[1:4] in funktionalArray:
        root = node.Node(treeAsString[1:4])
        treeInstance = tree.Tree(root)
        lastNode = root
        for i in range(4, len(treeAsString)):
            if treeAsString[i] == "|" and treeAsString[i+1] == "|":
                treeNode = node.Node(str(treeAsString[i+2:i+5]))
                print("Funktionalsymbol: " + str(treeNode.getNodeValue()))
                treeInstance.addNodeToTree(treeNode)
                treeNode.setPreviousNode(lastNode)
                if not lastNode.existsLeftNode():
                    lastNode.addLeftNode(treeNode)
                else:
                    lastNode.addRightNode(treeNode)
                lastNode = treeNode
            elif treeAsString[i] == "|" and treeAsString[i-1] != "|":
                print("Terminalsymbol: " + treeAsString[i+1:i+4].replace("||", ""))
        print(str(treeInstance))
        print("Tiefe: " + str(treeInstance.getDepth()))


if __name__ == '__main__':
    out()
