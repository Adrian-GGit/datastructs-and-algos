from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class QuickSort(Generic[T]):
    def __init__(self, lst: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.lst = lst


    def swap(self, first_index: int, second_index: int) -> None:
        self.lst[first_index], self.lst[second_index] = self.lst[second_index], self.lst[first_index]


    def sort(self, left: int = 0, right: int = None) -> list[T]:
        if right is None:
            right = len(self.lst) - 1
        
        if left < right:
            divider = self.divide(left, right)
            self.sort(left, divider - 1)
            self.sort(divider + 1, right)

    
    def get_left_right(self, left, right, pivot):
        while left < right and (self.comp_func(self.lst[left], self.lst[pivot]) or self.lst[left] == self.lst[pivot]):
            left += 1
        while right > left and self.comp_func(self.lst[pivot], self.lst[right]):
            right -= 1
        return left, right


    def divide(self, left: int, right: int) -> list[T]:
        pivot = right
        current_left = left
        current_right = pivot - 1
        while current_left < current_right:
            current_left, current_right = self.get_left_right(current_left, current_right, pivot)
            self.swap(current_left, current_right)
        if self.comp_func(self.lst[pivot], self.lst[current_left]):
            self.swap(current_left, pivot)
        else:
            current_left = pivot
        return current_left
