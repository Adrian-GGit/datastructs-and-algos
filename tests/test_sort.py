import copy
import random
import pytest
from operator import lt, gt
from typing import TypeVar, Callable
from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.insertion_sort import InsertionSort

from algorithms.sorting.merge_sort import MergeSort
from algorithms.sorting.quick_sort import QuickSort

T = TypeVar('T')

NUM_TESTS = 500
INTEGER_RANGE_START = 0
INTEGER_RANGE_END = 1000
LENGTH_LSTS = 100

priority_functions = [
    lt, gt
]
sorting_algos = [
    MergeSort,
    QuickSort,
    BubbleSort,
    InsertionSort,
]

def get_ground_truth(priority_function: Callable[[T, T], bool], array: list) -> list:
    ground_truth_lst = copy.deepcopy(array)
    if priority_function == gt:
        ground_truth_lst = list(reversed(sorted(array)))
    else:
        ground_truth_lst = list(sorted(array))
    return ground_truth_lst


@pytest.mark.parametrize('priority_function', priority_functions)
@pytest.mark.parametrize('sorting_algo', sorting_algos)
def test_sort(priority_function, sorting_algo):
    for _ in range(NUM_TESTS):
        lst = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        algo = sorting_algo(lst, priority_function)
        print(f'[-] Used lst: {lst}')

        algo.sort()
        assert algo.lst == get_ground_truth(priority_function, lst)
