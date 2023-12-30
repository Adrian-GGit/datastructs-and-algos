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

priority_functions = [
    lt, gt
]

def get_ground_truth(priority_function: Callable[[T, T], bool], array: list[int]) -> list[int]:
    ground_truth_array = copy.deepcopy(array)
    if priority_function == gt:
        ground_truth_array = list(reversed(sorted(array)))
    else:
        ground_truth_array = list(sorted(array))
    return ground_truth_array


@pytest.mark.parametrize('priority_function', priority_functions)
def test_empty_heap(priority_function):
    binary_heap = BinaryHeap(priority_function)

    assert binary_heap.size() == 0
    assert binary_heap.is_empty() is True


@pytest.mark.parametrize('priority_function', priority_functions)
def test_build_heap_randomly(priority_function):
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        print(f'[-] Used array: {array}')
        binary_heap.build(copy.deepcopy(array))

        popped_values = []
        array_reverse_sorted = get_ground_truth(priority_function, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_first() == next_max
            current = binary_heap.delete_first()
            popped_values.append(current)

        assert popped_values == get_ground_truth(priority_function, array)


@pytest.mark.parametrize('priority_function', priority_functions)
def test_insert_heap_randomly(priority_function): 
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        binary_heap.build(copy.deepcopy(array))

        for _ in range(NUM_TESTS):
            added_value = random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END)
            binary_heap.insert(added_value)
            array.append(added_value)
        print(f'[-] Used array: {array}')

        popped_values = []
        array_reverse_sorted = get_ground_truth(priority_function, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_first() == next_max
            current = binary_heap.delete_first()
            popped_values.append(current)

        assert popped_values == get_ground_truth(priority_function, array)


@pytest.mark.parametrize('priority_function', priority_functions)
def test_heap_randomly(priority_function):
    for _ in range(NUM_TESTS):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        print(f'[-] Used array: {array}')
        binary_heap.build(copy.deepcopy(array))
        
        popped_values = []
        array_reverse_sorted = get_ground_truth(priority_function, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_first() == next_max
            current = binary_heap.delete_first()
            popped_values.append(current)

        assert popped_values == get_ground_truth(priority_function, array)
