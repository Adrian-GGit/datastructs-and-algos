from pytest import fixture
AdjacencyList = dict[int,list[int]]

@fixture
def list_graph() -> AdjacencyList:
    E = dict.fromkeys(range(11))
    for i in range(10):
        E[i] = [i+1]
    E[10] = []
    return E

@fixture
def backtrack_graph() -> AdjacencyList:
    E = dict.fromkeys(range(11))
    edges = [
        [0, 1], 
        [1, 2],
        [2, 0], 
        [3, 4], 
        [4, 5],
        [4, 6], 
        [4, 7],
        [5, 6], 
        [7, 8],
        [8, 4], 
        [8, 9], 
        [9, 2],
        [9, 10], 
        [10, 3]
    ]
    for u, v in edges:
        if E[u] is None:
            E[u] = []
        E[u].append(v)
    E[6] = []
    
    return E