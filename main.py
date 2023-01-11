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
        treeString1 = "SUB(ADD(R,DIV(R,S)),DIV(ADD(R,V),MUL(V,S)))"
        tree1valid = False
        if treeString1.count("(") == treeString1.count(")"):
            treeInstance1.createTree(treeString1)
            tree1valid = True
            print(treeInstance1)

        treeInstance2 = tree.Tree()
        treeString2 = "ADD(ADD(R,SUB(R,V)),MUL(ADD(S,R),DIV(R,S)))"
        tree2valid = False
        if treeString2.count("(") == treeString2.count(")"):
            treeInstance2.createTree(treeString2)
            tree2valid = True
            print(treeInstance2)

        print("--------------------------------------------------")

        if tree1valid and tree2valid:
            evolution = evolutionOperationClass.evolutionOperations()
            evolution.makeEvolution([treeInstance1, treeInstance2], [[10, 15, 20, 8], [17, 7, 6, 25]])
        else:
            print(f"Einer der Bäume ist ungültig!")

if __name__ == '__main__':
    out()
