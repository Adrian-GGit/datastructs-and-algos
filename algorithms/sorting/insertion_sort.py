from algorithms.sorting.sort import Sort, T


class InsertionSort(Sort):
    def sort(self) -> list[T]:
        super().sort()

        for index in range(len(self.lst)):
            current_elem = self.lst[index]
            current_index = index - 1
            while current_index >= 0 and self.comp_func(current_elem, self.lst[current_index]):
                self.lst[current_index + 1] = self.lst[current_index]
                current_index -= 1
            self.lst[current_index + 1] = current_elem
