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
        treeInstance1.createTree("SUB(ADD(V,R),SUB(S,V))")
        print(treeInstance1)

        treeInstance2 = tree.Tree()
        treeInstance2.createTree("ADD(ADD(R,V),MUL(R,V))")
        print(treeInstance2)

        print("--------------------------------------------------")

        evolution = evolutionOperationClass.evolutionOperations()
        evolution.makeEvolution([treeInstance1, treeInstance2], [[10, 15], [17, 7]])

        #dict1 = {}
        #tempDict = {'2,2': 999.0, '2,1': 1007.0, '1,1': 585.75, '1,2': 592.75}
        #sortedValueDict = sorted(tempDict.values(), reverse=True)
        #for value in sortedValueDict:
            #dict1.update({key: value for key, val in tempDict.items() if val == value})

        #print(dict1)

        #makespan = ListSchedulingHandler.ListSchedulingHandler()
        #makespan.setTreeInstance(treeInstance1)
        #makespan.setArrayOfValues([[7, 6], [4, 10]])
        #makespan.fillPriorityList()

if __name__ == '__main__':
    out()
