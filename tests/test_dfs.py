from tests.fixtures.dfsFixtures import list_graph, backtrack_graph, tutorial_graph
from algorithms.DFS import dfs

VERBOSE = True

def test_num_sccs_listCase(list_graph):
    instance = dfs.DFS(list_graph)
    instance.process()
    num_closed_scc = len(set(instance.component))
    assert num_closed_scc == len(list_graph)
    
    
def test_num_sccs_lectureCase(backtrack_graph):
    instance = dfs.DFS(backtrack_graph, verbose=VERBOSE)
    instance.process()
    print(instance.component)
    num_closed_scc = len(set(instance.component))
    assert num_closed_scc == 4
    
def test_scc_members_tutorialCase(tutorial_graph):
    instance = dfs.DFS(tutorial_graph, verbose=VERBOSE)
    instance.process()
    sol_component = ['a', 'b', 'b', 'b', 'b', 'a', 'a', 'h']

    assert sol_component == dfs.map_to_char(instance.component)      
    
def test_intermediate_tutorialCase(tutorial_graph):
    instance = dfs.DFS(tutorial_graph, verbose=VERBOSE)
    instance.process(yield_after_step=12)
    _, _, components = instance.intermediate_result
    sol_component = ['-', 'b', 'b', 'b', 'b', '-', '-', '-']
    assert sol_component == dfs.map_to_char(components)      
    