from random import *
from selection.Selection import partitionDet, quickSelectRand, quickSelectDet

def quickSelectSort(l, select):
    assert type(l) == list, "Error! Not a list"

    recursiveQuickSelectSort(l, 0, len(l) - 1, select)


def recursiveQuickSelectSort(l, left, right, select):
    if left >= right:
        return

    if select == 0:
        pivot = sampleMedianSelect(l[left : right + 1])
    
    # se pivot == mediano velocizza l'esecuzione di quicksort
    
    elif select == 1:
        pivot = quickSelectRand(l, int(len(l) / 2))
    
    # lista minima di 10 elementi, altrimenti conviene ordinarli per estrarre il mediano

    elif select == 2:
        pivot = quickSelectDet(l, int(len(l) / 2), 10)

    #print(pivot)
    #print("({},{})".format(left, right))
    pIndex = partitionDet(l, left, right, pivot)
    #print(l)
    recursiveQuickSelectSort(l, left, pIndex - 1, select)
    #print("({},{})".format(left, right))
    #print(l)
    recursiveQuickSelectSort(l, pIndex + 1, right, select)
    #print("({},{})".format(left, right))
    #print(l)


def sampleMedianSelect(l):
    """
    #@param l: list 
    #@return pivot: int

    #Si assuma che m sia uguale a 5
    #Costruisco l'insieme V di 5 elementi scelti a caso da l
    
    """
    m = 5
    i = 0
    V = []
    temp = l.copy()

    while i < m and len(temp) != 0:
        lenTemp = len(temp) 
        index = randint(0, lenTemp - 1)
        V.append(temp.pop(index))
        i += 1

    #Effettuo un selection sort sui primi len(V)/2 elementi.
    #L'elemento alla posizione len(V) / 2 elemento sarà il mediano di V
    
    for k in range(0, int(len(V) / 2)):

        min_pos = k
        for j in range(k + 1, len(V)):
            if V[j] < V[min_pos]:
                min_pos = j

        V[min_pos], V[k] = V[k], V[min_pos]  # m

    pivot = V[int(len(V) / 2)]
    return pivot

    

