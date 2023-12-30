from copy import copy

def map_to_char(l: list[int]) -> list[str]:
        return [chr(x+97) if x >= 0 else "-" for x in l]

class DFS:

    def __init__(self, E: dict[int, list[int]], verbose = False) -> None:
        self.E = E  # adjacency list
        self.V = list(E.keys())
        self.reset()
        self.verbose = verbose

    def print_members(self):
        print("\toReps:       ", map_to_char(self.open_reps))
        print("\toNodes:      ", map_to_char(self.open_nodes))
        print("\tcomponent[w]:", map_to_char(self.component))
        
    def debug(func: callable):
        def inner(self, *args):
            func(self, *args)
            self.steps += 1
            if self.verbose:
                converted_args = tuple(map(lambda x: chr(x+97), args))
                print(f"Step {self.steps}: {func.__name__}{converted_args}:")
                self.print_members()
                print("-----------")
            if self.steps == self.stop_after:
                self.intermediate_result = (copy(self.open_nodes), copy(self.open_reps), copy(self.component))
        return inner

    def reset(self):
        self.dfs_pos = 1
        self.dfs_num = [-1] * len(self.V)
        self.component = [-1] * len(self.V)            # list of corr. component for each node. Per default, each node is its own component
        self.visited = set()                     # "marked" nodes
        self.open_nodes = []                     # stack of all nodes in open sccs
        self.open_reps = []                      # stack of all representatives of open sccs
        self.finished = False
        self.steps = 0
        self.stop_after = None

    def process(self, yield_after_step=-1):
        self.stop_after = yield_after_step
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

    @debug
    def _root(self, node: int):
        self.open_reps.append(node)
        self.open_nodes.append(node)
        self.dfs_num[node] = self.dfs_pos
        self.dfs_pos += 1

    @debug
    def _traverse_non_tree_edge(self, v: int, w: int):
        if w in self.open_nodes:
            while self.dfs_num[w] < self.dfs_num[self.open_reps[-1]]:
                self.open_reps.pop()

    @debug  
    def _traverse_tree_edge(self, v: int, w: int):
        self.open_reps.append(w)
        self.open_nodes.append(w)
        self.dfs_num[w] = self.dfs_pos
        self.dfs_pos += 1

    @debug
    def _backtrack(self, u: int, v: int):
        if len(self.open_reps) == 0:
            return
        if v == self.open_reps[-1]:
            self.open_reps.pop()
            while True:
                w = self.open_nodes.pop()
                self.component[w] = v
                if w == v:
                    break