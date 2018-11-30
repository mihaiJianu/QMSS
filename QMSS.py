from random import *

from Selection import *

def quickSort(l):
    
    recursiveQuickSort(l, 0, len(l) - 1)

def recursiveQuickSort(l, left, right):
    
    if left >= right:
        return

    pivot = sampleMedianSelect(l)
    
    pIndex = partitionDet(l, left, right, pivot)
    recursiveQuickSort(l, left, pIndex - 1)
    recursiveQuickSort(l, pIndex + 1, right)

def sampleMedianSelect(l):
    # @param l: list
    # @return pivot: int

    # Si sceglie il parametro m = 5, ovvero il n° minimo di elementi per eseguire 
    # l'operazione di calcolo del mediano in tempo O(n).

    # Costruisce sottoinsieme V di 5 elementi scelti a caso da l;
    
    i = 0
    V = []
    temp = l.copy()

    for i in range(0, 5):
        
        V.append(temp.pop(temp[randint(0, len(temp) - 1)]))

    # Prende mediano da suddetto sottoinsieme, effettuando un 
    # selectionSort sui primi 3 elementi di V (il mediano occupa la terza posizione)

    for k in range(0, 3):

        min_pos = k
        for j in range(k + 1, len(V)):
            if V[j] < V[min_pos]:
                min_pos = j

        V[min_pos], V[k] = V[k], V[min_pos]
        
    pivot = V[2]
    return pivot

    # 

    

