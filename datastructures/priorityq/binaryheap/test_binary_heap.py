import copy
import random
import pytest
from binary_heap import BinaryHeap

priority_functions = [
    min, max
]

def get_ground_truth(priority_function: callable, array: list) -> list:
    ground_truth_array = copy.deepcopy(array)
    if priority_function == max:
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
def test_build_heap(priority_function):
    test_arrays = [
        [2, 5, 1, 3, 7, 8],
        [2, 5, 1, 3, 7, 6], 
        [2, 5, 1, 3, 7, 5, 6, 8, 8], 
        [2, 5, 1, 3, 7, 5, 6, 8],
        [6, 4, 7, 9, 1, 3],
    ]
    for array in test_arrays:
        binary_heap = BinaryHeap(priority_function)
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
def test_build_heap_randomly(priority_function):
    for _ in range(10):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(1, 1000) for _ in range(10)]
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
    for _ in range(10):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(1, 1000) for _ in range(10)]
        binary_heap.build(copy.deepcopy(array))

        for _ in range(10):
            added_value = random.randint(1, 100)
            binary_heap.insert(added_value)
            array.append(added_value)

        popped_values = []
        array_reverse_sorted = get_ground_truth(priority_function, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_first() == next_max
            current = binary_heap.delete_first()
            popped_values.append(current)

        assert popped_values == get_ground_truth(priority_function, array)
        print(f'[-] Used array: {array}')


@pytest.mark.parametrize('priority_function', priority_functions)
def test_heap_randomly(priority_function):
    for _ in range(10):
        binary_heap = BinaryHeap(priority_function)
        array = [random.randint(1, 1000) for _ in range(10)]
        binary_heap.build(copy.deepcopy(array))
        
        popped_values = []
        array_reverse_sorted = get_ground_truth(priority_function, array)
        for _ in range(len(array)):
            next_max = array_reverse_sorted.pop(0)
            assert binary_heap.peek_first() == next_max
            current = binary_heap.delete_first()
            popped_values.append(current)

        assert popped_values == get_ground_truth(priority_function, array)
        print(f'[-] Used array: {array}')
