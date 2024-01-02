# TODO: validate code coverage
# TODO: test all functions of binary heap etc
# TODO: search for all invariants and test these



import copy
import random
import pytest
from operator import lt, gt
from typing import TypeVar, Callable

from datastructures.priorityq.binary_heap import BinaryHeap

T = TypeVar('T')

NUM_TESTS = 100
INTEGER_RANGE_START = 0
INTEGER_RANGE_END = 1000
LENGTH_LSTS = random.randint(0, 100)

comp_funcs = [
    lt, gt
]

def get_ground_truth(comp_func: Callable[[T, T], bool], array: list[int]) -> list[int]:
    ground_truth_array = copy.deepcopy(array)
    if comp_func == gt:
        ground_truth_array = list(reversed(sorted(array)))
    else:
        ground_truth_array = list(sorted(array))
    return ground_truth_array


@pytest.mark.parametrize('comp_func', comp_funcs)
def test_empty_heap(comp_func):
    binary_heap = BinaryHeap(comp_func)

    assert binary_heap.size() == 0
    assert binary_heap.is_empty() is True


@pytest.mark.parametrize('comp_func', comp_funcs)
def test_build_heap_randomly(comp_func):
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(comp_func)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        print(f'[-] Used array: {array}')
        binary_heap.build(copy.deepcopy(array))

        popped_values = []
        array_reverse_sorted = get_ground_truth(comp_func, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_min() == next_max
            current = binary_heap.delete_min()
            popped_values.append(current)

        assert popped_values == get_ground_truth(comp_func, array)


@pytest.mark.parametrize('comp_func', comp_funcs)
def test_insert_heap_randomly(comp_func): 
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(comp_func)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        binary_heap.build(copy.deepcopy(array))

        for _ in range(NUM_TESTS):
            added_value = random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END)
            binary_heap.insert(added_value)
            array.append(added_value)
        print(f'[-] Used array: {array}')

        popped_values = []
        array_reverse_sorted = get_ground_truth(comp_func, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_min() == next_max
            current = binary_heap.delete_min()
            popped_values.append(current)

        assert popped_values == get_ground_truth(comp_func, array)


@pytest.mark.parametrize('comp_func', comp_funcs)
def test_heap_randomly(comp_func):
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(comp_func)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        print(f'[-] Used array: {array}')
        binary_heap.build(copy.deepcopy(array))
        
        popped_values = []
        array_reverse_sorted = get_ground_truth(comp_func, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_min() == next_max
            current = binary_heap.delete_min()
            popped_values.append(current)

        assert popped_values == get_ground_truth(comp_func, array)
