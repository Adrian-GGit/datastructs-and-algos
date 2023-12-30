from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class InsertionSort(Generic[T]):
    def __init__(self, lst: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.lst = lst


    def _swap(self, first_index: int, second_index: int) -> None:
        self.lst[first_index], self.lst[second_index] = self.lst[second_index], self.lst[first_index]


    def sort(self) -> list[T]:
        for index in range(len(self.lst)):
            current_elem = self.lst[index]
            current_index = index - 1
            while current_index >= 0 and self.comp_func(current_elem, self.lst[current_index]):
                self.lst[current_index + 1] = self.lst[current_index]
                current_index -= 1
            self.lst[current_index + 1] = current_elem
