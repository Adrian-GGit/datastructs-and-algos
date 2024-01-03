from algorithms.sorting.sort import Sort, T


class MergeSort(Sort):
    def _merge(self, left: list[T], right: list[T]) -> list[T]:
        sorted_lst = []
        while left and right:
            next_item = left.pop(0) if self.comp_func(left[0], right[0]) else right.pop(0)
            sorted_lst.append(next_item)
        sorted_lst.extend(left)
        sorted_lst.extend(right)
        return sorted_lst


    def sort(self, lst: list[T] = None) -> list[T]:
        if lst is None:
            lst = self.lst

        if len(lst) <= 1:
            return lst
        else:
            len_lst_half = len(lst) // 2
            left, right = lst[:len_lst_half], lst[len_lst_half:len(lst)]
            left = self.sort(left)
            right = self.sort(right)
            self.lst = self._merge(left, right)
            return self.lst
