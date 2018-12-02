import QMSS_module
import argparse
import cProfile
import pstats
import random
from sorting.Sorting import *


if __name__ == "__main__":

    l = [random.randint(0, 100) for i in range(20)]

    parser = argparse.ArgumentParser()
    parser.add_argument("sel", type = str, choices = ["med", "rand", "det"])
    args = parser.parse_args()

    if(args.sel == "med"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 0)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    elif(args.sel == "rand"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 1)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    elif(args.sel == "det"):

    	cProfile.run('QMSS_module.quickSelectSort(l, 2)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()


    cProfile.run('selectionSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('insertionSortDown(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('bubbleSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('mergeSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('quickSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('heapSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('radixSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

    cProfile.run('sort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("Time").print_stats()

