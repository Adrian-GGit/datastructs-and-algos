from typing import TypeVar, Callable
from operator import lt

from datastructures.priorityq.priorityq import PriorityQ

T = TypeVar('T')

class FibonacciHeap(PriorityQ):
    def __init__(self, comp_func: Callable[[T, T], bool] = lt) -> None:
        super().__init__([], comp_func)


    def build(self, array: list[T]) -> None:
        super().build(array)


    def remove(self, index: int) -> T:
        super().remove(index)
    

    def decrease_key(self, index: int, val: T) -> None:
        super().decrease_key(index, val)

    
    def merge(self, queue) -> None:
        super().merge(queue)


    def visualize(self) -> None:
        super().visualize()
