from fixtures import list_graph, backtrack_graph
from src.DFS import dfs


def test_pos_increment_after(list_graph):
    instance = dfs.DFS(list_graph)
    instance.dfs()
    num_closed_scc = len(set(instance.component))

    assert num_closed_scc == len(list_graph)
    
    
def test_pos_increment_after_bt(backtrack_graph):
    instance = dfs.DFS(backtrack_graph)
    instance.dfs()
    num_closed_scc = len(set(instance.component))
    assert num_closed_scc == 4