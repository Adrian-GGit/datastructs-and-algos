import copy
import random
import pytest
from operator import lt, gt
from typing import Callable
import string

from algorithms.stringology.longest_common_prefix import LongestCommonPrefix

NUM_TESTS = 500
INTEGER_RANGE_START = 0
INTEGER_RANGE_END = 100
LENGTH_LSTS = random.randint(INTEGER_RANGE_START, INTEGER_RANGE_END)

priority_functions = [
    lt, gt
]
stringoloy_algos = [
]

def get_ground_truth(priority_function: Callable[[str, str], bool], array: list) -> list:
    ground_truth_lst = copy.deepcopy(array)
    if priority_function == gt:
        ground_truth_lst = list(reversed(sorted(array)))
    else:
        ground_truth_lst = list(sorted(array))
    return ground_truth_lst


@pytest.mark.parametrize('priority_function', priority_functions)
def test_longest_common_prefix(priority_function):
    for _ in range(NUM_TESTS):
        prefix_chars_length = random.randint(1, len(string.ascii_lowercase) - 1)
        prefix_chars = list(string.ascii_lowercase[0:prefix_chars_length])
        rest_chars = list(string.ascii_lowercase[prefix_chars_length:len(string.ascii_lowercase)])

        prefix_length = random.randint(0, INTEGER_RANGE_END)
        longest_common_prefix_choices = random.choices(prefix_chars, k=prefix_length)
        longest_common_prefix = ''.join(longest_common_prefix_choices)
        str_lst = []
        for i in range(LENGTH_LSTS):
            rest_length = random.randint(1, INTEGER_RANGE_END)
            content_choices = random.choices(rest_chars, k=rest_length)
            content = ''.join(content_choices)
            if i == 0:
                content = longest_common_prefix + ' ' + content # ensures that lcp can't be randomly extended by the rest chars
            else:
                content = longest_common_prefix + content
            str_lst.append(content)

        algo = LongestCommonPrefix(str_lst, priority_function)
        print(f'[-] Used lst: {str_lst}')

        assert algo.get_longest_common_prefix() == longest_common_prefix