from os.path import abspath


class Node:
    """
    Représente un noeud d'un arbre B.
    """

    def __init__(self,keys, sons=[], parent=None, leaf=False):
        """
        Construits un noeud constitué d'une liste de clés, une liste de fils.
        Un attribut parent stockant le noeud parent du noeud crée, si ce noeud a un parent
        et None si il n'en a pas. Un attribut leaf qui vaut True si le noeud est feuille
        de l'arbre dans lequel il se trouve et False sinon. 
        :param keys: La liste contenant les clés du noeud.
        :param sons: La liste contenant les fils du noeud.
        :param parent: Le noeud parent du noeud créé.
        :param leaf: Booléen précisant si le neoud est une feuille ou non.
        """
        self.keys = keys
        self.sons = sons
        self.parent = parent
        self.leaf = leaf
        self.number_of_keys = 0

    def is_leaf(self):
        """
        Vérifie si le noeud est une feuille ou non en vérifiant la valeur de cet attribut leaf.
        :return: True if the node is a leaf and false if he is not.
        """
        return self.leaf

    def set_leaf(self):
        """
        Défini le noeud comme étant une feuille de l'arbre dans lequel il se trouve en 
        définissant à True son attribut leaf.
        :return: Ne retourne rien.
        """
        self.leaf = True

    def number_of_sons(self):
        """
        Retourne le nombre de fils du noeud en renvoyant le nombre d'éléments de la liste 
        self.sons.
        :return: int, le nombre d'enfants du noeud.
        """
        return len(self.sons)

    def remove_value_in_node(self, value):
        """"
        Remove a value in a node and decreases the number of keys containing by the node.
        :param value: Value to remove from the node.
        :return: True if the value was present in the node and has been successfully removed and false in a other case.
        """
        self.keys.remove(value)

    def insert_value_in_node(self, value):
        """
        Insert a value at the correct position in a node and keep the value sorted.
        :param value: int value to insert.
        :return: The index where the value where added.
        """
        i = 0
        if value not in self.keys:
            while i < (len(self.keys)) and self.keys[i] < value:
                i += 1
            self.keys.insert(i, value)
            return self.keys.index(value)
        else:
            return self.keys.index(value)

    def search_in_node(self, value):
        """
        Recherche la valeur "value" dans le neoud en appliquant la recherche dichotomique
        sur les clés du noeud.
        :param value: int, valeur recherchée dans le noeud.
        :return: bool, retourne vrai si le noeud contient la valeur "value" et faux sinon.
        """
        found = False
        position_min = 0
        position_max = len(self.keys) - 1
        while position_min <= position_max and not found:
            position_middle = (position_min + position_max) // 2
            element = self.keys[position_middle]
            if value > element:
                position_min = position_middle + 1
            elif value < element:
                position_max = position_middle - 1
            else:
                found = True
        return found

    def hauteur(self):
        """
        Compte le nombre de descendants du noeud.
        :return: La nombre descendants d'un noeud.
        """
        if self.is_leaf():
            return 0
        else:
            return self.sons[0].hauteur() + 1
