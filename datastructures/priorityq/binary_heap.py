import math

class BinaryHeap():
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
    def __init__(self, priority_func: callable = min) -> None:
        self.queue = []
        self.priority_func = priority_func


    def get_node(self, index: int) -> tuple[int, int | None]:
        value = None
        if index < len(self.queue):
            value = self.queue[index]
        return index, value


    def get_left(self, parent_index: int) -> tuple[int, int | None]:
        return self.get_node(2 * parent_index + 1)


    def get_right(self, parent_index: int) -> tuple[int, int | None]:
        return self.get_node(2 * parent_index + 2)
    

    def get_parent(self, child_index: int) -> tuple[int, int | None]:
        return self.get_node((child_index - 1) // 2)
    

    def swap(self, first_index: int, second_index: int) -> None:
        tmp_val = self.queue[first_index]
        self.queue[first_index] = self.queue[second_index]
        self.queue[second_index] = tmp_val


    def get_priority_val(self, l) -> int:
        return self.priority_func([val for val in l if val is not None])


    def heapify_down(self, index: int) -> None:
        current_index = index
        while True:
            parent_index, parent_val = current_index, self.queue[current_index]
            left_index, left_val = self.get_left(parent_index)
            right_index, right_val = self.get_right(parent_index)
            priority_val = self.get_priority_val([parent_val, left_val, right_val])

            if priority_val == parent_val:
                break
            elif priority_val == left_val:
                self.swap(current_index, left_index)
                current_index = left_index
            elif priority_val == right_val:
                self.swap(current_index, right_index)
                current_index = right_index

    
    def heapify_up(self, index) -> None:
        val = self.queue[index]
        parent_index, parent_val = self.get_parent(index)
        while self.get_priority_val([val, parent_val]) == val and index > 0:
            self.swap(parent_index, index)
            index = parent_index
            parent_index, parent_val = self.get_parent(parent_index)
            

    def build(self, array: list) -> None:
        """
        Rearrange elements in array to fulfill the heap characteristic by going bottom up
        Note: to start from the parents of the last childs just iterate over the first half (the last row contains half of the elements)

        Args:
            array (list): array to be converted to heap
        """
        if len(array) == 0: return
        self.queue = array
        for i in range(len(array) // 2, -1, -1):
            self.heapify_down(i)


    def decrease_key(self, index: int, val: int) -> None:
        self.queue[index] = val
        self.heapify_up(index)


    def insert(self, val: int) -> None:
        self.queue.append(val)
        self.decrease_key(self.size() - 1, val)


    def delete_first(self) -> int | None:
        return self.remove_at(0)


    def remove_at(self, index: int) -> int:
        if self.is_empty():
            return None
        
        self.swap(index, self.size() - 1)
        removed = self.queue.pop()
        if index != self.size():
            self.heapify_down(index)
            
        return removed


    def peek_first(self) -> int:
        return None if self.is_empty() else self.queue[0]


    def size(self) -> int:
        return len(self.queue)


    def is_empty(self) -> bool:
        return self.size() <= 0


    def visualize(self) -> None:
        def add_padding(block_size, element, padding_char, block_space_char):
            half_block_size = block_size // 2
            block_size_rest = block_size % 2
            half_element_size = len(element) // 2
            element_size_rest = len(element) % 2
            padding_front = (half_block_size - half_element_size) * padding_char
            padding_back = (half_block_size + block_size_rest - half_element_size - element_size_rest) * padding_char
            return padding_front + element + padding_back + block_space_char
        

        def get_nodes(current_level, empty_node_char):
            num_nodes_on_level = (2**current_level) // 2
            start = 2**current_level - (num_nodes_on_level + 1)
            end = start + (num_nodes_on_level) if start + num_nodes_on_level <= self.size() else self.size()
            nodes = self.queue[start:end]
            nodes.extend([empty_node_char for _ in range(num_nodes_on_level - len(nodes))])
            return nodes


        def get_biggest_node():
            return max([len(str(number)) for number in self.queue])
        

        def get_heap_depth():
            return math.floor(math.log(self.size(), 2)) + 1
        

        def add_box(current_level, line, previous_lines):
            BOX_TOP = '-'
            BOX_SIDE = '|'
            box_outer = BOX_TOP * (len(line) + 2)
            empty_line = '\n' + BOX_SIDE + SPACE_CHAR*len(line) + BOX_SIDE if current_level != get_heap_depth() - 1 else '\n' + box_outer
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
        current_level = get_heap_depth()
        last_block_size = get_biggest_node()
        while current_level > 0:
            line = ''
            current_block_size = 2 * last_block_size + SPACE_LENGTH
            for number in get_nodes(current_level, EMPTY_NODE_CHAR):
                line += add_padding(current_block_size, str(number), SPACE_CHAR, BLOCK_SPACE_CHAR)
            last_block_size = current_block_size
            current_level -= 1
            output = add_box(current_level, line, output)
    
        print(output)
        return output