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


    def get_left(self, parent_index: int) -> tuple[int, int | None]:
        left_value = None
        left_index = 2 * parent_index + 1
        if left_index < len(self.queue):
            left_value = self.queue[left_index]
        return left_index, left_value


    def get_right(self, parent_index: int) -> tuple[int, int | None]:
        right_value = None
        right_index = 2 * parent_index + 2
        if right_index < len(self.queue):
            right_value = self.queue[right_index]
        return right_index, right_value
    

    def get_parent(self, child_index: int) -> tuple[int, int | None]:
        parent_value = None
        parent_index = (child_index - 1) // 2
        if parent_index < len(self.queue):
            parent_value = self.queue[parent_index]
        return parent_index, parent_value
    

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
            l = [parent_val, left_val, right_val]
            priority_val = self.get_priority_val(l)

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
        if self.is_empty():
            return ''

        space_length = 1
        
        output = ''
        longest_number = max([len(str(number)) for number in self.queue])
        heap_depth = math.floor(math.log(self.size(), 2)) + 1
        block_space_char = ' ' * space_length
        space_char = ' '
        current_level = heap_depth
        last_block_size = longest_number
        while current_level > 0:
            num_nodes_on_level = (2**current_level) // 2
            start = 2**current_level - (num_nodes_on_level + 1)
            end = start + (num_nodes_on_level) if start + num_nodes_on_level <= self.size() else self.size()
            numbers_of_level = self.queue[start:end]

            line = ''
            current_block_size = 2 * last_block_size + space_length
            for number in numbers_of_level:
                padding_front = ((longest_number // 2) - (len(str(number)) // 2)) * space_char
                padding_back = ((longest_number // 2) + (longest_number % 2) - (len(str(number)) // 2) - (len(str(number)) % 2)) * space_char
                number_with_padding = padding_front + str(number) + padding_back

                padding_block_size_front = ((current_block_size // 2) - (len(number_with_padding) // 2)) * space_char
                padding_block_size_back = (
                    (current_block_size // 2) + (current_block_size // 2 % 2) - (len(number_with_padding) // 2) - (len(number_with_padding) % 2)
                ) * space_char
                number_with_all_paddings = padding_block_size_front + number_with_padding + padding_block_size_back + block_space_char
                line += number_with_all_paddings
            last_block_size = current_block_size

            output = '\n' + '|' + line + output
            current_level -= 1
    
        max_line_length = len(max(output.split('\n'), key=len))
        separator = '-' * max_line_length
        output = '\n' + separator + output + '\n' + separator + '\n'
        print(output)

        return output