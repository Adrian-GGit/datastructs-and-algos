from algorithms.sorting.sort import Sort, T


class QuickSort(Sort):
    def _get_left_right(self, left, right, pivot):
        while left < right and (self.comp_func(self.lst[left], self.lst[pivot]) or self.lst[left] == self.lst[pivot]):
            left += 1
        while right > left and self.comp_func(self.lst[pivot], self.lst[right]):
            right -= 1
        return left, right


    def _divide(self, left: int, right: int) -> list[T]:
        pivot = right
        current_left = left
        current_right = pivot - 1
        while current_left < current_right:
            current_left, current_right = self._get_left_right(current_left, current_right, pivot)
            self._swap(current_left, current_right)
        if self.comp_func(self.lst[pivot], self.lst[current_left]):
            self._swap(current_left, pivot)
        else:
            current_left = pivot
        return current_left


    def sort(self, left: int = 0, right: int = None) -> list[T]:
        if right is None:
            right = len(self.lst) - 1
        
        if left < right:
            divider = self._divide(left, right)
            self.sort(left, divider - 1)
            self.sort(divider + 1, right)
