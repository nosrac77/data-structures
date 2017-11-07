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
    g.add_edge('A', 'B')
    assert g.graph['A'] == ['B']
