from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class Sort(ABC, Generic[T]):
    def __init__(self, lst: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.lst = lst


    def _swap(self, first_index: int, second_index: int) -> None:
        self.lst[first_index], self.lst[second_index] = self.lst[second_index], self.lst[first_index]

    
    @abstractmethod
    def sort(self):
        pass
