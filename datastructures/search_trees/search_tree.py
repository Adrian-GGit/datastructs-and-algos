from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')

class SearchTree(ABC, Generic[T]):
    def __init__(self, queue: list[T], comp_func: Callable[[T, T], bool] = lt) -> None:
        self.comp_func = comp_func
        self.queue = queue


    def _swap(self, first_index: int, second_index: int) -> None:
        self.queue[first_index], self.queue[second_index] = self.queue[second_index], self.queue[first_index]


    def is_empty(self) -> bool:
        return self.size() <= 0


    def size(self) -> int:
        return len(self.queue)


    # TODO: if not self.comp_func(current, )
    @abstractmethod
    def search(self, key: T) -> None:
        pass


    @abstractmethod
    def insert(self, key: T) -> None:
        pass


    @abstractmethod
    def delete(self, key: T) -> None:
        pass


    # @abstractmethod
    # def traverse(self, ) -> None:
    #     pass


    @abstractmethod
    def build(self, array: list[T]) -> None:
        pass