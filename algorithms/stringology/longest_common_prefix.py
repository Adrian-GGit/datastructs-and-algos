from typing import Callable
from operator import lt


class LongestCommonPrefix():
    def __init__(self, str_lst: list[str], comp_func: Callable[[str, str], bool] = lt) -> None:
        self.comp_func = comp_func
        self.str_lst = str_lst
        self.prefix = ''


    def get_longest_common_prefix(self):
        self.str_lst = self.str_lst or ['']
        if len(self.str_lst) <= 1:
            return self.str_lst[0]

        first = self.str_lst[0]
        for i, c in enumerate(first):
            for word in self.str_lst[1:]:
                if i >= len(word) or (self.comp_func(word[i], c) or self.comp_func(c, word[i])):
                    return self.prefix
            self.prefix += c
        return self.prefix
