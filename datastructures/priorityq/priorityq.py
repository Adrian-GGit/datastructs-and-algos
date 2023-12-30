from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class PriorityQ(ABC, Generic[T]):
    def __init__(self, queue: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.queue = queue


    def _swap(self, first_index: int, second_index: int) -> None:
        self.queue[first_index], self.queue[second_index] = self.queue[second_index], self.queue[first_index]


    def is_empty(self) -> bool:
        return self.size() <= 0


    def size(self) -> int:
        return len(self.queue)


    def insert(self, val: T) -> None:
        self.queue.append(val)
        self.decrease_key(self.size() - 1, val)


    def peek_min(self) -> T:
        return None if self.is_empty() else self.queue[0]


    def delete_min(self) -> T | None:
        return self.remove(0)


    @abstractmethod
    def build(self, array: list[T]) -> None:
        self.queue = array


    @abstractmethod
    def remove(self, index: int) -> T:
        if self.is_empty():
            return None
    

    @abstractmethod
    def decrease_key(self, index: int, val: T) -> None:
        self.queue[index] = val


    @abstractmethod
    def merge(self, queue) -> None:
        self.queue.extend(queue)
        self.build(self.queue)
    

    @abstractmethod
    def visualize(self) -> str:
        pass