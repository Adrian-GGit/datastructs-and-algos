import copy
import random
import pytest
from operator import lt, gt
from typing import Callable
from datastructures.search_trees.binary_search_tree import BinarySearchTree, T

NUM_TESTS = 100
INTEGER_RANGE_START = 0
INTEGER_RANGE_END = 1000
LENGTH_LSTS = 100

order_relations = [
    lt, gt
]
search_trees = [
    BinarySearchTree,
]

def get_ground_truth(order_relation: Callable[[T, T], bool], array: list) -> list:
    ground_truth_lst = copy.deepcopy(array)
    if order_relation == gt:
        ground_truth_lst = list(reversed(sorted(array)))
    else:
        ground_truth_lst = list(sorted(array))
    return ground_truth_lst


@pytest.mark.parametrize('order_relation', order_relations)
@pytest.mark.parametrize('search_tree', search_trees)
def test_search_tree(order_relation, search_tree):
    for _ in range(NUM_TESTS):
        keys = [random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END) for _ in range(LENGTH_LSTS)]
        tree = search_tree(order_relation)
        print(f'[-] Used lst: {keys}')

        random_value = random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END)
        tree.insert(random_value, random_value)
        assert tree.search(random_value).value == random_value
        assert tree.search(-1) == None
        tree.delete(random_value)

        for key in keys:
            tree.insert(key, key)

        deletion_range = (len(keys) // 2)
        for _ in range(deletion_range):
            keys.pop()
            tree.delete(keys[len(keys) - 1])
        print(f'[-] Used lst: {keys}')

        for index, key in enumerate(keys):
            node = tree.search(key)
            if index < len(keys) - deletion_range:
                assert node.value == key
            else:
                assert tree.search(-1) == None

        for key in keys[1:len(keys)]:
            tree.delete(key)
