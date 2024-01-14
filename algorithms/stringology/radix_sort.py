import string


class RadixSort():
    def __init__(self, str_lst: list[str], chars: str = string.printable) -> None:
        self.str_lst = str_lst
        self.chars = chars
        self.max_ord = max(ord(char) for char in self.chars) + 1


    def _get_prefix_sum(self, str_lst, prefix_length):
        prefix_sum_list = [0] * self.max_ord
        for strng in str_lst:
            char_index = ord(strng[prefix_length]) if len(strng) > prefix_length else 0
            prefix_sum_list[char_index] += 1
        
        for i in range(1, len(prefix_sum_list)):
            prefix_sum_list[i] += prefix_sum_list[i - 1]

        for index, count in enumerate(prefix_sum_list):
            print(index, chr(index), count)

        return prefix_sum_list


    def sort(self):
        max_len = max(len(s) for s in self.str_lst)
            
        for pos in range(max_len - 1, -1, -1):
            num_strings = len(self.str_lst)
            output = [0] * num_strings
            count = self._get_prefix_sum(self.str_lst, pos)

            for i in range(num_strings - 1, -1, -1):
                index = ord(self.str_lst[i][pos]) if pos < len(self.str_lst[i]) else 0
                output[count[index] - 1] = self.str_lst[i]
                count[index] -= 1

            for i in range(num_strings):
                self.str_lst[i] = output[i]

        return self.str_lst