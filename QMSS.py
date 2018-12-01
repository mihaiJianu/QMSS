from random import *
from selection.Selection import partitionDet

def quickSort(l):
    assert type(L) == list, "Error! Not a list"

    recursiveQuickSort(l, 0, len(l) - 1)


def recursiveQuickSort(l, left, right):
    if left >= right:
        return

    pivot = sampleMedianSelect(l[left : right + 1]);
    #print(pivot)
    #print("({},{})".format(left, right))
    pIndex = partitionDet(l, left, right, pivot)
    #print(l)
    recursiveQuickSort(l, left, pIndex - 1)
    #print("({},{})".format(left, right))
    #print(l)
    recursiveQuickSort(l, pIndex + 1, right)
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

    

