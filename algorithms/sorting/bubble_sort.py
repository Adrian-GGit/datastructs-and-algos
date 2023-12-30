from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class BubbleSort(Generic[T]):
    def __init__(self, lst: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.lst = lst


    def _swap(self, first_index: int, second_index: int) -> None:
        self.lst[first_index], self.lst[second_index] = self.lst[second_index], self.lst[first_index]


    def sort(self) -> list[T]:
        swapped = True
        rng = len(self.lst)
        while swapped:
            swapped = False
            for index in range(rng - 1):
                if self.comp_func(self.lst[index + 1], self.lst[index]):
                    self._swap(index, index + 1)
                    swapped = True
            rng -= 1
