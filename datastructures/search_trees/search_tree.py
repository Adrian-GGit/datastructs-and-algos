from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable
from operator import lt

T = TypeVar('T')
V = TypeVar('V')


class Node(Generic[T, V]):
    def __init__(self, key: T, value: V) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class SearchTree(ABC, Generic[T]):
    def __init__(self, order_relation: Callable[[T, T], bool] = lt) -> None:
        self.order_relation = order_relation
        self.tree_size = 0
        self.root = None            


    def _get_min_by_node(self, current_node) -> tuple[Node, V]:
        if not current_node: 
            return None, None
        while current_node.left:
            current_node = current_node.left
        return current_node, current_node.value


    def _shift_nodes(self, current_node: Node, next_node: Node) -> None:
        if not current_node.parent:
            self.root = next_node
        elif current_node == current_node.parent.left:
            current_node.parent.left = next_node
        else:
            current_node.parent.right = next_node
        if next_node:
            next_node.parent = current_node.parent


    def is_empty(self) -> bool:
        return self.size() <= 0


    def size(self) -> int:
        return self.tree_size


    @abstractmethod
    def search(self, key: T) -> None:
        pass


    @abstractmethod
    def insert(self, key: T) -> None:
        pass


    @abstractmethod
    def delete(self, key: T) -> V | None:
        pass


    @abstractmethod
    def visualize(self) -> str:
        pass
