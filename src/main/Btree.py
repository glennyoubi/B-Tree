import math

from Node import *


class Btree:
    """
    Représentation d'un arbre B.
    """

    def __init__(self, l, u, root):
        """
        Crée un arbre B d'ordre l-1 en initialisant l'arbre avec la racine
        root. Initialise à vide deux listes leaf_nodes et nodes.
        La liste leaf_nodes contiendra les feuilles de l'abre.
        la liste nodes contiendra les noeuds internes de l'arbre.
        :param l: Nombres fils minimun pour un noeud interne de l'arbre.
        :param u: Nombres fils maximun pour un noeud interne de l'arbre.
        :param root: Racine mentionnée à la création de l'arbre.
        """
        self.min_sons = l
        self.max_sons = u
        self.min_keys = l - 1
        self.max_keys = u - 1
        self.leaf_nodes = list()  # Liste contenant toutes les feuilles.
        self.nodes = list()  # Liste contenant tous les noeuds internes.
        self.root = root
        if len(self.root.sons) == 0:
            self.set_leaf(self.root)

    def set_leaf(self, node):
        """
        Défini un noeud en tant que feuille .En Ajoutant le noeud passé en paramètre 
        dans la liste des feuilles de l'arbre et met l'attribut leaf du noeud à true.
        :param node: Node, Le noeud à ajouter à la liste.
        :return: Ne retourne rien, 
        """
        node.leaf = True
        self.leaf_nodes.append(node)

    def set_no_leaf(self, node):
        """
        Retire le noeud passé en paramètre dans la liste des feuilles de l'arbre et
        met l'attribut leaf du noeud à false.
        :param node: Node, Le noeud à ajouter à la liste.
        :return:
        """
        node.leaf = False
        if node in self.leaf_nodes:
            self.leaf_nodes.remove(node)
        self.nodes.append(node)

    def leaf_to_node_level(self, node):
        """
        Prends une feuille en paramètre et calcule sa profondeur en calculant
        son nombre d'ascendants.
        :param node: Neoud pour lequel on calcule la hauteur.
        :return: La profondeur de la feuille.
        """
        if node == self.root:
                return 0
        else:
            return self.leaf_to_node_level(node.parent) + 1

    def check_leaf_same_height(self, check):
        """
        Vérifie si toutes les feuilles de l'arbre sont à la même pronfonduer.
        :param check: Hauteur de l'arbre. Entier utilisé pour vérifier la hauteur.
        :return: Booléen. True si toutes les feuilles sont à la même profondeur , False sinon.
        """
        found = True
        checking_len = 0
        while found and checking_len < len(self.leaf_nodes):
            for i in self.leaf_nodes:
                checking_leaf = self.leaf_to_node_level(i)
                if checking_leaf != check:
                    found = False
                checking_len += 1
        return found
    
    def check_keys_per_node(self):
        """
        Vérifie si tous les noeuds interne de l'arbre on un nombre de clés de valide.
        """
        checking = True
        i = 0
        for n in self.nodes:
            if not self.node_is_valid(n):
                self.nodes.remove(n)
        while i < len(self.nodes) and checking:
            if self.max_keys < len(self.nodes[i].keys) or len(self.nodes[i].keys) < self.min_keys:
                found = False 
            i += 1
        return checking

    def est_ArbreB(self):
        """
        Vérifie si un arbre respecte les conditions pour être un arbre B.
        Vérifie si les feuilles sont à la même profondeur.
        Vérifie si chaque noeud respecte le nombre de fils maximale et minimale de l'arbre.
        Vérifie si
        :return: Bool si il s'agit d'un arbre B et faux sinon.
        """
        hauteur_arbre = self.root.hauteur()
        leaf_at_the_same_level_check = self.check_leaf_same_height(hauteur_arbre)
        checking_keys_per_node = self.check_keys_per_node()
        return leaf_at_the_same_level_check and checking_keys_per_node

    def btree_search(self, value, node=None):
        """
        Rechercher la valeur "value" dans l'arbre, en vérifiant à chaque étape si
        la "value" est dans le noeud passer en paramètre de la fonction à la fonction rechercher dans le noeud.
        :param value: Value to search.
        :param node: Starting node for the research
        :return: Boolean, True if the value is in the B-Tree and False if not.
        """
        if node is None:
            node = self.root
        if node.search_in_node(value):
            return True
        elif node.is_leaf():
            return False
        elif node.keys[0] > value:
            return self.btree_search(value, node.sons[0])
        elif value > node.keys[len(node.keys)- 1]:
            return self.btree_search(value, node.sons[len(node.sons) - 1])
        else:
            for i in range(0, (len(node.keys)) - 1):
                if node.keys[i] < value < node.keys[i + 1]:
                    return self.btree_search(value, node.sons[i + 1])

    def node_is_valid(self, node):
        """
        Vérifie si un noeud est valide. Pour faire cela on vérifie que le nombre de clés
        contenues dans le noeud est inférieur ou égale au nombre de clés maximales acceptées
        pour un noeud.
        :param node: Noeud sur lequel la vérification s'effectue.
        :return: Bool True si le noeud est valide, false
        """
        return len(node.keys) <= self.max_keys
    
    def node_is_valid_after_deletion(self,node):
        """
        Vérifie si un noeud est valide après qu'on y ait supprimer une valeur. 
        Pour faire cela on vérifie que le nombre de clés
        contenues dans le noeud est supérieur ou égale au nombre de clés minimales acceptées
        pour un noeud.
        :param node: Noeud sur lequel la vérification s'effectue.
        :return: Bool True si le noeud est valide, false
        """
        return len(node.keys) >= self.min_keys

    def get_node_to_insert(self, value, node):
        """
        Retourne le nœud dans lequel la valeur doit être insérée.
        :param value: int, the value to insert.
        :param node: Node, The node from which we search the right node to insert the keys
        :return: Node where we must insert the value.
        """
        if node.is_leaf():
            return node
        else:
            i = 0
            while i < (len(node.keys)) and value > node.keys[i]:
                i += 1
            return self.get_node_to_insert(value, node.sons[i])
    
    def get_node_to_delete(self, value, node):
        """
        Retourne le nœud dans lequel la valeur doit être supprimer.

        :param value: int, the value to insert.
        :param node: Node, The node from which we search the right node to insert the keys
        :return: Node where we must insert the value.
        """
        if node == self.root:
            if node.search_in_node(value):
                return node
        elif node.is_leaf():
            if node.search_in_node(value):
                return node
            else:
                return None
        else:
            i = 0
            while i < (len(node.keys)) and value > node.keys[i]:
                i += 1
            return self.get_node_to_delete(value, node.sons[i])
        

    def split_node(self, node):
        """
        Divise un noeud en 3 noeud dont l'un est le père des deux autres. Pour effectuer la division
        on récupère la valeur médiane du noeud passé en paramètre. Les valeurs qui précèdent la valeur médiane
        sont ajoutés comme clé au nouveau noeud fils gauche.
        Les valeurs qui succèdent la valeur médiane sont ajoutés comme clé au nouveau noeud fils droits.
        Ensuite on gère la parenté en précisant aux fils gauche et droit que leur parent est le 3ème noeud créé. 
        :param node: Noeud à diviser en 3.
        :return: Le nouveau noeud parent avec ses fils gauche et droit.
        """
        middle_index = len(node.keys) // 2  # index de la valeur médiane
        i = 0
        # taking keys
        keys_left_son = []
        keys_right_son = []
        while i < middle_index:
            keys_left_son.append(node.keys[i])
            i += 1
        b = middle_index + 1
        while b < (len(node.keys)):
            keys_right_son.append(node.keys[b])
            b += 1
        # taking sons
        middle_child_ind = len(node.sons) // 2
        left_sons = node.sons[:middle_child_ind]
        right_sons = node.sons[middle_child_ind:]
        # We create the 3 new nodes
        left_son = Node(keys_left_son, left_sons, None, False)
        right_son = Node(keys_right_son, right_sons, None, False)
        new_parent = Node([node.keys[middle_index]], [left_son, right_son], None, False)
        # Handle relationship
        left_son.parent = new_parent
        right_son.parent = new_parent
        for l_s in left_sons:
            l_s.parent = left_son
        for r_s in right_sons:
            r_s.parent = right_son
        if len(left_son.sons) > 0:
            self.set_no_leaf(left_son)
        else:
            self.set_leaf(left_son)
        if len(right_son.sons) > 0:
            self.set_no_leaf(right_son)
        else:
            self.set_leaf(right_son)
        return new_parent

    def balance(self, node):
        """
        Équilibre l'arbre à partir du noeud passé en paramètre. Cette fonction est appelée 
        sur un noued invalide, elle le divise en 3 avec la fonction split_node.
        Et traite les cas si en vérifiant si le neoud divisé avait un parent ou non.
        :param node: Node à équilobre.
        :return: Renvoie le nouveau noeud parent.
        """
        parent = node.parent
        new_parent = self.split_node(node)
        left_son = new_parent.sons[0]
        right_son = new_parent.sons[1]
        if parent is not None:
            index_where_added = parent.insert_value_in_node(
            new_parent.keys[0])  # On ajoute la valeur de new parent dans
            # le noeud parent
            parent.sons.remove(node) # On rétire l'ancien fils du noeud parent.
            # On rajoute les fils de new parent au parent dans le noeud parent. 
            parent.sons.insert(index_where_added, left_son)
            parent.sons.insert(index_where_added + 1, right_son)
            # On modifie le parent des noeud ajoutés à la liste sons du noeud parent.
            left_son.parent = parent
            right_son.parent = parent
            # On vérfie si le noeud parent est valide.
            if not self.node_is_valid(parent):
                # Si le noeud n'est pas valide on l'équilibre.
                self.balance(parent)
            else:
                return parent
        else:
            self.root = new_parent
            return new_parent

    def insert(self, value, node=None):
        """
        Insèrer la valeur "value" passer en paramètre dans l'arbre.
        :param value: Int, valeur à ajouter dans l'arbre.
        :param node: Node, optionnel noeud à partir duquel l'ajout est réalisée.
        :return: Bool, True si la valeur a pu être ajouter dans l'arbre. False, sinon.
        """
        if self.btree_search(value):
            print("La valeur est déjà dans l'arbre.")
            return False
        node_insert = self.get_node_to_insert(value, self.root)  # Node where we will insert the value.
        node_insert.insert_value_in_node(value)
        if not self.node_is_valid(node_insert):
            self.balance(node_insert)
            self.leaf_nodes.remove(node_insert)
            return True
        else:
            return True

    def display_tree(self, node, level=0):
        """
        Affiche l'arbre par noeud et par niveau. Chaque noeud est affiché en précisant à 
        sa suite son parent si il en a. Sous la forme (exemple): 
        "Level 0  |Noeud|  fils de -> [Noeud parent]".
        :param node: Noeud à partir du quel l'affichage sera réalisée.
        :param level: Niveau du noeud dans l'arbre.
        :return: Affiche l'arbre sur la sortie standard.
        """
        print("Level ", level, end="    |")
        for i in range(len(node.keys)):
            if i == len(node.keys) - 1:
                if node.parent is not None:
                    print(node.keys[i], end="|   fils de -> " + str(node.parent.keys) + "")
                else:
                    print(node.keys[i], end="|")
            else:
                print(node.keys[i], end=",")
        print()
        level += 1
        if len(node.sons) > 0:
            for i in node.sons:
                self.display_tree(i, level)
    
    def get_type_of_deletion(node):
        """
        Vérifie si le noeud dans lequelm on effectue la suppresion est la racine de l'arbre,
        un noeud interne ou une feuille de l'arbre.

        :param node: node, noeud dont on vérifie le type.
        :return: int, 0 si le noeud passé en paramètre est la racine de l'arbre,
        1 si il s'agit d'un noeud interne et 2 si il s'agit d'une feuille de l'arbre.
        """
        if (node==self.root):
            return 0
        elif (node.leaf == True):
            return 2
        else:
            return 1
    
    def delete(self,value):
        """
        Supprime une valeur de l'arbre rééquilibre selon les necessistés
        afin de respecter la structure d'un arbre B.

        :param value: Int, valeur à supprimer de l'arbre.
        :return: Bool, True si la valeur a pu être retirer, False sinon.
        """
        if not self.btree_search(value):
            print("CETTE VALEUR N'EST PAS PRESENTE DANS L'ARBRE.")
            return False
        node_delete = self.get_node_to_delete(self,value,arbre.root)
        type_of_deletion = self.get_type_of_deletion(node_delete)
        if(type_of_deletion == 0):
            self.delete_in_root(value)
        elif(type_of_deletion == 2):
            self.delete_in_leaf(value)
        else:
            self.delete_in_internal_node(value)
    
    def delete_in_root(value):
        """
        Supprime la valeur passée en paramètre de la racine de l'arbre et l'équilibre si necessaire.
        """
        pass

    def delete_in_leaf(value):
        """
        Supprime la valeur passée en paramètre d'une feuille de l'arbre et l'équilibre si necessaire.
        """
        pass

    def delete_in_internal_node(value):
        """
        Supprime la valeur passée en paramètre d'un noeud interne de l'arbre et l'équilibre si necessaire.
        """
        pass



if __name__ == '__main__':
    root = Node([], [], None, True)
    arbre = Btree(2, 3, root)
    l = [i for i in range(1, 21)]
    #l =[20, 22, 24, 26, 28, 30, 32, 34, 36, 7, 9, 11, 13]
    #l = [4, 6, 14, 10, 2, 5]
    for i in l:
        print("Insertion de "+str(i)+"")
        arbre.insert(i)
    for i in l:
        print("Recherche de "+str(i)+"")
        booll = arbre.btree_search(i)
        print(booll)
    arbre.display_tree(arbre.root)
    print("Recherche de 45")
    bool2 = arbre.btree_search(45)
    print(bool2)
    print("Test est arbre B")
    bool3 = arbre.est_ArbreB()
    print(bool3)
