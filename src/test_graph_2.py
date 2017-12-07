"""Tests for graph 2."""
import pytest


@pytest.fixture
def g():
    """Fixture for new graph instance, called g."""
    from graph_2 import G
    g = G()
    return g


def test_graph_2_is_dict(g):
    """Function to test graph has dict upon init."""
    assert isinstance(g.graph, dict)


def test_graph_2_has_weight(g):
    """G has weight."""
    assert g.weights == {}


def test_add_edge(g):
    """Function to test add_edge method of G class."""
    g.add_edge('A', 'B', 5)
    assert g.graph['A'] == ['B']


def test_add_node(g):
    """Function to test that the add_node method is functional."""
    g.add_node(1)
    g.add_node(400)
    assert g.graph == {1: [], 400: []}
    assert len(g.graph) == 2


def test_edges(g):
    """Test that edges returns a list of all edges."""
    g.add_edge(1, 3, 1000)
    g.add_edge('A', 'Flerg', 300)
    assert g.edges() == [(1, 3), ('A', 'Flerg')]


def test_nodes(g):
    """Test that nodes returns a list of all nodes."""
    g.add_node(1)
    g.add_node('A')
    assert g.nodes() == [1, 'A']


def test_del_node(g):
    """Del node deletes node, and references to node in edges."""
    g.add_node(5)
    g.add_edge(5, 25, 100)
    g.del_node(5)
    assert g.edges() == []
    assert g.nodes() == [25]


def test_del_node_not_in_graph(g):
    """Del node deletes node, and references to node in edges."""
    with pytest.raises(KeyError):
        assert g.del_node(100)


def test_breadth_first_traversal_returns_list_of_val_if_val_not_in_graph(g):
    """."""
    with pytest.raises(KeyError):
        assert g.breadth_first_traversal(5)


def test_breadth_first_traversal_returns_list_with_val_if_val_no_edges(g):
    """."""
    g.add_node('A')
    assert g.breadth_first_traversal('A') == ['A']


def test_breadth_first_traversal_returns_list_of_all_head_nodes_children(g):
    """."""
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'F', 10)
    g.add_edge('D', 'G', 10)
    assert g.graph['A'] == ['B', 'C']
    assert g.breadth_first_traversal('A') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def test_breadth_first_traversal_returns_list_of_all_val_children(g):
    """."""
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


def test_depth_first_traversal_returns_list_with_val_if_val_no_edges(g):
    """."""
    g.add_node('A')
    assert g.depth_first_traversal('A') == ['A']


def test_depth_first_traversal_val_not_a_node(g):
    """Test that KeyError is raised if val not in graph."""
    g.add_edge(1, 2, 300)
    with pytest.raises(KeyError):
        assert g.depth_first_traversal(400)


def test_depth_first_traversal_returns_list_of_all_val_children(g):
    """DFT returns all val children in list."""
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'E', 10)
    g.add_edge('B', 'C', 10)
    g.add_edge('B', 'F', 10)
    g.add_edge('C', 'D', 10)
    g.add_edge('E', 'G', 10)
    g.add_edge('G', 'H', 10)
    assert g.depth_first_traversal('A') == ['A', 'B', 'C', 'D', 'F', 'E', 'G', 'H']


def test_depth_first_traversal_does_not_repeat_edges_with_looped_modes(g):
    """Test that DFT doesnt enter an infinite loop."""
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 10)
    g.add_edge(3, 4, 10)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 10)
    g.add_edge(6, 3, 10)
    g.add_edge(7, 3, 10)
    assert g.depth_first_traversal(3) == [3, 4, 5, 6]


def test_breadth_first_traversal_does_not_repeat_edges_with_looped_modes(g):
    """Test that BFT doesnt enter an infinite loop."""
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 10)
    g.add_edge(3, 4, 10)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 10)
    g.add_edge(6, 3, 10)
    g.add_edge(7, 3, 10)
    assert g.breadth_first_traversal(3) == [3, 4, 5, 6]
