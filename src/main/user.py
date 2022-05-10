from Node import *
from Btree import *
import sys
import time

def explication():
    print("#----------------------------------- WELCOME -------------------------------------#")
    time.sleep(1.0)
    print("#------------------------------------- MENU --------------------------------------#")
    print("POUR AFFICHER L'ARBRE ENTREZ : d                                                  #")
    print("POUR INSÉRER UNE VALEUR DANS L'ARBRE ENTREZ : i                                   #")
    print("POUR INSÉRER UN INTERVALLE DE NOMBRES DANS L'ARBRE ENTREZ : iv                    #")
    print("POUR RECHERCHER UNE VALEUR DANS L'ARBRE ENTREZ : s                                #")
    print("POUR SUPPRIMER UNE VALEUR DE L'ARBRE ENTREZ : r                                   #")
    print("POUR VÉRIFIER SI L'ARBRE RESPECTE LES CONDITIONS D'UN ARBRE B ENTREZ : c          #")
    print("POUR SORTIR DU PROGRAMME ENTREZ : q                                               #")
    print("#---------------------------------------------------------------------------------#")
    print()

def create_tree():
    print("#------------------------------ CRÉATION DE L'ARBRE -------------------------------------#")
    print("#------------------------------ U DOIT ÊTRE SUPÉRIEUR À L -------------------------------#")
    print("#---------------------------- U ET L DOIVENT ETRE DES VALEURS ENTIÈRES ------------------#")
    l = int(input("#- Entrez la valeur que souhaitez pour L : "))
    u = int(input("#- Entrez la valeur que souhaitez pour U : "))
    print()
    if l > u:
        print("#---- LA VALEUR DE L DOIT ÊTRE INFÉRIEUR À LA VALEUR DE U                               ----#")
        return -1
    root = Node([], [], None, True)
    arbre = Btree(l,u,root)
    return arbre

if __name__ == '__main__':
    print("USER PY")
    explication()
    arbre = create_tree()
    if(arbre == -1):
        print("#---- ERREUR DE CRÉATION, LE PROGRAMME VA S'ARRÊTER VEUILLEZ LE RELANCER POUR RÉESSAYER ----#")
        time.sleep(1.0)
        print("#------------------------------------ À LA PROCHAINE----------- ----------------------------#")
        time.sleep(1.0)
        sys.exit()
    while(True):
        entrer_clavier = str(input("QUELLE ACTION SOUHAITEZ VOUS RÉALISER : "))

        if (entrer_clavier == 'i'):
            insert_value = l = int(input("#- Entrez la valeur que souhaitez pour insérer dans l'abre (DOIT ÊTRE UN ENTIER): "))
            print("Insertion de "+str(insert_value)+"")
            check = arbre.insert(insert_value)
            if(check == True):
                print("#-------------------- INSERTION DE "+str(insert_value)+" RÉUSSI --------------------#")
            else:
                print("#-------------------- INSERTION DE "+str(insert_value)+" RATÉ ----------------------#")
                print("#-------------------- LA VALEUR EST DÉJÀ PRÉSENTE DANS L'ARBRE --------------------#")
                print()
        
        elif (entrer_clavier == 'q'):
            time.sleep(1.0)
            print("#---------------- VOUS ALLEZ QUITTER LE PROGRAMMME ----------------#")
            time.sleep(1.0)
            print("#------------------------ À LA PROCHAINE---------------------------#")
            time.sleep(1.0)
            sys.exit()
        
        elif (entrer_clavier == 'd'):
            if len(arbre.root.keys) == 0:
                print(" L'ARBRE EST VIDE ")
                print()
            else:
                print("#---------------- AFFICHAGE DE L'ARBRE ----------------------------#")
                arbre.display_tree(arbre.root)
                print()
        
        elif (entrer_clavier == 's'):
            value_to_search = int(input("QUELLE VALEUR SOUHAITEZ RECHERCHER (DOIT ÊTRE UN ENTIER) :"))
            bool1 = arbre.btree_search(value_to_search)
            print("RÉSULTAT DE LA RECHERCHE :",end=" ")
            print(bool1)
            print()
            print("#--------------------FIN DE LA RECHERCHE DE "+str(value_to_search)+"-------------------#")

        elif (entrer_clavier == 'c'):
            print("#---------------VÉRIFICATION  SI C'EST UN ARBRE B---------------#")
            booltree = arbre.est_ArbreB() 
            print("RÉSULTAT DE LA VÉRIFICATION :",end=" ")
            print(booltree)
            print()
            time.sleep(1.0)
            print("#-------------------- FIN DE LA VÉRIFICATION --------------------#")
        
        elif (entrer_clavier == 'iv'):
            start = int(input("ENTREZ LA VALEUR DE DÉPART                                                  : "))
            end = int(input("ENTREZ LA VALEUR DE FIN                                                       : "))
            step = int(input("ENTREZ LE PAS D'ÉCART ENTRE CHAQUE VALEUR (DOIT ÊTRE SUPÉRIEUR OU ÉGALE À 1) : "))
            check_v = str(input("SOUHAITEZ VOUS SUIVRE PROGRESSIVEMENT L'INSERTION (y (oui) ou n (non))    : "))
            print()
            if(step<1):
                print("LA VALEUR DU PAS DOIT ÊTRE SUPÉRIEUR OU ÉGALE À 1 !")
                print()
            else:
                l_insert = [i for i in range(start,end+1,step)]
                if (check_v == 'y'):
                    for i in l_insert:
                        print("Insertion de "+str(i)+"")
                        arbre.insert(i)
                        print("ARBRE")
                        arbre.display_tree(arbre.root)
                        time.sleep(1.0)
                        print()
                else:
                    for i in l_insert:
                        print("Insertion de "+str(i)+"")
                        arbre.insert(i)
                        print("ARBRE")
                        arbre.display_tree(arbre.root)
                        print()
                
        elif (entrer_clavier == 'r'):
            print()
            print("CETTE FONCTIONNALITÉ N'EST PAS ENCORE DISPONIBLE.")
            print()

        else:
            time.sleep(1.0)
            print("#---- ERREUR DE D'ACTION, LA COMMANDE ENTRER N'EST PAS VALIDE ----#")
            print()
            explication()
            print()