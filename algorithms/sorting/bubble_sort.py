from algorithms.sorting.sort import Sort, T


class BubbleSort(Sort):
    def sort(self) -> list[T]:
        swapped = True
        rng = len(self.lst)
        while swapped:
            swapped = False
            for index in range(rng - 1):
                if self.comp_func(self.lst[index + 1], self.lst[index]):
                    self._swap(index, index + 1)
                    swapped = True
            rng -= 1
