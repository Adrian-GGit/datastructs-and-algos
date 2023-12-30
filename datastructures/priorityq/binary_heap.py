import math
from typing import TypeVar, Callable
from operator import lt

from datastructures.priorityq.priorityq import PriorityQ

T = TypeVar('T')

class BinaryHeap(PriorityQ):
    """
    Representation example:
                                  0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

    => left child of parent k: 2k+1
    => right child of parent k: 2k+2
    """
    def __init__(self, comp_func: Callable[[T, T], bool] = lt) -> None:
        super().__init__([], comp_func)

    def _get_left_child(self, parent_index: int) -> tuple[int, T | None]:
        return 2 * parent_index + 1


    def _get_right_child(self, parent_index: int) -> tuple[int, T | None]:
        return 2 * parent_index + 2
    

    def _get_parent(self, child_index: int) -> tuple[int, T | None]:
        return (child_index - 1) // 2


    def _heapify_down(self, index: int) -> None:
        current_index = index
        while current_index < self.size():
            left_child_index = self._get_left_child(current_index)
            right_child_index = self._get_right_child(current_index)
            swap_index = current_index
            if left_child_index < self.size() and self.comp_func(self.queue[left_child_index], self.queue[swap_index]):
                swap_index = left_child_index
            if right_child_index < self.size() and self.comp_func(self.queue[right_child_index], self.queue[swap_index]):
                swap_index = right_child_index

            if swap_index != current_index:
                self._swap(current_index, swap_index)
                current_index = swap_index
            else:
                break

    
    def _heapify_up(self, index: int) -> None:
        current_index = index
        while current_index > 0:
            parent_index = self._get_parent(current_index)
            if self.comp_func(self.queue[current_index], self.queue[parent_index]):
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
            

    def build(self, array: list[T]) -> None:
        """
        Rearrange elements in array to fulfill the heap characteristic by going bottom up
        Note: to start from the parents of the last childs just iterate over the first half (the last row contains half of the elements)

        Args:
            array (list): array to be converted to heap
        """
        super().build(array)
        if len(array) != 0:
            for i in range(len(array) // 2, -1, -1):
                self._heapify_down(i)


    def remove(self, index: int) -> T:
        super().remove(index)
        self._swap(index, self.size() - 1)  
        removed = self.queue.pop()
        if index != self.size():
            self._heapify_down(index)
            
        return removed
    

    def decrease_key(self, index: int, val: T) -> None:
        super().decrease_key(index, val)
        self._heapify_up(index)

    
    def merge(self, queue) -> None:
        super().merge(queue)


    def visualize(self) -> None:
        super().visualize()

        def _add_padding(block_size, element, padding_char, block_space_char):
            half_block_size = block_size // 2
            block_size_rest = block_size % 2
            half_element_size = len(element) // 2
            element_size_rest = len(element) % 2
            padding_front = (half_block_size - half_element_size) * padding_char
            padding_back = (half_block_size + block_size_rest - half_element_size - element_size_rest) * padding_char
            return padding_front + element + padding_back + block_space_char
        

        def _get_nodes(current_level, empty_node_char):
            num_nodes_on_level = (2**current_level) // 2
            start = 2**current_level - (num_nodes_on_level + 1)
            end = start + (num_nodes_on_level) if start + num_nodes_on_level <= self.size() else self.size()
            nodes = self.queue[start:end]
            nodes.extend([empty_node_char for _ in range(num_nodes_on_level - len(nodes))])
            return nodes


        def _get_biggest_node():
            return max([len(str(number)) for number in self.queue])
        

        def _get_heap_depth():
            return math.floor(math.log(self.size(), 2)) + 1
        

        def _add_box(current_level, line, previous_lines):
            BOX_TOP = '-'
            BOX_SIDE = '|'
            box_outer = BOX_TOP * (len(line) + 2)
            empty_line = '\n' + BOX_SIDE + SPACE_CHAR*len(line) + BOX_SIDE if current_level != _get_heap_depth() - 1 else '\n' + box_outer
            added_new_line = '\n' + BOX_SIDE + line + BOX_SIDE + empty_line + previous_lines
            if current_level <= 0:
                added_new_line = box_outer + added_new_line
            return added_new_line


        if self.is_empty():
            return ''

        SPACE_LENGTH = 1
        SPACE_CHAR = ' '
        BLOCK_SPACE_CHAR = SPACE_CHAR * SPACE_LENGTH
        EMPTY_NODE_CHAR = '*'
        
        output = ''
        current_level = _get_heap_depth()
        last_block_size = _get_biggest_node()
        while current_level > 0:
            line = ''
            current_block_size = 2 * last_block_size + SPACE_LENGTH
            for number in _get_nodes(current_level, EMPTY_NODE_CHAR):
                line += _add_padding(current_block_size, str(number), SPACE_CHAR, BLOCK_SPACE_CHAR)
            last_block_size = current_block_size
            current_level -= 1
            output = _add_box(current_level, line, output)
    
        print(output)
        return output