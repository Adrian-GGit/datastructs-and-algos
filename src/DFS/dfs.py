
class DFS:

    def __init__(self, E: dict[int, list[int]], verbose = False) -> None:
        self.E = E  # adjacency list
        self.V = list(E.keys())
        self.reset()
        self.verbose = verbose

    def annotate(func: callable):
        def inner(self, *args):
            if self.verbose:
                print(f"{func.__name__}{args}")
            func(self, *args)
        return inner

    def reset(self):
        self.dfs_pos = 1
        self.dfs_num = [-1] * len(self.V)
        self.component = [v for v in self.V]     # list of corr. component for each node
        self.visited = set()                    # "marked" nodes
        self.open_nodes = []                    # stack of all nodes in open sccs
        self.open_reps = []                     # stack of all representatives of open sccs
        self.finished = False

    def dfs(self):
        for v in self.V:
            if v in self.visited:
                continue
            self.visited.add(v)
            self._root(v)
            self._dfs(v,v)
        self.finished = True

    def _dfs(self, u: int, v: int):
        for w in self.E[v]: # all (v, w) in E
            if w in self.visited:
                self._traverse_non_tree_edge(v, w)
            else:
                # add w as child to v, start new DFS from w
                self._traverse_tree_edge(v, w)
                self.visited.add(w)
                self._dfs(v, w)
        self._backtrack(u, v)

    @annotate
    def _root(self, node: int):
        self.open_reps.append(node)
        self.open_nodes.append(node)
        self.dfs_num[node] = self.dfs_pos
        self.dfs_pos += 1

    @annotate
    def _traverse_non_tree_edge(self, v: int, w: int):
        if w in self.open_nodes:
            while self.dfs_num[w] < self.dfs_num[self.open_reps[-1]]:
                self.open_reps.pop()

    @annotate  
    def _traverse_tree_edge(self, v: int, w: int):
        self.open_reps.append(w)
        self.open_nodes.append(w)
        self.dfs_num[w] = self.dfs_pos
        self.dfs_pos += 1

    @annotate
    def _backtrack(self, u: int, v: int):
        if len(self.open_reps) == 0:
            return
        if v == self.open_reps[-1]:
            self.open_reps.pop()
            while True:
                w = self.open_nodes.pop()
                if w == v:
                    break
                self.component[w] = v