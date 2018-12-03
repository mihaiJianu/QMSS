import QMSS_module
import argparse
import cProfile
import pstats
import random
from sorting.Sorting import *

l = [random.randint(0, 1000000) for i in range(10000)]

if __name__ == "__main__":

    temp = l.copy()

    parser = argparse.ArgumentParser("oython - main", description='profile execution time, of major sortin algorithms')
    parser.add_argument("sel", type = str, choices = ["med", "rand", "det"], help =  "choose the type of selection used by quickSort")
    args = parser.parse_args()

    if(args.sel == "med"):

        cProfile.run('QMSS_module.quickSelectSort(l, 0)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    elif(args.sel == "rand"):

        cProfile.run('QMSS_module.quickSelectSort(l, 1)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    elif(args.sel == "det"):

        cProfile.run('QMSS_module.quickSelectSort(l, 2)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    l = temp.copy()
    cProfile.run('selectionSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('insertionSortDown(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('bubbleSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('mergeSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('quickSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('heapSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('radixSort(l, 100, 10)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
    cProfile.run('l.sort()', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
    l = temp.copy()
