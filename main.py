import QMSS_module
import argparse
import cProfile
import pstats
import random
from sorting.Sorting import *


if __name__ == "__main__":

    
    parser = argparse.ArgumentParser("python -m main")
    parser.add_argument("sel", type = str, choices = ["med", "rand", "det"], help = "chooses the type of selection used by quickSort")

    args = parser.parse_args()
    
    l = [random.randint(0, 100) for i in range(20)]
    temp = l
    print(f"input list is: {l}")

    if(args.sel == "med"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 0)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    elif(args.sel == "rand"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 1)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    elif(args.sel == "det"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 2)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    print(f"quickSelectSort list: {l}")

    l = temp
    cProfile.run('selectionSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"selectionSort list: {l}")

    l = temp
    cProfile.run('insertionSortDown(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"insertionSortDown list: {l}")

    l = temp
    cProfile.run('bubbleSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"bubbleSort list: {l}")

    l = temp
    cProfile.run('mergeSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"mergeSort list: {l}")

    l = temp
    cProfile.run('quickSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"quickSort list: {l}")

    l = temp
    cProfile.run('heapSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"heapSort list: {l}")

    l = temp
    cProfile.run('radixSort(l, 100, 10)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"radixSort list: {l}")

    l = temp
    cProfile.run('l.sort()', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    print(f"l.sort() list: {l}")
