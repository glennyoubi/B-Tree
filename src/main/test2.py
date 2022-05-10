from Node import *
from Btree import *
import time
if __name__ == '__main__':
    print("TEST2 PY")
    root = Node([], [], None, True)
    arbre = Btree(6, 11, root)
    print("CARACTERISTOQUES DE L'ARBRE : L = "+str(arbre.min_sons)+" U = "+str(arbre.max_sons)+" !")
    l1 = [i for i in range(10,5001,10)]
    l2 = [v for v in range(5,5000,5)]
    print(l1)
    print(l2)
    for i in l1:
        print("Insertion de "+str(i)+"")
        arbre.insert(i)
        print("Tree")
        arbre.display_tree(arbre.root)
        #time.sleep(0.5)
    for i in l1:
        print("Insertion de "+str(i)+"")
        arbre.insert(i)
        print("Tree")
        arbre.display_tree(arbre.root)
        #time.sleep(0.5)
    print()
    print("#------------------------- ARBRE FINAL --------------------------#")
    print()
    time.sleep(1.0)
    arbre.display_tree(arbre.root)