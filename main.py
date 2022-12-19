import ListSchedulingHandler
import tree

def out():
    quitAction = "0"
    decision = 0
    if decision == 1:
        trees = []
        while quitAction == "0":
            print("Bitte wähle eine Aktion aus!")
            action = input(
                "1 - Beenden, 2 - Baum erstellen, 3 - Baumdetails anzeigen, 4 - Baum modifizieren\nAktion: ")
            if action == "1":
                quitAction = "1"
                print("--------------------------------------------------")
            elif action == "2":
                treeString = input("Gib deinen Baum als String ein!\n Baum: ")
                # check if the TreeString is valid
                if treeString.count("(") == treeString.count(")"):
                    treeInstance = tree.Tree()
                    treeInstance.createTree(treeString)
                    trees.append(treeInstance)
                    print("Baum erfolgreich erstellt!")
                else:
                    print("Der Baum ist ungültig!")
                print("--------------------------------------------------")
            elif action == "3":
                if trees:
                    selectedTree = input(f"Wähle ein Baum aus der Liste: von 0 bis {str(len(trees) - 1)}" + "\nBaum: ")

                    currentTree = trees[int(selectedTree)]
                    print(currentTree)
                    print(f"Länge: {len(currentTree)}")
                    print(f"Tiefe: {str(currentTree.getDepth())}")
                    print(f"Dictionary: {str(currentTree.getTreeDictionary())}")
                    print("--------------------------------------------------")
                else:
                    print("Es wurden noch keine Bäume erstellt!")
    else:
        treeInstance = tree.Tree()
        treeInstance.createTree("SUB(ADD(2,3),MUL(ADD(4,2),6))")

        print(treeInstance)
        print(treeInstance.getTreeDictionary())
        print(treeInstance.getDepth())
        print(len(treeInstance))

        makeSpan = ListSchedulingHandler.ListSchedulingHandler()
        makeSpan.calculatePriorityLevel(treeInstance)

    # SUB(ADD(X,Y),MUL(ADD(X,Y),Z))
    # SUB(ADD(X,Y),MUL(Y,Z))

    #makespan = ListSchedulingHandler.ListSchedulingHandler()
    #makespan.getMakeSpan([[500,250,300],[75,62,30],[145,750,951]], "SPT")
    #makespan.getProcessingTime()


if __name__ == '__main__':
    out()
