from datastructures.search_trees.search_tree import SearchTree, Node, T, V


class BinarySearchTree(SearchTree):
    def search(self, search_key: T, current_node: Node = None) -> tuple[Node]:
        current_node = current_node or self.root
        while current_node is not None and current_node.key != search_key:
            comparison_current_vs_search = self.order_relation(current_node.key, search_key)
            if comparison_current_vs_search:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return current_node


    def insert(self, key: T, value: V, current_node: Node = None) -> None:
        current_node = current_node or self.root
        new_node = Node(key, value)
        if not self.root:
            self.root = new_node
            return
        comparison = self.order_relation(current_node.key, key)
        if comparison:
            if current_node.right:
                self.insert(key, value, current_node.right)
            else:
                current_node.right = new_node
                new_node.parent = current_node
        else:
            if current_node.left:
                self.insert(key, value, current_node.left)
            else:
                current_node.left = new_node
                new_node.parent = current_node
        return


    def delete(self, key: T) -> V | None:
        found_node = self.search(key)
        if not found_node:
            return None

        found_value = found_node.value
        if not found_node.left:
            self._shift_nodes(found_node, found_node.right)
        elif not found_node.right:
            self._shift_nodes(found_node, found_node.left)
        else:
            search_from_node = found_node.right if found_node.right else found_node
            min_node, _ = self._get_min_by_node(search_from_node)
            if min_node.parent != found_node:
                self._shift_nodes(min_node, min_node.right) # there can only be right nodes
                min_node.right = found_node.right
                min_node.right.parent = min_node
            self._shift_nodes(found_node, min_node)
            min_node.left = found_node.left
            min_node.left.parent = min_node
        return found_value


    def visualize(self) -> str:
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self, current_node = None):
        current_node = current_node or self.root
        if current_node.right is None and current_node.left is None:
            line = '%s' % current_node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if current_node.right is None:
            lines, n, p, x = self._display_aux(current_node.left)
            s = '%s' % current_node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if current_node.left is None:
            lines, n, p, x = self._display_aux(current_node.right)
            s = '%s' % current_node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(current_node.left)
        right, m, q, y = self._display_aux(current_node.right)
        s = '%s' % current_node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2