import ListSchedulingHandler, evolutionOperationClass
import tree
import uuid

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
        treeInstance1 = tree.Tree()
        treeInstance1.createTree("SUB(ADD(R,V),SUB(S,V))")
        print(treeInstance1)

        treeInstance2 = tree.Tree()
        treeInstance2.createTree("ADD(MUL(R,V),MUL(S,V))")
        print(treeInstance2)

        print("--------------------------------------------------")

        #evolution = evolutionOperationClass.evolutionOperations()
        #evolution.makeEvolution([treeInstance1, treeInstance2], [[10, 21, 35, 14, 5], [17, 14, 35, 10, 25]])

        subtree = treeInstance1.getTree()[1]
        j = 0
        while j < len(subtree):
            if subtree[j].existsLeftNode():
                subtree.append(subtree[j].getLeftNode())
            if subtree[j].existsRightNode():
                subtree.append(subtree[j].getRightNode())
            j += 1

        treeInstance1.deleteSubtree(subtree)

        print(treeInstance1)
        """
        makeSpan = ListSchedulingHandler.ListSchedulingHandler()
        makeSpan.setTreeInstance(treeInstance)
        makeSpan.setArrayOfValues([[4,7,18,12,20,8], [5,6,6,7,19,23]])
        makeSpan.fillPriorityList()
        print("Priority List: " + str(makeSpan.getPriorityList()))
        print("----------------------------------------------")
        print(f"Makespan: {str(makeSpan.calculateMakeSpan())}")
        print("----------------------------------------------")
        """
        #evolution = evolutionOperationClass.evolutionOperations()
        #evolution.crossover(treeInstance1, treeInstance2)
        #print("--------------------------------------------------")
        #print(f"Mutation:")
        #evolution.mutation(treeInstance1)
        #evolution.mutation(treeInstance2)
        #print("--------------------------------------------------")
        #fitnessValues = evolution.selection([treeInstance1, treeInstance2], [[4,7,18], [5,6,6], [8,6,10]])
        #print(f"Fitness Values: {str(fitnessValues)}")
        #print("--------------------------------------------------")
    # SUB(ADD(X,Y),MUL(ADD(X,Y),Z))
    # SUB(ADD(X,Y),MUL(Y,Z))
    # [[4,5], [8,6]]

if __name__ == '__main__':
    out()
