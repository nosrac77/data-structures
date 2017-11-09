"""."""
import pytest


@pytest.fixture
def new_graph():
    """Return a new graph instance."""
    from graph_2 import G
    return G()


def test_graph_2_is_dict(new_graph):
    """Function to test graph has dict upon init."""
    g = new_graph
    assert isinstance(g.graph, dict)


def test_add_edge(new_graph):
    """Function to test add_edge method of G class."""
    g = new_graph
    g.add_edge('A', 'B', 5)
    assert g.graph['A'] == ['B']


def test_breadth_first_traversal_returns_list_of_val_if_val_not_in_graph(new_graph):
    """."""
    g = new_graph
    with pytest.raises(KeyError):
        assert g.breadth_first_traversal(5)


def test_breadth_first_traversal_returns_list_with_val_if_val_no_edges(new_graph):
    """."""
    g = new_graph
    g.add_node('A')
    assert g.breadth_first_traversal('A') == ['A']


def test_breadth_first_traversal_returns_list_of_all_head_nodes_children(new_graph):
    """."""
    g = new_graph
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'F', 10)
    g.add_edge('D', 'G', 10)
    assert g.graph['A'] == ['B', 'C']
    assert g.breadth_first_traversal('A') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def test_breadth_first_traversal_returns_list_of_all_val_children(new_graph):
    """."""
    g = new_graph
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'D', 10)
    g.add_edge('B', 'X', 10)
    g.add_edge('X', 'Y', 10)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'F', 10)
    g.add_edge('D', 'G', 10)
    assert g.graph['A'] == ['B', 'C']
    assert g.breadth_first_traversal('B') == ['B', 'D', 'X', 'F', 'G', 'Y']


def test_depth_first_traversal_returns_list_with_val_if_val_no_edges(new_graph):
    """."""
    g = new_graph
    g.add_node('A')
    assert g.depth_first_traversal('A') == ['A']


def test_depth_first_traversal_returns_list_of_all_val_children(new_graph):
    """."""
    g = new_graph
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'E', 10)
    g.add_edge('B', 'C', 10)
    g.add_edge('B', 'F', 10)
    g.add_edge('C', 'D', 10)
    g.add_edge('E', 'G', 10)
    g.add_edge('G', 'H', 10)
    assert g.depth_first_traversal('A') == ['A', 'B', 'C', 'D', 'F', 'E', 'G', 'H']
